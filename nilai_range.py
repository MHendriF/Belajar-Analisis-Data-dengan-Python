# Range : mencari selisih antara bilangan terbesar dengan bilangan terkecil dari suatu deret bilangan

import numpy as np

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
range_nilai = jumlah_kucing.max() - jumlah_kucing.min()
print("Nilai range:", range_nilai)