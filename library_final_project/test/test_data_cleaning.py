import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from DS_toolbox.data.cleaning.nan_manager import *
from DS_toolbox.data.cleaning.outliers_processor import *

# Testing the functions
class TestDataCleaning(unittest.TestCase):
    def test_clearNA(self):
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan], "gender":["M",np.nan, "F"]})
        expected_output = pd.DataFrame(data = {"age":[18, 22], "gender": ["M", np.nan]})
        result = clearNA_from_column(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_fillNA_mean(self):
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
        expected_output = pd.DataFrame(data = {"age":[18, 22, 20]})
        result = fillNA_mean(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

if __name__ == "__main__":
    unittest.main()


