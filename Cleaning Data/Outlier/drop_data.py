import pandas as pd
    
df = pd.read_csv("data.csv")
    
Q1 = (df['TotalCharges']).quantile(0.25)
Q3 = (df['TotalCharges']).quantile(0.75)
IQR = Q3 - Q1
    
maximum = Q3 + (1.5*IQR)
minimum = Q1 - (1.5*IQR)
    
kondisi_lower_than = df['TotalCharges'] < minimum
kondisi_more_than = df['TotalCharges'] > maximum
    
df.drop(df[kondisi_lower_than].index, inplace=True)
df.drop(df[kondisi_more_than].index, inplace=True)