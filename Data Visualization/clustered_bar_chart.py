import seaborn as sns
import matplotlib.pyplot as plt
    
penguins = sns.load_dataset("penguins")
    
sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)
plt.show()