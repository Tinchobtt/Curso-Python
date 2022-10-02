from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

archivo = pd.read_csv('excels/BTC.csv')
valores = archivo.to_dict('list')

y = valores['Open']
x = valores['Date']

maxOpen = max(y)
maxDay = archivo[ archivo['Open'] == maxOpen]
maxDay = maxDay['Date']

plt.figure(figsize=(12,4))
plt.title('Bitcoin en los ultimos 10 años')
plt.plot(x, y, 'r-', label='Open')
plt.plot(maxDay, maxOpen, 'bo', label='maximo')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.show()



