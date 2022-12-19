def evaluate_on_metrics(predictions, y_test, metrics_dict):
    """
    It receives predictions, real values and a group of metrics to evaluate the model 
    and returns a dict of metrics with their evaluated value.
    Parameters:
    --------------
    - predictions: vector of predictions
    - y_test: vector of real values
    - metrics_dict: dictionary with {name: metric function}
    Returns:
    - metrics_dict: a dictionary with {metric name: value}
    """
    for key in metrics_dict.keys():
        metrics_dict[key] = metrics_dict[key](y_test, predictions)
    return metrics_dict
