import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from DS_toolbox.data.creation.interaction import *

# Testing the functions
class TestDataCreation(unittest.TestCase):
    def test_poly_feature_creation(self):
        data_to_test = pd.DataFrame(data = {"salary": [10000, 20000], "age": [22, 30]})
        result = poly_feature_creation(data_to_test, ["salary", "age"], max_degree=2, interaction_only=False)
        expected_output = pd.DataFrame(data = { "salary": [10000, 20000], 
                                                "age": [22, 30],
                                                "salary^2": [np.power(10000,2), np.power(20000,2)],
                                                "salaryxage": [10000*22, 20000*30],
                                                "age^2": [np.power(22,2), np.power(30,2)]})
        assert_frame_equal(result, expected_output, check_dtype=False)
if __name__ == '__main__':
    unittest.main()

def poly_feature_creation(df_scaled, list_of_columns, max_degree, interaction_only = True):
    
    
    df_aux = df_scaled.copy()
    X = df_aux[list_of_columns]  
    poly = PolynomialFeatures(degree = max_degree, interaction_only = interaction_only, include_bias = False).fit(X)
    poly_cols = [x.lower().replace(" ", "x") for x in poly.get_feature_names(list_of_columns)]
    X_overfitted = pd.DataFrame(data = poly.transform(X), columns = poly_cols)
    for column in poly_cols:
        df_aux[column]=X_overfitted[column]

    return df_aux
    