import matplotlib.pyplot as plt
import numpy as np
    
x = np.random.normal(15, 5, 250)
    
plt.hist(x=x, bins=15)
plt.show()