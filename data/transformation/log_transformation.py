
def log_transformation(df, list_of_columns):
    """Log transformation of continuous variables"""
    df_aux = df.copy()
    for column in list_of_columns:
        df_aux[column]= np.log(df_aux[column])
    return df_aux

