# Median : mencari nilai yang selisih antara bilangan terbesar dengan bilangan terkecil dari suatu deret bilangan

import numpy as np
    
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
range = jumlah_kucing.max() - jumlah_kucing.min()
print("Nilai range:", range)