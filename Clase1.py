#%% Descargador de archivos
import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista_final.csv")
#%% LEECTURA DE ARCHIVOS
import pandas as pd

#Leemos el archivo xlsx 
archivo = pd.read_excel('excels/Datos.xlsx')
print(archivo,'\n')
print(archivo.loc[0]) #loc me devuelve una fila

#to_dict('list') te devuelve un diccionario con las columnas encerradas en listas
data = archivo.to_dict('list')
print(data)
print(data['Nombre']) #Me devuelve una columna
print(data['Nombre'][1],'\n') #Me devuelve el segundo item de la columna/lista nombres

# "records" significa que vamos a obtener el contenido separado por cada fila en una lista de diccionarios
data = archivo.to_dict("records") 
print(data)
print(data[2])            # Accedemos a los datos de una fila
print(data[2]['Nombre'],'\n')  # Accedemos a la columna 'Nombres' de la fila con índice 2

# Indicamos que la columna de indexación será apellido.
archivo = pd.read_excel("excels/Datos.xlsx", index_col ="Apellido") 
print(archivo,'\n')

data = archivo.to_dict("index") #index nos devuelve un diccionario de diccionarios en el que cada uno tiene como palabre clave el apellido
print(data,'\n')

print(data)
print(data['Martinez'])                # Accedemos a los datos de una fila (usando el dato de índice apropiado)
print(data['Martinez']['Legajo'],'\n') # Accedemos a la columna 'Legajo' de la fila con índice 'Martinez'

#%%ESCRITURA DE ARCHIVOS
import pandas as pd

data = {
    "Personas" : ["Analía Ferreyra" , "Martin Hugo", "Fernando Lorenzo"],
    "Edad" : [25, 35, 87] 
}
df = pd.DataFrame(data) #Crea un dataframe con los datos del diccionario
print(df,'\n')

#%%
import pandas as pd
df.to_excel('excels/personas.xlsx') #Crea un archivo excel si no existe y sino lo sobrescribe

datos = pd.read_excel("excels/Datos.xlsx") 
print(datos,'\n')

print(datos['Quimica']) #Accedemos a la columna 'Quimica'
alumno = datos.loc[0]   #Accedemos a la fila deseada
print(alumno)
print(alumno['Matematica']) #Accedemos a la fila y columna deseada

#%% SELECCIONAR CIERTAS PARTES DE DF
import pandas as pd

datos = pd.read_excel("excels/Datos.xlsx") 
print("Datos:\n")
print(datos)

# No es necesario usar paréntesis si hay una única condición
aprobados = datos[ datos['Quimica'] >= 4 ] 
print("\nAprobados en Química:\n")
print(aprobados)

#%% SELECCIONAR CIERTAS PARTES DE DF
import pandas as pd

datos2 = pd.read_excel("excels/Datos2.xlsx") 
print("Datos:\n")
print(datos2,'\n')

datos2_matematica = datos2[ (datos2['Matematica'].notna()) & (datos2['Matematica'] != 'A')  ]
print(datos2_matematica)

datos2_matematica = datos2_matematica['Matematica'] # Nos quedamos con la columna de interés

print('Notas válidas en Matemática: ')
print(datos2_matematica)