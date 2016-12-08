
# coding: utf-8

# In[ ]:

#2a
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
x= np.linspace(0,4*pi,100)
y= np.cos(2*x)+np.sin(3*x)

w= np.linspace(0,4*pi,100)
z= -2*np.sin(2*x)+3*np.cos(3*x)

plt.plot(x,y, color='y', linestyle='--', label='s(x)', linewidth=4)
plt.plot(w,z, color='b', linestyle='--', label='v(x)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej2a.png')
plt.show()

#Luis Manuel Garcia Valdivia