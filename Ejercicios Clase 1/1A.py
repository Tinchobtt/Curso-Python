import pandas as pd

archivo = pd.read_excel('excels/Tabla1.xlsx')
print(archivo)
equipos = archivo.to_dict("records") 
print(equipos)

for equipo in equipos:
    dif = equipo['Goles a favor'] - equipo['Goles en contra']
    print(f'Diferencia {equipo["Equipo"]}:',dif)
    
   