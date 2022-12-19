import pandas as pd
import numpy as np


def OneHotEncoding(df, list_of_columns):
    """Generate dummies for categorical column (One hot encoding)
    -----
    Parameters
    df =  
    list_of_columns: list of categorical columns that you want to transform into dummy variables"""
    return pd.get_dummies(df, columns=list_of_columns, drop_first=True)


def binary_var(df, column, labels):
    df_aux = df.copy()
    # Create a binary variable for gender M/F. labels = ["M","F"]
    df_aux[column] = df_aux[column].apply(lambda x: 1 if x == labels[0] else 0)
    df_aux[column] = pd.to_numeric(df_aux[column])

    return df_aux


def log_transformation(df, list_of_columns):
    """Log transformation of continuous variables"""
    df_aux = df.copy()
    for column in list_of_columns:
        df_aux[column]= np.log(df_aux[column])
    return df_aux
