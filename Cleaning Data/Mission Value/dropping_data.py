# Dropping: menghapus seluruh baris atau kolom yang memiliki missing value

import os
import pandas as pd

file_path = "product.csv"
if os.path.exists(file_path):
    products_df = pd.read_csv(file_path)
else:
    products_df = pd.DataFrame({
        'product_id': [1, 2, 3, 4],
        'price': [100.0, None, 150.0, 200.0],
        'category': ['A', 'B', None, 'A']
    })

print("Data awal:")
print(products_df)

# Menghapus baris yang mengandung missing value (NaN)
clean_products_df = products_df.dropna(axis=0)
print("\nData setelah dropna:")
print(clean_products_df)