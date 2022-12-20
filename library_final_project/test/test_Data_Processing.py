
import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from EinesDeJardiner.Data_Processing import clearNA_from_column, fillNA

# Testing the functions
class Test_Data_Processing(unittest.TestCase):
    def test_clearNA(self):
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
        expected_output = pd.DataFrame(data = {"age":[18, 22]})
        result = clearNA_from_column(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_fillNA(self):
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
        expected_output = pd.DataFrame(data = {"age":[18, 22, 20]})
        result = fillNA(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

if __name__ == "__main__":
    unittest.main()


