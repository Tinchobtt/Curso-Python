#%% 2
import pandas as pd

data = {
    'Cursada': [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9],
    'Final':   [1,2,5,6,8,3,4,5,6,8,9,9,8,7,6,5,6,7,4,3,5,6,7,8,6,2,1]
}

df = pd.DataFrame(data)
print(df)

print(df.sort_values(by = ['Final','Cursada'], ascending=[False, True]))

#%% 3
import pandas as pd

tabla = pd.read_excel('excels/Datos.xlsx', index_col='Apellido')
dataFrame = tabla.to_dict('index')
print(dataFrame)
print(dataFrame['Martinez']['Matematica'])

#%% 4
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [4,3,2,1,0,0,1,2,3,4]

plt.subplot(2,3,4)
plt.plot(x,y, 'ko', label = 'Amplitud')
plt.legend()
plt.grid()
#plt.savefig('Plot.png', dpi = 300)
plt.subplot(2,3,6)
plt.plot(y,x)

#plt.show()

#%% 5
import matplotlib.pyplot as plt

notas = [10,9,7,4,0,0,1,1,1,3,3,4,4,5,5,6,7,7,8,8,9,9,0,0,2,2,2,2,2,1,1,1,1,1,1,6,7,8,4,6,3,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,2,9,8,7,9,8,7,8,4,6,3,2,9,8,7,9,8,7,8,4,6,3,2,9,8,7,9,8,7,8,4,6,3,2,9,8,7,9,8,7,8,4,6,3,2,9,8,7,9,8,7,9,8,3,2,1,3]

plt.hist(notas, range(12), align = 'mid', rwidth=0.75)
plt.legend()
plt.grid()
#plt.show()

#%% 6
import pandas as pd

data = pd.read_excel('Libro1.xlsx')
errores = data['Difrencia de Gol'] != (data['Goles convertidos'] - data['Goles recibidos'])
#print(data['Error'].mask(errores,'Si'))

#%% 7
import pandas as pd

data = pd.read_excel('Libro1.xlsx', index_col='Equipo')
df = data.to_dict('index')
print(df)
print(data.idxmax()['Goles Recibidos'])