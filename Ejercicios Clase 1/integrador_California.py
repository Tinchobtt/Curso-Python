import pandas as pd
import numpy as np

archivo = pd.read_excel('california_housing_train.xlsx')

filtro = archivo[ (archivo['longitude'] >= -120) & (archivo['longitude'] <= -118) & (archivo['median_house_value'] > 80000)]
casas = len(filtro)
print('\nHay',casas,'casas con median_value mayor a 80.000, entre las longitudes -120 y -118\n')

habitaciones = sum( filtro['total_rooms'] )
print('Promedio:', habitaciones/casas,'\n')

mas_cara = archivo['median_house_value'].max()
cantidad = sum(archivo['median_house_value'] == mas_cara)
print(f'La casa mas cara cuesta: ${mas_cara}\nY hay {cantidad} casas con ese precio\n')

media = np.mean(archivo['median_house_value'])
varianza = np.var(archivo['median_house_value'])
print(f'La media de la propiedad "media_house_value" es de {media}, y la varianza es de {varianza}')

 