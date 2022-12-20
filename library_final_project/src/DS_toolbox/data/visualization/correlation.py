import seaborn as sns
import matplotlib.pyplot as plt

def correlation_matrix(df):
    """Calculate and plot the correlation matrix for all the numerical variables in the data frame
     
     Parameters
     ----------
     df =  Input DataFrame

     Returns
     ----------
     corr = Correlation matrix for the input DataFrame."""

    ax = plt.figure(figsize=(12,10))
    sns.heatmap(df.corr(),annot=True,cmap="Blues", fmt='.0%')
    plt.show()