# Interpolation : menghitung titik data baru berdasarkan range data yang sudah ada menggunakan garis linear ataupun polynomial

import pandas as pd

data=pd.read_csv('bbca_index.csv')

data.close_price.interpolate(method='linear', limit_direction='forward', inplace=True)