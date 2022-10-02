import pandas as pd

usuarios_archivo = pd.read_excel('excels/Finanzas.xlsx', index_col='Usuario')
print('Usuarios:\n',usuarios_archivo,'\n')

usuarios = usuarios_archivo.to_dict("index") #Diccionario de diccionarios con el index de key

transferencia_archivo = pd.read_excel('excels/Finanzas.xlsx', 'Transferencias')
transferencias = transferencia_archivo.to_dict('records') #Una lista con un diccionario por cada fila
print(transferencias)

for transferencia in transferencias:
    emisor = transferencia['Emisor']
    receptor = transferencia['Receptor']
    monto = transferencia['Monto']

    usuarios[emisor]['Presupuesto'] -= monto
    usuarios[receptor]['Presupuesto'] += monto

print(usuarios)
#Creo el DataFrame
usuarios_actualizados = pd.DataFrame.from_dict(usuarios, orient='index')

print("Usuarios luego de realizar las transferencias:")
print(usuarios_actualizados)

#grabo info
usuarios_actualizados.to_excel("excels/usuarios_actualizados.xlsx")