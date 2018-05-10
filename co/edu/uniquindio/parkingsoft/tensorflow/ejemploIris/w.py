from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import argparse
import co.edu.uniquindio.parkingsoft.tensorflow.ejemploIris


import sys


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')




def main(argv):


 

    args = parser.parse_args(argv[1:])
    print(args.train_steps)
    print(args.batch_size)

    (train_x, train_y), (test_x, test_y) = est_data.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10, 10],
        n_classes=2)

    classifier.train(
         input_fn=lambda:est_data.train_input_fn(train_x, train_y, args.batch_size),
         steps=args.train_steps)




    eval_result = classifier.evaluate(
        input_fn=lambda:est_data.eval_input_fn(test_x, test_y,
                                                args.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    expected = ['Lleno', 'Medio', 'Vacio']
    predict_x = {
        'colorUno': [1, 2, 6],
        'colorDos': [2, 8, 1],
        'colorTres': [3, 2, 2],
       
    }

    predictions = classifier.predict(
        input_fn=lambda:est_data.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=args.batch_size))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        print(type(class_id))
        print (class_id)
        probability = pred_dict['probabilities'][class_id]

        print(template.format(est_data.ESTADO[class_id],
                              100 * probability, expec))
if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
