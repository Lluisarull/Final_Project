import seaborn as sns
import matplotlib.pyplot as plt
"""Utility for visualizing data outliers"""


def outliers_printer(df, list_of_columns):
    """This functions gives the visual representation of the input variable's
    distribution, including the presence of the outliers

    Parameters
    ----------
    list_of_columns =  a list of columns with numerical values for which you
    want to visualize its distribution

    Returns:
    ----------
    The function uses the boxplot function from the seaborn library to return
    a boxplot of the data and displays it using show."""

    i = 1
    plt.figure(figsize=(20, 10))
    for col in list_of_columns:
        plt.subplot(3, 3, i)
        sns.boxplot(df[col])

    i = i+1
