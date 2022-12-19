# Define function to fit model and predict values
# Modificar-la en funció d'una llista de mètriques...
def fit_n_predict(X_train, X_test, y_train, model):
    
    fitted_model = model
    fitted_model = fitted_model.fit(X_train, y_train)
    predictions = fitted_model.predict(X_test)
    
    print("Accuracy Score: {:.2f}".format(accuracy_score(y_test, predictions)))
    print("Precision Score: {:.2f}".format(precision_score(y_test, predictions)))
    print("Recall Score:{:.2f}".format(recall_score(y_test, predictions)))
    print("F1 Score: {:.2f}".format(f1_score(y_test, predictions)))
    
    return fitted_model, predictions

clf, predictions_clf = fit_n_predict(X_train, X_test, y_train, clf)