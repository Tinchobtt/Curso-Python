import pandas as pd

listas = ['excels/lista1.csv', 'excels/lista2.csv']

clientes = dict() 

for lista in listas: # iteramos todas las bases de datos 
    archivo = pd.read_csv(lista, index_col =["Mail"])
    data = archivo.to_dict("index") 
    
    print("Base de datos", lista)
    print(archivo)

    for mail in data: 
        if mail not in clientes: 
            clientes[mail] = dict() 

        campos = data[mail] #fila

        for campo in campos:
            clientes[mail][campo] = data[mail][campo]

df = pd.DataFrame.from_dict(clientes, orient='index')

print("Base de datos unificada")
print(df)