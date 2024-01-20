import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(15, 5, 250)

sns.histplot(x=x, bins=15, kde=True)
plt.show()