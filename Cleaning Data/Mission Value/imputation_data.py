# Imputation : mengisi (fill) missing value dengan nilai tertentu

import pandas as pd
    
data=pd.read_csv('employee_data.csv')
    
data.age.fillna(value=data.age.mean(), inplace=True)