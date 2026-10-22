import os
import pandas as pd

file_path = "data.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame({
        'TotalCharges': [100.0, 150.0, 200.0, 220.0, 180.0, 190.0, 5000.0, -100.0]
    })

q1 = df['TotalCharges'].quantile(0.25)
q3 = df['TotalCharges'].quantile(0.75)
iqr = q3 - q1

maximum = q3 + (1.5 * iqr)
minimum = q1 - (1.5 * iqr)

# Menghapus outlier menggunakan boolean indexing
filtered_df = df[(df['TotalCharges'] >= minimum) & (df['TotalCharges'] <= maximum)].copy()

print(f"Batas minimum: {minimum:.2f}, Batas maksimum: {maximum:.2f}")
print(f"Jumlah baris sebelum filtering: {len(df)}")
print(f"Jumlah baris setelah filtering outlier: {len(filtered_df)}")
print(filtered_df)