import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
        'Close': base_price,
        'High': base_price + 50,
        'Low': base_price - 50,
        'Adj Close': base_price
    })

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], label='Close', color='red')
plt.plot(df['Date'], df['Open'], label='Open', color='blue')
plt.title('BBCA Stock Price', fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Price (IDR)', fontsize=15)
plt.legend()
plt.tight_layout()
plt.show()