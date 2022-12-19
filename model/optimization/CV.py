import numpy as np

def CV_model(X , y, kf, model, metric, the_greater_the_better = True):
    """This function allows for a cross validationtraining returning all the important information
    of the best fold training.
    
    Parameters:
    --------------
    - y: real target values
    - X: X training data
    - kf: KFold object to split data
    - model: model to evaluate
    - metric: metric function from sklearn
    - the_greater_the_better: boolean parameter to indicate if the score has to be maximized or minimized
    
    Returns:
    - model trained with the best split
    - X testing data of the split that gave the best model
    - y testing data of the split that gave the best model
    - predictions over X testing of the split that gave the best model
    - mean of the chosen metric over all folds"""

    metrics_list = []
    
    if the_greater_the_better:
        best_metric = 0
    
    if not the_greater_the_better:
        best_metric = 1000
    
    for train_index, test_index in kf.split(X):

        X_train, X_test = np.matrix(X)[train_index], np.matrix(X)[test_index]
        y_train, y_test = np.array(y)[train_index], np.array(y)[test_index]
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        metric_val = metric(y_test, y_pred)
        metrics_list.append(metric_val)

        if the_greater_the_better:

            if metric_val > best_metric:
                
                final_model = model
                final_X_test = X_test
                final_y_pred = y_pred
                final_y_test = y_test
                best_metric = metric_val
        else:

            if metric_val < best_metric:
                
                final_model = model
                final_X_test = X_test
                final_y_pred = y_pred
                final_y_test = y_test
                best_metric = metric_val

    return final_model, final_X_test, final_y_test, final_y_pred, np.mean(metrics_list)