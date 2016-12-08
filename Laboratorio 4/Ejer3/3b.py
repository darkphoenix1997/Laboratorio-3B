
# coding: utf-8

# In[ ]:

#3b
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
t= np.linspace(-2*pi,2*pi)
x= t+2*np.sin(2*t) 

t= np.linspace(-2*pi,2*pi)
y= t+2*np.cos(5*t)

plt.plot(t,x, color='r', linestyle='--', label='x', linewidth=4)
plt.plot(t,y, color='b', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej3b.png')
plt.show()

#Luis Manuel Garcia Valdivia