import seaborn as sns 
import matplotlib.pyplot as plt

def outliers_printer(df,list_of_columns):
  i=1
  plt.figure(figsize = (20,10))
  for col in list_of_columns:
    plt.subplot(3,3,i)
    sns.boxplot(df[col])

    i=i+1