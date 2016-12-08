
# coding: utf-8

# In[ ]:

#3c
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
t= np.linspace(-2*pi,2*pi)
x= np.sin(3*t) 

t= np.linspace(0,2*pi)
y= np.sin(4*t)

plt.plot(t,x, color='r', linestyle='--', label='x', linewidth=4)
plt.plot(t,y, color='g', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej3c.png')
plt.show()

#Luis Manuel Garcia Valdivia