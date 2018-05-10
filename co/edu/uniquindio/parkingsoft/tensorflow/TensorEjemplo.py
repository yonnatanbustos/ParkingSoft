from __future__ import absolute_import, division, print_function

import tempfile
import shutil
import tensorflow as tf

_CSV_COLUMNAS = [
    'fechaEntrada', 'horaEntrada', 'tipoVehiculo', 'cantidad']

_CSV_COLUMNA_DEFAULTS = [[''], [''], [''], ['']]

_NUM_EJEMPLOS = {
    'train': 32561,
    'validation': 16281,
}


def construir_columnas_modelo():
    tipoVehiculo = tf.feature_column.categorical_column_with_vocabulary_list('tipoVehiculo', ['CARRO', 'MOTO'])

    fechaEntrada = tf.feature_column.categorical_column_with_hash_bucket('fechaEntrada', hash_bucket_size=2000)
    horaEntrada = tf.feature_column.categorical_column_with_hash_bucket('horaEntrada', hash_bucket_size=2000)
    fechaEntrada_x_horaEntrada = tf.feature_column.crossed_column(['fechaEntrada', 'horaEntrada'],
                                                                  hash_bucket_size=2000)

    columnas_base = [tipoVehiculo]
    columnas_cruzadas = [tf.feature_column.crossed_column(['fechaEntrada', 'horaEntrada'], hash_bucket_size=2000)]

    model_dir = tempfile.mkdtemp()
    model = tf.estimator.LinearClassifier(model_dir=model_dir, feature_columns=columnas_base + columnas_cruzadas)
    model.train(input_funcion=lambda: input_funcion(train_data, num_epochs, ))


# batch_size - tamño del lote
# delta_file - archivo del conjunto de entrenamiento


def input_funcion(delta_file, num_epochs, shuffle, batch_size):
    assert tf.gfile.Exists(delta_file), ('%s extraviado. Asegúrese de haber ejecutado data_download.py'
                                         ' y establecer ambos argumentos --train_data y --test_data.' % delta_file)

    def parse_csv(value):
        print('anilisis', delta_file)
        columnas = tf.decode_csv(value, record_defaults=_CSV_COLUMNA_DEFAULTS)
        caracteristicas = dict(zip(_CSV_COLUMNAS, columnas))
        etiquetas = caracteristicas.pop('cantidad')
        return caracteristicas, tf.equal(etiquetas, '>23')

    # Extraer líneas de archivos de entrada utilizando la API Dataset
    dataset = tf.data.TextLineDataset(delta_file)
    if shuffle:
        dataset = dataset.shuffle(buffer_size=_NUM_EJEMPLOS)

    dataset = dataset.map(parse_csv, num_parallel_calls=5)

    # Llamamos repetir después de barajar, en lugar de antes, para evitar que se separen
    # épocas de la mezcla.
    dataset = dataset.repeat(num_epochs)
    dataset = dataset.batch(batch_size)

    iterador = dataset.make_one_shot_iterator()
    caracteristicas, etiquetas = iterador.get_next()
    return caracteristicas, etiquetas


def exportar_modelo(modelo, tipo_modelo, export_dir):
    wipe_columns, deep_columns = construir_columnas_modelo()
    if tipo_modelo == 'wide':
        columns = tipo_modelo
    elif tipo_modelo == 'deep':
        columns = deep_columns
    else:
        columns = tipo_modelo + deep_columns

    caracteristica_especifica = tf.feature_column.make_parse_example_spec(columns)
    ejemplo_input_funcion = (tf.estimator.export.build_parsing_serving_input_receiver_fn(feature_spec=caracteristica_especifica))
    modelo.export_savedmodel(export_dir, ejemplo_input_funcion)


def correr_muy_profundo(flags_obj):

    shutil.rmtree(flags_obj.model_dir, ignore_errors=True)
    model =estimandor_construccion(flags_obj.model_dir, flags_obj.tipo_modelo)


def estimandor_construccion(model_dir, tipo_modelo):
    wide_columns, deep_columns = construir_columnas_modelo()
    hidden_units = [100, 75, 50, 25]
    configuracion_run = tf.estimator.RunConfig().replace(sesion_config= tf.ConfigProto(device_count={'GPU':0}))

    if tipo_modelo == 'wide':
        return tf.estimator.LinearClassifier(model_dir=model_dir, feature_columns=wide_columns, config=configuracion_run)
    elif tipo_modelo == 'deep':
        return tf.estimator.DNNClassifier(model_dir=model_dir, feature_columns=deep_columns, hidden_units=hidden_units, config=configuracion_run)
    else:
        return tf.estimator.DNNLinearCombinedClassifier(model_dir=model_dir, linear_feature_columns=wide_columns, dnn_feature_columns=deep_columns,
                                                        dnn_hidden_units=hidden_units, config=configuracion_run)


