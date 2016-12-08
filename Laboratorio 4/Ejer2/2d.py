
# coding: utf-8

# In[ ]:

#2d
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
t= np.linspace(0,2*pi,100)

x= (1+2*np.sin(t))*np.cos(t)
plt.plot(t,x, color='y', linestyle='--', label='x(t)', linewidth=4)

y= (1+2*np.sin(t))*np.sin(t)
plt.plot(t,y, color='b', linestyle='--', label='y(t)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej2d.png')
plt.show()#Luis Manuel Garcia Valdivia

