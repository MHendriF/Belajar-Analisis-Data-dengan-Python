# Imputation: mengisi (fill) missing value dengan nilai tertentu (misal: mean)

import os
import pandas as pd

file_path = "employee_data.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25.0, None, 30.0, 35.0, None]
    })

print("Data awal:")
print(data)

# Mengisi missing value pada kolom age dengan nilai rata-rata (mean)
mean_age = data['age'].mean()
data['age'] = data['age'].fillna(mean_age)

print(f"\nNilai mean age: {mean_age:.1f}")
print("Data setelah imputasi missing value:")
print(data)