
# coding: utf-8

# In[ ]:

#1d
import numpy as np
import matplotlib.pyplot as plt
from math import sin, e

t= np.linspace(0,24,100)
y= (e**(-0.1*t))*np.sin(2*t)

plt.plot(t,y, color='y', linestyle='--', label='h(t)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej1d.png')
plt.show()#Luis Manuel Garcia Valdivia

