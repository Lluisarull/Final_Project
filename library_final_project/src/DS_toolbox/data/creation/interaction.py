import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
"""Utility for creating new variables related to the interaction of the
existing ones of the database"""


def poly_feature_creation(df_scaled,
                          list_of_columns,
                          max_degree,
                          interaction_only=True):
    """This function adds to the existing data frame all the possible
    interactions between the specified columns given a maximum
    polynomial degree.

    Parameters
    ----------
    df_scaled =  the resulting data frame after standardizing the independent
    numerical variables (target is excluded)
    list_of_columns =  the columns for which we want to apply the interactions
    max_degree = it specifies the maximal degree of the polynomial features.

    Returns:
    ----------
    The function returns the original data frame including new columns for
    each of the interactions."""

    df_aux = df_scaled.copy()
    X = df_aux[list_of_columns]
    poly = PolynomialFeatures(degree=max_degree,
                              interaction_only=interaction_only,
                              include_bias=False).fit(X)
    poly_cols = [x.lower().replace(" ", "x") for x in
                 poly.get_feature_names(list_of_columns)]
    X_overfitted = pd.DataFrame(data=poly.transform(X), columns=poly_cols)
    for column in poly_cols:
        df_aux[column] = X_overfitted[column]

    return df_aux
