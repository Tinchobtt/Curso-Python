#%% NUMPY ARANGE Y LINSPACE
import numpy as np

x = np.arange(0, 1, .1) # inicio, fin, salto
y = np.linspace(0, 1, 5) # inicio, fin, cantidad (incluye el segundo paramentro)
print(x)
print(y)

#%% MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*3.14, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'b-', label='Seno')    # graficamos función y1
plt.plot(x, y2, 'r-.', label='Coseno') # graficamos función y2
plt.legend() # Le decimos a maplotlib que muestre todos los labels
plt.show()
#%% DOS GRAFICOS EN UNO
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*3.14, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)   # 2 filas, 1 columna, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(2, 1, 2)   # 2 filas, 1 columna, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('Ejemplo 1:\n')
plt.show()

# Una vez que usamos plt.show() el gráfico se muestra y podemos crear uno nuevo:

plt.subplot(1, 2, 1)   # 1 fila, 2 columnas, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(1, 2, 2)   # 1 fila, 2 columnas, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('\nEjemplo 2:\n')
plt.show()

#%% CARTELES
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*3.14, 0.3)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12,4)) #Configuracion del tamaño del grafico (pulgadas)

plt.subplot(1,2,1)
plt.title('Grafico Azul')
plt.plot(x, y1, 'bo')
plt.xlabel('Tiempo')
plt.ylabel('Corriente')

plt.subplot(1,2,2)
plt.title('Grafico Rojo')
plt.plot(x, y2, 'r-.')
plt.xlabel('Tiempo')
plt.ylabel('Corriente')
plt.axis([0, 3, -1, 1]) #Elegis los limites de los ejes ([X , Y] --> [(de 0 a 3 en X), (de -1 a 1 en Y)])
plt.grid('True')

plt.show()

#%% TORTA
import matplotlib.pyplot as plt

sizes = [215, 130, 245, 210, 120, 45] # Porcentaje de tamaños
e = (0.2, 0, 0, 0, 0, 0) # Separacion de la porcion
l = ('Python', 'Java', 'Javascript', 'PHP', 'C#', 'Ruby')
colors = ['#47f', '#f22', '#ec2', '#02f', '#b1f', '#f24']
plt.pie(sizes, explode = e, labels=l, colors=colors, autopct='%5.01f%%', startangle=90)
plt.show()

#%% TORTA MEJORADO
import matplotlib.pyplot as plt

# Pie chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

e = (0,0.1,0,0) 

fig1, ax1 = plt.subplots()

patches, texts, autotexts = ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, explode=e)

for text in texts:
    text.set_color('grey')

for autotext in autotexts:
    autotext.set_color('grey')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()

#%% MAS TORTA
import matplotlib.pyplot as plt
 
# Data to plot
labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [504, 337, 415, 280]
colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff']

labels_gender = ['Man','Woman','Man','Woman','Man','Woman','Man','Woman']
sizes_gender = [315,189,125,212,270,145,190,90]
colors_gender = ['#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
 
# Plot
plt.pie(sizes, labels=labels, colors=colors, startangle=90)

plt.pie(sizes_gender,colors=colors_gender,radius=0.75,startangle=90)

centre_circle = plt.Circle((0,0),0.5,color='black', fc='white',linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 
plt.axis('equal')
plt.tight_layout()
plt.show()