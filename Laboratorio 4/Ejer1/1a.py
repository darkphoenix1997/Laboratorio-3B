
# coding: utf-8

# In[ ]:

#1a
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-6,2,100)
y= 5-(4*x)-(x**2)

plt.plot(x,y, marker='x' ,color='r', linestyle='--', label='f(x)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej1a.png')
plt.show()
#Luis Manuel Garcia Valdivia

