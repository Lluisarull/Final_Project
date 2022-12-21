import seaborn as sns
import matplotlib.pyplot as plt
"""Utility for different types of correlation visualization of the data"""


def correlation_matrix(df):
    """Calculate and plot the correlation matrix for all the numerical
    variables in the data frame

     Parameters
     ----------
     df =  Input DataFrame

     Returns
     ----------
     corr = Correlation matrix for the input DataFrame."""

    ax = plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap="Blues", fmt='.0%')
    plt.show()


def big_panel(df, target):
    """Shows the correlations between all the variables of the dataset
    indicating the target in red

     Parameters
     ----------
     df =  Input DataFrame
     target = label for target column

     Returns
     ----------
     corr = Correlation matrix for the input DataFrame."""
    sns.set(style="ticks")
    sns.pairplot(df, hue=target)
