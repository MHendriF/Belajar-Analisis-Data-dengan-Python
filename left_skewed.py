# Right-skewed distribution merupakan distribusi data yang memiliki sebagian besar populasi data yang terkonsentrasi pada bagian kiri. Distribusi data ini memiliki nilai mean lebih besar dari nilai median dan juga mode.
# Left-skewed distribution merupakan distribusi data yang terjadi ketika sebagian besar populasi data berada pada bagian kanan. Umumnya distribusi ini memiliki nilai median dan mode yang lebih besar dari nilai mean.

import numpy as np
import pandas as pd
    
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
nilai_skewness = jumlah_kucing_series.skew()
print("Nilai skewness:", nilai_skewness)