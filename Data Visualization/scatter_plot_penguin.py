import matplotlib.pyplot as plt
import seaborn as sns
    
penguins = sns.load_dataset("penguins")
    
sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species", style="species")
plt.show()