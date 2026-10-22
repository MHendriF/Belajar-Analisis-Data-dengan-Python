import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'

try:
    df = pd.read_csv(url)
except Exception as e:
    print(f"Peringatan: Gagal mengunduh langsung dari Yahoo Finance ({e}). Menggunakan data simulasi BBCA.")
    dates = pd.date_range(start="2022-02-14", end="2023-02-14", freq="B")
    np.random.seed(42)
    base_price = 7500 + np.cumsum(np.random.randn(len(dates)) * 50)
    df = pd.DataFrame({
        'Date': dates,
        'Open': base_price + np.random.randn(len(dates)) * 20,
        'High': base_price + 60,
        'Low': base_price - 60,
        'Close': base_price,
        'Adj Close': base_price
    })

df['Date'] = pd.to_datetime(df['Date'])
df_boxplot = df[["Open", "High", "Low", "Close", "Adj Close"]]

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_boxplot, palette="rocket")
plt.title("Distribusi Harga Saham BBCA", fontsize=16)
plt.ylabel('Price (IDR)', fontsize=12)
plt.xlabel('Attributes', fontsize=12)
plt.tight_layout()
plt.show()