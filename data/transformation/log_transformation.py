
def log_transformation(df, list_of_columns):
    """This function carries out a Log transformation of continuous variables
    
    Parameters
    ----------
    list_of_columns = list of of columns in which we want to apply a log transformation (continuous variables)
    
    Returns:
    ----------
    This function returns a new data frame where the columns specified are log-transformed. """
    
    df_aux = df.copy()
    for column in list_of_columns:
        df_aux[column]= np.log(df_aux[column])
    return df_aux

