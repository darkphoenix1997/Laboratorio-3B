import numpy as np
import matplotlib.pyplot as plt
from math import  pi, sin, cos
i= np.linspace(0,4*pi,)

r= 105+100*(np.sin(4.5*i))
l= i-((np.cos(10*i)/10))

x= 320+(r*np.cos(l))
y= -240-(r*np.sin(l))

plt.plot(i,x, color='b', linestyle='--', label='x', linewidth=4)
plt.plot(i,y, color='k', linestyle='--', label='y', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej7.png')
plt.show()
#Luis Manuel Garcia Valdivia