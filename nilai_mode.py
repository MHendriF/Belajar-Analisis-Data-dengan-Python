# Mode : mencari nilai yang paling sering muncul dari suatu deret bilangan

import numpy as np
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
mode_result = stats.mode(jumlah_kucing)
mode_jumlah_kucing = int(np.asarray(mode_result.mode).ravel()[0])
print("Nilai mode:", mode_jumlah_kucing)