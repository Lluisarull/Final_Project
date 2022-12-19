def clearNA_from_column(df, list_of_columns):
    # Remove those rows that contain NaN values in the columns: age, gender, ethnicity
    return df.dropna(subset=list_of_columns, how="any")


def fillNA(df, list_of_columns):
    # Fill NaN with the mean value of the column in the columns: height, weight.
    for column in list_of_columns:
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)
    return df

def check_outliers_IQM(df, vars_without_outliers):
  """Finds outliers with interquartile methodIt gets the df and a list of variables that dont 
  have outliers (categorical and binary vars) and returns a dictionary with the total number of outliers
  and the index of them for each var that HAS outliers
  """
  outliers = dict()
  for column in df.columns:
    if column in vars_without_outliers:
      continue
    else:
      q25, q75 = np.quantile(df[column], 0.25), np.quantile(df[column], 0.75)
      IQR = q75 - q25
      lower,upper = q25 - IQR*1.5, q75 + IQR*1.5
      outliers_index = ((df[column] < lower) | (df[column] > upper))
      df_no_out = df_no_out[~outliers_index]
      if len(outliers_index == True) == 0:
        continue
      else:
        output = {
            "indexes" : outliers_index,
            "quantity" : outliers_index.sum(axis = 0)
        }
        outliers[column] = output
  return outliers, df_no_out

def check_outliers_std_dev(df, vars_without_outliers):
  df_no_out = df.copy()
  """Finds outliers with std dev method.It gets the df and a list of variables that dont 
  have outliers (categorical and binary vars) and returns a dictionary with the total number of outliers
  and the index of them for each var that HAS outliers
  """
  outliers = dict()
  for column in df.columns:
    if column in vars_without_outliers:
      continue
    else:
      mean = np.mean(df_no_out[column], axis=0)
      sd = np.std(df_no_out[column], axis=0)
      lower,upper =  mean - 3 * sd,  mean + 3 * sd
      outliers_index = (df_no_out[column] < lower) | (df_no_out[column] > upper)
      df_no_out = df_no_out[~outliers_index]
      if len(outliers_index == True) == 0:
        continue
      else:
        output = {
            "indexes" : outliers_index,
            "quantity" : outliers_index.sum(axis = 0)
        }
        outliers[column] = output
  return outliers, df_no_out