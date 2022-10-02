from matplotlib import pyplot as plt
import numpy as np
import math

#PARTE 1
x = np.linspace(-1,1,10)
y = np.absolute(x)
plt.plot(x,y)
plt.show()

#PARTE 1

def f(x):
    e = np.exp(1)
    return e**((-x**2)/2)

x1 = np.linspace(-5,5,11)
y1 = f(x1)
plt.plot(x1,y1)
plt.show()
