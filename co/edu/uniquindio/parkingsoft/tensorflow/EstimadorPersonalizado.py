from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import tensorflow as tf
from tensorflow.python.platform.app import run

from co.edu.uniquindio.parkingsoft.tensorflow import ParqueaderoData

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')


def main():


    (train_x, train_y) = ParqueaderoData.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10, 10],
        n_classes=3)

    print(train_y)
    dato = 100
    classifier.train(
        input_fn=lambda: ParqueaderoData.train_input_fn(train_x, train_y, 100))





    # Generate predictions from the model
    expected = ['Lleno', 'Medio', 'Vacio']
    predict_x = {
        'dia': [2.0],


    }

    predictions = classifier.predict(
        input_fn=lambda: ParqueaderoData.eval_input_fn(predict_x,
                                                       labels=None,
                                                       batch_size=100))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        print(type(class_id))
        print(class_id)
        probability = pred_dict['probabilities'][class_id]

        print(template.format(ParqueaderoData.ESTADO[class_id],
                              100 * probability, expec))




if __name__ == '__main__':
    #tf.logging.set_verbosity(tf.logging.INFO)
    main()

