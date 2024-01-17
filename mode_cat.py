# Mode : mencari nilai yang paling sering muncul dari suatu deret bilangan, nilai diurutkan terlebih dahulu secara ascending

import numpy as np
from scipy import stats
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print("Nilai mode:", mode_jumlah_kucing)