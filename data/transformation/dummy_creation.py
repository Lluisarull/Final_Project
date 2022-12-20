import pandas as pd
import numpy as np


def OneHotEncoding(df, list_of_columns):
    """Generate dummies for categorical column (One hot encoding)
    
    Parameters:
    ----------
    list_of_columns: list of categorical columns that you want to transform into dummy variables
    
    Returns:
    ----------
    This function returns as output the data frame including every specified categorical variable in list_of_columns as a new column
    for every category coded in binary (1 for being in the corresponding category and 0 otherwise). """
    
    return pd.get_dummies(df, columns=list_of_columns, drop_first=True)


def binary_var(df, column, labels):
    """ This function creates a binary variable from a categorical variable with two given categories
   
    Parameters:
    ---------
    column = specify the column which is going to be transformed to a binary variable
    labels = apply the correspondent numerical value

    Returns:
    ---------
    This function returns a new data frame having converted the categorical variable with two labels to a 
    binary variable, assigning for every category a value equal to 0 or 1."""
    
    df_aux = df.copy()
    # Create a binary variable for gender M/F. labels = ["M","F"]
    df_aux[column] = df_aux[column].apply(lambda x: 1 if x == labels[0] else 0)
    df_aux[column] = pd.to_numeric(df_aux[column])

    return df_aux


