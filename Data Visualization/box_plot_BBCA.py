import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
    
url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])
    
df_boxplot = df[["Open", "High", "Low", "Close", "Adj Close"]]
    
sns.boxplot(data=df_boxplot, palette="rocket")
plt.ylabel('Price',size=15)
plt.show()