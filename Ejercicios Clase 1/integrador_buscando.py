import pandas as pd
import numpy as np

archivo = pd.read_excel('excels/california_housing_train.xlsx')

paso = .5
lats = np.arange(32.5, 42.5, paso) #[32.5, 33.,  33.5, 34.,  34.5, 35.,  35.5, 36.,  36.5, 37.,  37.5, 38.,  38.5, 39., 39.5, 40.,  40.5, 41.,  41.5, 42.]
lons = np.arange(-124.3, -114.3, paso) #[-124.3, -123.8, -123.3, -122.8, -122.3, -121.8, -121.3, -120.8, -120.3, -119.,8 -119.3, -118.8, -118.3, -117.8, -117.3, -116.8, -116.3, -115.8, -115.3, -114.8]
maximoValor = 0
maximaLat = 0
maximaLon = 0

for lat in lats:
    for lon in lons:
        data = archivo[(archivo['latitude']>=lat) & (archivo['latitude']<=lat+paso)]
        data = data[(data['longitude']>=lon) & (data['longitude']<=lon+paso)]
        if(len(data)>100): #menos de 100 filas
            m = np.mean(data['median_house_value'])
            if m > maximoValor:
                maximaLat = lat
                maximaLon = lon
                maximoValor = m
                
print('Latitude:',maximaLat,'Longitude',maximaLon,'Price',maximoValor)