import pandas as pd

data = pd.read_excel('Datos.xlsx')
print(data)

aprobados_mat = data[ data['Matematica'] >= 6 ]
print(aprobados_mat)