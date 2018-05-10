from __future__ import absolute_import, division, print_function

import csv

import tensorflow as tf
import tensorflow.contrib.eager as tfe

train_dataset_file = "parqueadero.csv"
train_test_dataset_file = "parqueadero_test.csv"

CSV_COLUMN_NAMES = ['horaEntrada', 'fechaEntrada', 'tipoVehiculo', 'etiqueta']


try:
    with open(train_dataset_file, "w") as f:
        print(f)
        archivo = csv.reader(f)
        for reg in archivo:
            print(train_test_dataset_file)

    with open(train_test_dataset_file, "w") as g:
        print(g)
except IOError as e:
    print("Uh oh! Esto no existe")


def parse_csv(valor):
    ejemplo_default = [[''], [''], [''], ['']]
    linea_analizada = tf.decode_csv(valor, ejemplo_default)
    caracteristicas = tf.reshape(linea_analizada[:-1], shape=(3,))
    etiquetas = tf.reshape(linea_analizada[-1], shape=())
    return caracteristicas, etiquetas


train_dataset = tf.data.TextLineDataset(train_dataset_file)
train_dataset = train_dataset.skip(1)
train_dataset = train_dataset.map(parse_csv)
train_dataset = train_dataset.shuffle(buffer_size=100)
train_dataset = train_dataset.batch(32)

caracteristicas, etiquetas = iter(train_dataset).next()
print("Ejemplo de caracteristicas: ", caracteristicas[0])
print("Ejemplo de etiquetas: ", etiquetas[0])

modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(3)
])


def perdida_modelo(modelo, x, y):
    y_ = modelo(x)
    return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)


def gradiente(modelo, entradas, objetivos):
    with tf.GradientTape() as tipo:
        perdida_valor = perdida_modelo(modelo, entradas, objetivos)
    return tipo.gradient(perdida_valor, modelo.variables)


optimizador = tf.train.GradientDescentOptimizer(learning_rate=0 - .1)

resultados_entrenamiento_perdidos = []

resultados_precision_entrenamiento = []

num_particiones = 201

for particion in range(num_particiones):
    particion_perdida_avg = tfe.metrics.Mean()
    particion_exactitud = tfe.metrics.Accuracy()

    for x, y in train_dataset:
        grad = gradiente(modelo, x, y)
        optimizador.apply_gradients(zip(grad, modelo.variables),
                                    global_step=tf.train.get_or_create_global_step())

        resultados_entrenamiento_perdidos(perdida_modelo(modelo, x, y))
        particion_exactitud(tf.argmax(modelo(x), axis=1, output_type=tf.int32), y)

    resultados_entrenamiento_perdidos.append(particion_perdida_avg.result())
    resultados_precision_entrenamiento.append(particion_exactitud.result())

    if particion % 50 == 0:
        print("Particion {:03d}: Perdida: {:.3f}, Exactitud: {:.3%}".format(particion, particion_perdida_avg.result(),
                                                                            particion_exactitud.result()))

test_dataset = tf.data.TextLineDataset(train_test_dataset_file)
test_dataset = test_dataset.skip(1)
test_dataset = test_dataset.map(parse_csv)
test_dataset = test_dataset.shuffle(1000)
test_dataset = test_dataset.batch(32)

precision_test = tfe.metrics.Accuracy()

for (x, y) in test_dataset:
    prediccion = tf.argmax(modelo(x), axis=1, output_type=tf.int32)
    precision_test(prediccion, y)

print("Precision del modelo de entrenamiento: {:.3%}".format(precision_test.result()))

class_ids = ['Lleno', 'Medianamente Lleno', 'Vacio']

predecir_dataset = tf.convert_to_tensor([
    [5.1, 3.3, 1.7, 0.5, ],
    [5.9, 3.0, 4.2, 1.5, ],
    [6.9, 3.1, 5.4, 2.1]
])

predicciones = modelo(predecir_dataset)

for i, logits in enumerate(predicciones):
    class_idx = tf.argmax(logits).numpy()
    nombre = class_ids[class_idx]
    print("Ejemplo {} prediccion: {}".format(i, nombre))
