
# coding: utf-8

# In[ ]:
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
t= np.linspace(0,4*pi,100)
y= (np.sin(3*t))*(np.cos(2*t))

z= .5*np.cos(t)+(5/2)*np.cos(5*t)

plt.plot(t,y, color='y', linestyle='--', label='f(t)', linewidth=4)
plt.plot(t,z, color='r', linestyle='--', label='g(t)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej2c.png')
plt.show()#Luis Manuel Garcia Valdivia

