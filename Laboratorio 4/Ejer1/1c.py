
# coding: utf-8

# In[ ]:

#1c
import numpy as np
import matplotlib.pyplot as plt
from math import e

t= np.linspace(-1,5,100)
y= t*e**-2*t

plt.plot(t,y, color='r', linestyle='--', label='f(t)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej1c.png')
plt.show()
#Luis Manuel Garcia Valdivia
