import matplotlib as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
"""Utility visualizations of classification models"""


def binary_conf_mat(y_test, predictions):
    """
    This function creates a confusion matrix of the model.
    Parameters:
    --------------
    - y_test: real target values
    - predictions: predictions of the target by the model
    """
    cm = confusion_matrix(y_test, predictions, labels=[0, 1])
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, cmap="Blues", annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('True')
