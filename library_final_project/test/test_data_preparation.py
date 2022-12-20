import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from DS_toolbox.data.preparation.standardization import *
# Testing the functions
class TestDataPreparation(unittest.TestCase):
    def test_careful_standarization(self):

        data_to_test = {"age":[20,14,15],
        "salary":[10000,20000,50000],
        "gender":[1,0,1]}
        data_to_test = pd.DataFrame(data = data_to_test)

        expected_output = {  "age": [1.397001, -0.889001, -0.508001],
            "salary":[-0.980581,-0.392232, 1.372813],
            "gender":[1,0,1]}
        expected_output = pd.DataFrame(data = expected_output)

        result = careful_standardization(data_to_test, ["gender"])
        assert_frame_equal(result, expected_output, check_dtype=False)


if __name__ == '__main__':
    unittest.main()