# Define a global function to tune the hyperparameters of the model

def tuning(model, parameters, X_train, y_train):
    
    random_estimator = RandomizedSearchCV(estimator = model,
                                          param_distributions = parameters,
                                          n_iter=10, 
                                          scoring='accuracy', 
                                          n_jobs=-1, 
                                          cv=5, 
                                          verbose=3, 
                                          random_state=420)
    
    random_estimator.fit(X_train, y_train)

    print ('Best Estimator: ', random_estimator.best_estimator_, ' \n')
    
    chosen_model = random_estimator.best_estimator_
    
    return chosen_model