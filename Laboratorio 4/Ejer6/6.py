
# coding: utf-8

# In[ ]:import numpy as np
import matplotlib.pyplot as plt
from math import  pi, sin, cos

i= np.linspace(0,2*pi)
r= -250*(np.sin(5*i))*(np.cos(4*i))
l= i+np.sin(r/100)

x= 320+(r*np.cos(l))
y= -240-(r*np.sin(l))

plt.plot(i,x, color='b', linestyle='--', label='x', linewidth=4)
plt.plot(i,y, color='g', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('Ej6.png')
plt.show()
#Luis Manuel Garcia Valdivia

