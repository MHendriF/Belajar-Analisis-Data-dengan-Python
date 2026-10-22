# Interpolation: menghitung titik data baru berdasarkan range data yang sudah ada menggunakan garis linear ataupun polynomial

import os
import pandas as pd

file_path = "bbca_index.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame({
        'day': [1, 2, 3, 4, 5],
        'close_price': [8000.0, None, 8200.0, None, 8500.0]
    })

print("Data awal:")
print(data)

# Mengisi missing value dengan interpolasi linear
data['close_price'] = data['close_price'].interpolate(method='linear', limit_direction='forward')

print("\nData setelah interpolasi:")
print(data)