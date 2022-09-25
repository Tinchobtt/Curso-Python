import pandas as pd

df = pd.read_excel('Tabla1.xlsx')
print(df)
equipos = df.to_dict("records") 

for equipo in equipos:
    dif = equipo['Goles a favor'] - equipo['Goles en contra']
    print(f'Diferencia {equipo["Equipo"]}:',dif)
    

