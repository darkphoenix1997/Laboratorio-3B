import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, e
x= np.linspace(0,2,100)
y= x*e**(-3*x)

w= np.linspace(0,2,100)
z= e**(-3*x)*(1-3*x) 

plt.plot(x,y, color='r', linestyle='--', label='f(x)', linewidth=4)
plt.plot(w,z, color='b', linestyle='--', label='g(x)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('Ej2b.png')
plt.show()#Luis Manuel Garcia Valdivia

