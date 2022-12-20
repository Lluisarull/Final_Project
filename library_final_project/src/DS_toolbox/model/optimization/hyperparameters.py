from sklearn.model_selection import RandomizedSearchCV


def tuning(model, random_grid, scoring, X, y):
    """
    This function finds the best combination of hyperparameter values from a random grid
    of values for the model.
    Parameters:
    --------------
    - model: model to optimize hyperparameters
    - random_grid: grid of values for RandomizedSearch to try. Look at sklearn RandomizedSearchCV for more info
    - scoring: str score identifier from sklearn to optimize the hyperparameters
    - y: real target values
    - X: X training data
    
    Returns:
    - model tuned with best hyperparameters and best split from kfold
    - dict of best hyperparameters
    """
    
    search = RandomizedSearchCV(estimator = model,
                                          param_distributions = random_grid,
                                          n_iter=5, 
                                          scoring=scoring, 
                                          n_jobs=-1, 
                                          cv=5, 
                                          random_state=420)
    
    search.fit(X, y)

    print ('Best Estimator: ', search.best_estimator_)
    print ('Optimized Hyperparameters: ', search.best_params_)
    optmizied_model = search.best_estimator_
    
    return optmizied_model, search.best_params_


