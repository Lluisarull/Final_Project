
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from EinesDeJardiner.Dummy_Creation import OneHotEncoding, binary_var

# Testing the functions
class Test_Dummy_Creation(unittest.TestCase):
    def test_OneHotEncoding(self):
        data_to_test = pd.DataFrame(data = {'gender':['M','F','M','F','F', 'I']})
        result = OneHotEncoding(data_to_test, ['gender'])
        expected_output = pd.DataFrame(data = {'gender_I':[0,0,0,0,0,1],'gender_M':[1,0,1,0,0,0]})
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_binary_var(self):
        column = 'gender'
        labels = ['M', 'F']
        data_to_test = pd.DataFrame(data = {'gender':['M','F','M','F','F']})
        result = binary_var(data_to_test, column, labels)
        expected_output = pd.DataFrame(data = {'gender':[1,0,1,0,0]})
        assert_frame_equal(result, expected_output, check_dtype=False)

if __name__ == '__main__':
    unittest.main()


