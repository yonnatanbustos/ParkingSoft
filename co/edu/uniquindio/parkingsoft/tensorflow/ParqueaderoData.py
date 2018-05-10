import pandas as pd
import tensorflow as tf

TRAIN_URL = "https://l.facebook.com/Estado_Animo_Training.csv"
TEST_URL = "https://l.facebook.com/Estado_Animo_Test.csv"

CSV_COLUMN_NAMES = ['dia', 'resultado']
ESTADO = ['Lleno', 'Medio', 'Vacio']


def load_data(y_name='resultado'):
    train = pd.read_csv('C:\\Users\Asus\Desktop\parqueadero_train.csv', names=CSV_COLUMN_NAMES, header=0)
    train_x, train_y = train, train.pop(y_name)

    return (train_x, train_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    labels = tf.cast(labels, tf.int32)
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset


# The remainder of this file contains a simple example of a csv parser,
#     implemented using a the `Dataset` class.

# `tf.parse_csv` sets the types of the outputs to match the examples given in
#     the `record_defaults` argument.
CSV_TYPES = [[0], [0]]


def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('resultado')

    return features, label


def csv_input_fn(csv_path, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path).skip(1)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset
