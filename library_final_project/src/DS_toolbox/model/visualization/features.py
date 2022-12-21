import matplotlib as plt
import pandas as pd
"""Utility for visualizations of the model features"""


def plot_feats(model, X):
    """
    This function creates a bar plot of the importance of the features of the
    model sorted.
    Parameters:
    --------------
    - model: model
    - X: input data
    """
    model.feature_importances_

    features = X.columns

    importances_clf = pd.Series(data=model.feature_importances_,
                                index=features)

    # Sort importances
    importances_sorted_clf = importances_clf.sort_values()

    # Draw a horizontal barplot of importances_sorted
    importances_sorted_clf.plot(kind='barh', color='sandybrown')
    plt.title('Gini Features Importances', size=15)
    plt.show()
