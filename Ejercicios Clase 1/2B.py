import pandas as pd

def promedio(df, id):
    alumno = df.loc[id]
    prom = (alumno['Quimica'] + alumno['Matematica'] + alumno['Fisica']) / 3
    return prom


alumnos = pd.read_excel('Datos.xlsx')
indice = int(input('Ingrese el indice del alumno requerido: '))

print('Promedio:',promedio(alumnos, indice))