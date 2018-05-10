
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import pandas as pd

from six.moves import StringIO

from co.edu.uniquindio.parkingsoft.tensorflow import ParqueaderoData, EstimadorPersonalizado

FOUR_LINES = "\n".join([
    "10052018,540, 1",
    "9052018, 959, 1",
    "17062015, 136, 0",
    "23122010, 1730, 0",])

def four_lines_data():
    text = StringIO(FOUR_LINES)

    df = pd.read_csv(text, names=ParqueaderoData.CSV_COLUMN_NAMES)
    xy = (df, df.pop("etiqueta"))
    return xy, xy

class RegressionTest(tf.test.TestCase):

    @tf.test.mock.patch.dict(EstimadorPersonalizado.__dict__,
                             {"load_data": four_lines_data})
    def test_premade_estimator(self):
        EstimadorPersonalizado.main([None, "--train_steps=1"])

    @tf.test.mock.patch.dict(EstimadorPersonalizado.__dict__,
                             {"load_data": four_lines_data})
    def test_custom_estimator(self):
        EstimadorPersonalizado.main([None, "--train_steps=1"])


if __name__ == "__main__":
    tf.test.main()
