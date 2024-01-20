import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
    
x = np.random.normal(15, 5, 250)
sns.boxplot(x)
plt.show()