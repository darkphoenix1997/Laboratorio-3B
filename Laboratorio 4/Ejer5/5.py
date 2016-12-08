
# coding: utf-8

# In[ ]:

#5
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, sqrt
l= np.linspace(0,2*pi) 
r= 2-2*np.sin(l)+np.sin(l)*np.sqrt(np.cos(l)/np.sin(l)+1.4) 

x= r*np.cos(l) 

y= r*np.sin(l)

plt.plot(l,x, color='r', linestyle='--', label='x', linewidth=4)
plt.plot(l,y, color='g', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej5.png')
plt.show()#Luis Manuel Garcia Valdivia

