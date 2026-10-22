import os
import pandas as pd

# Contoh data atau muat dari file CSV jika tersedia
file_path = "data.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    # Sample DataFrame untuk demonstrasi penanganan outlier
    df = pd.DataFrame({
        'TotalCharges': [100.0, 150.0, 200.0, 220.0, 180.0, 190.0, 5000.0, -100.0]
    })

q1 = df['TotalCharges'].quantile(0.25)
q3 = df['TotalCharges'].quantile(0.75)
iqr = q3 - q1

maximum = q3 + (1.5 * iqr)
minimum = q1 - (1.5 * iqr)

# Imputasi / winsorization: batasi nilai ekstrem ke threshold minimum dan maksimum
df['TotalCharges'] = df['TotalCharges'].clip(lower=minimum, upper=maximum)

print(f"Batas minimum: {minimum:.2f}")
print(f"Batas maksimum: {maximum:.2f}")
print("Data setelah imputasi outlier:")
print(df['TotalCharges'])