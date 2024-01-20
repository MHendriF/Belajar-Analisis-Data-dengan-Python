import matplotlib.pyplot as plt
    
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
            'Surakarta','Surabaya', 'Medan', 'Makassar')
    
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
                3481, 287750, 785409)
    
plt.bar(x=cities, height=populations)
plt.show()