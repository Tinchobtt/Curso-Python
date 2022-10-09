#%% 1
import matplotlib.pyplot as plt

p0 = [-1,0]
p1 = [0,1]
p2 = [1,0]
p3 = [0,-1]
p4 = [-1,-1]
p5 = [0,0]
p6 =[1,1]


points = [p4, p3, p5, p1, p6, p2, p0, p4]

xCoord = []
yCoord = []

for i in range(len(points)):
    xCoord.append(points[i][0])
    yCoord.append(points[i][1])

plt.plot(xCoord, yCoord)
plt.plot(xCoord, yCoord, 'ro')
#plt.show()

#%% 2
import pandas as pd

tabla = pd.read_excel('Libro2.xlsx')
print(tabla)
tabla = tabla.dropna(subset=["Puntaje", "Diferencia de Gol"])
print(tabla)

#%% 3
import matplotlib.pyplot as plt

x = [3,4,6,6,4,6,8,9,3,2,7,5]
y = [0,1,2,3,4,5,6,7,8,9,10,11]

plt.plot(x,y, 'k.')
plt.grid()
#plt.show()

#%% 4
import matplotlib.pyplot as plt

plt.subplot(2, 3, 2)

#%%  5
# value_counts().idxmax()

#%% 6 
import pandas as pd

data = pd.read_excel('Libro1.xlsx')
errores = data['Diferencia de Gol'] != (data['Goles convertidos'] - data['Goles recibidos'])
print(data['Error'].mask(errores,'Si'))

#%% 7
# Error de matplolib del parametro de plot() del color y linea

#%% 8
import pandas as pd
import numpy as np

table = np.array([[4,6,5],[8,8,8],[5,7,8]])
df = pd.DataFrame(table, columns=['Matemática', 'Física', 'Química'])

df2 = pd.DataFrame(df, columns=['Química', 'Matemática'])
df2.to_excel('Alumnos.xlsx')
#%% 9
# Seleccion con pandas de un DataFrame

#%% 10
import matplotlib.pyplot as plt

y = [0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

plt.hist(y, range(1,7), align='left', rwidth=0.5, color='orchid')
plt.show()