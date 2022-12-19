# Define a function for plotting feature importances 

def plot_feats(fitted_model):
    fitted_model.feature_importances_

    features = X.columns

    importances_clf = pd.Series(data = fitted_model.feature_importances_,
                                index= features)

    # Sort importances
    importances_sorted_clf = importances_clf.sort_values()

    # Draw a horizontal barplot of importances_sorted
    importances_sorted_clf.plot(kind='barh', color='sandybrown')
    plt.title('Gini Features Importances', size=15)
    plt.show()
    
plot_feats(clf)

# Define function for plotting a confusion matrix

def conf_mat(y_test, model_predict):

    cm = confusion_matrix(y_test, model_predict, labels=[0,1])
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, cmap="Blues", annot = True)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    
conf_mat(y_test, predictions_clf)