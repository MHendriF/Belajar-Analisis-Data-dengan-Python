import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
            'Surakarta','Surabaya', 'Medan', 'Makassar')
    
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
                3481, 287750, 785409)
        
df = pd.DataFrame({
    'Cities': cities,
    'Population': populations,
})

# Sort value
df.sort_values(by='Population', inplace=True)

sns.barplot(y=df["Cities"], x=df["Population"], orient="h", color='blue')
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()