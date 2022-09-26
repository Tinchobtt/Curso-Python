import pandas as pd
import os

def copia(archivo):
    df = pd.read_excel(archivo)

    i = 1
    name = 'Copia ' + str(i) + ' - ' + archivo
    while os.path.exists(name) == True:
        name = 'Copia ' + str(i + 1) + ' - ' + archivo
        i += 1
    
    df.to_excel(name)

copia('Datos.xlsx')
