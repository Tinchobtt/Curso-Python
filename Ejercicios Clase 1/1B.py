import pandas as pd

df = pd.read_excel('Tabla1.xlsx')
print(df)
equipos = df.to_dict("list")

ganador = max(equipos['Puntos'])
equipos = df.to_dict("records")

for equipo in equipos:
    if equipo['Puntos'] == ganador:
        print('El ganador es el', equipo['Equipo'])

