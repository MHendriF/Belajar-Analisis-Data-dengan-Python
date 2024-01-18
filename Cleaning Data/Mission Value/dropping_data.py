# Dropping : menghapus seluruh baris atau kolom yang memiliki missing value

import pandas as pd
    
products_df = pd.read_csv("product.csv")
    
products_df.dropna(axis=0, inplace=True)