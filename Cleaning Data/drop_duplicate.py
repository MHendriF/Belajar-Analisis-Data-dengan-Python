# Drop Duplicates: menghapus baris duplikat dalam DataFrame

import os
import pandas as pd

file_path = "data.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame({
        'customer_id': [101, 102, 102, 103, 104, 101],
        'product': ['Shirt', 'Shoes', 'Shoes', 'Hat', 'Pants', 'Shirt']
    })

print("Data awal:")
print(df)

# Menghapus duplikat
clean_df = df.drop_duplicates().reset_index(drop=True)

print(f"\nJumlah baris awal: {len(df)}")
print(f"Jumlah baris setelah drop_duplicates: {len(clean_df)}")
print("Data setelah pembersihan duplikat:")
print(clean_df)