import pandas as pd
from sklearn.preprocessing import StandardScaler

def careful_standardization(df, not_standardize_list):
  """ This function receives the DataFrame and a list of variables not to standardize
  (for example the target, binary variables, or dummy variables(categorical vars
  should have been dummified). Also can receive sub strings of dummified categorical vars.
  For example, neigborhoodcode when dummified turns into neigborhoodcode_1, neigborhoodcode_2...
  so by putting the string 'neigborhoodcode_' inside the list no dummy of 'neigborhoodcode_' will
  be standardized). The output is the same DataFrame with all the other columns standardized. 
  
  Parameters
  ----------
  not_standardized_list =  list of columns for which we don't apply the standardization process since they constitute dummy or 
  categorical variables
   
  Returns:
  ----------
  The corresponding output is the same data frame with all the columns not specified in the not_standardized_list standardized."""
  
  standardize_vars_cols = []
  dummy_vars_and_y = []

  for column in df.columns:
    for element in not_standardize_list:
    
      if element in column:
        save = False
        break
      else:
        save = True

    if save:
      standardize_vars_cols.append(column)
    else:
      dummy_vars_and_y.append(column)

  # scaler
  scaler = StandardScaler().fit(df[standardize_vars_cols])
  scaled_features = scaler.transform(df[standardize_vars_cols])
  df_scaled = pd.DataFrame(scaled_features, index = df.index, columns = df[standardize_vars_cols].columns)
  df_scaled[dummy_vars_and_y] = df[dummy_vars_and_y]

  return df_scaled