import pandas as pd
import numpy as np

archivo = pd.read_csv('recorridos-realizados-2021-sample.csv')

todos = len(archivo)
estado_noraml = sum(archivo['Estado cerrado'] == 'NORMAL')
porcentaje = round(estado_noraml * 100 / todos ,2)
print(f'El {porcentaje}% de los viajes fueron completados en estado NORMAL')

duracion = round(archivo['Duración'].mean())
print(f'La duracion promedio de los viajes es de {duracion//60} minutos {duracion % 60} segundos')

horarios_inicio = archivo['Fecha de inicio']
horarios_inicio = pd.to_datetime(horarios_inicio)
horas_inicio = horarios_inicio.dt.hour
hora_pico = horas_inicio.value_counts().idxmax()
print(f'La hora más concurrida es de {hora_pico}hs a {hora_pico+1}hs')

estaciones_inicio = archivo['Nombre de estación de inicio']
estaciones_fin = archivo['Nombre de estación de fin de viaje']
estaciones = pd.concat([estaciones_inicio, estaciones_fin])
print(f'Hay {len(estaciones.value_counts())} estaciones en total')

print('\nCantidad de viajes iniciados en cada estación:\n')
for estacion, cantidad in estaciones_inicio.value_counts().iteritems():
  print('Cantidad:', cantidad, ' Estación:', estacion)