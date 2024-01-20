import matplotlib.pyplot as plt
    
flavors = ('Chocolate', 'Vanilla', 'Macha', 'Others')
votes = (50, 20, 30, 10)
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.1, 0, 0, 0)
    
plt.pie(
    x=votes,
    labels=flavors,
    colors=colors,
    autopct='%1.1f%%',
    wedgeprops = {'width': 0.4}
)
plt.show()