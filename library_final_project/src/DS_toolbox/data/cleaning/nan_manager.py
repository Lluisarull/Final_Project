"""Utility for cleaning and managing NaNs of the database"""


def clearNA_from_column(df, list_of_columns):
    """ This function drops NaNs of a certain columns in a data frame

    Parameters
    ----------
    df = dataframe to clear
    list_of_columns = list of column names for which we wish to remove NaNs

    Returns:
    ----------
    It returns the data frame with the NaNs removed  """

    return df.dropna(subset=list_of_columns, how="any")


def fillNA_mean(df, list_of_columns):
    """ This function fills NAs imputing the missing values of certain columns
    in a data frame with the computed mean of the rest of the existing
    values in the column in question

    Parameters
    ----------
    df = dataframe to fill
    list_of_columns = list of column names for which we wish to fill NaNs

    Returns:
    ----------
    It returns the data frame with the NaNs filled  """

    for column in list_of_columns:
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)
    return df
