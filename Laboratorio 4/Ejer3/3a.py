import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
t= np.linspace(0,2*pi)
x= (np.cos(t))**3 

y= (np.sin(t))**3 

plt.plot(t,x, color='r', linestyle='--', label='x', linewidth=4)
plt.plot(t,y, color='k', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej3a.png')
plt.show()
#Luis Manuel Garcia Valdivia