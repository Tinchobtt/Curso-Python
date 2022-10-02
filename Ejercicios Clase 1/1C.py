import pandas as pd

df = pd.read_excel('excels/Tabla1.xlsx')
print(df)
equipos = df.to_dict('records')

lista = []

for equipo in equipos:
    if equipo['Puntos'] > 20:
        lista.append(equipo['Equipo'])

if lista != []:
    print('Equipos que tuvieron mas de 20 puntos:',lista)
else:
    print('Ningun Equipo tuvo mas de 20 puntos')

print(df.sort_values(by = 'Puntos', ascending=False))


