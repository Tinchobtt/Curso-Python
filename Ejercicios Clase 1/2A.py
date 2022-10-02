import pandas as pd

df = pd.read_excel('Datos.xlsx')

sumQuim = sum(df['Quimica'])
prom = sumQuim / len(df['Quimica'])
print(prom)
