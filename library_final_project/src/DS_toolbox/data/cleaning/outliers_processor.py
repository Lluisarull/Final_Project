import numpy as np


def check_outliers_IQM(df, vars_without_outliers):
    """This function finds outliers using the interquartile method.

    Parameters
    ----------
    vars_without_outliers = list of variables that dont have outliers
    (categorical and binary vars)

    Returns:
    ----------
    It returns a dictionary with the total number of outliers and the index
    of them for each var that HAS outliers  """

    outliers = dict()
    for column in df.columns:
        if column in vars_without_outliers:
            continue
        else:
            q25, q75 = np.quantile(df[column], 0.25), np.quantile(df[column],
                                                                  0.75)
            IQR = q75 - q25
            lower, upper = q25 - IQR*1.5, q75 + IQR*1.5
            outliers_index = ((df[column] < lower) | (df[column] > upper))
            df_no_out = df_no_out[~outliers_index]
            if len(outliers_index == True) == 0:
                continue
            else:
                output = {
                    "indexes": outliers_index,
                    "quantity": outliers_index.sum(axis=0)
                }
            outliers[column] = output
    return outliers, df_no_out


def check_outliers_std_dev(df, vars_without_outliers):
    """This function finds outliers using the standard deviation method.

    Parameters
    ----------
    vars_without_outliers = list of variables that dont have outliers
    (categorical and binary vars)

    Returns:
    ----------
    It returns a dictionary with the total number of outliers and the index of
    them for each var that HAS outliers. The index 0 corresponds to the
    outliers and the index 1 corresponds to the data frame once the outliers
    have been removed."""

    df_no_out = df.copy()
    outliers = dict()
    for column in df.columns:
        if column in vars_without_outliers:
            continue
        else:
            mean = np.mean(df_no_out[column], axis=0)
            sd = np.std(df_no_out[column], axis=0)
            lower, upper = mean - 3 * sd,  mean + 3 * sd
            outliers_index = (df_no_out[column] < lower) | \
                             (df_no_out[column] > upper)
            df_no_out = df_no_out[~outliers_index]
            if len(outliers_index == True) == 0:
                continue
            else:
                output = {
                    "indexes": outliers_index,
                    "quantity": outliers_index.sum(axis=0)
                }
            outliers[column] = output
    return outliers, df_no_out