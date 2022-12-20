import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from DS_toolbox.data.transformation.categorical import *
from DS_toolbox.data.transformation.numerical import *
# Testing the functions
class TestDataTransformation(unittest.TestCase):
    def test_OneHotEncoding(self):
        data_to_test = pd.DataFrame(data = {'gender':['M','F','M','F','F', 'M']})
        result = OneHotEncoding(data_to_test, ['gender'])
        expected_output = pd.DataFrame(data = {'gender_F':[0,1,0,1,1,0],'gender_M':[1,0,1,0,0,1]})
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_binary_var(self):
        column = 'gender'
        labels = ['M', 'F']
        data_to_test = pd.DataFrame(data = {'gender':['M','F','M','F','F']})
        result = binary_var(data_to_test, column, labels)
        expected_output = pd.DataFrame(data = {'gender':[1,0,1,0,0]})
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_log_transf(self):
        data_to_test = pd.DataFrame(data = {"salary": [10000,20000,50000]})
        result = log_transformation(data_to_test, ["salary"])
        expected_output = pd.DataFrame(data = {"salary":[np.log(10000), np.log(20000), np.log(50000)]})
        assert_frame_equal(result, expected_output, check_dtype=False)

if __name__ == '__main__':
    unittest.main()