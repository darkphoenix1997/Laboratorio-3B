
# coding: utf-8

# In[ ]:

#1b
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-1,5,100)
y= 2*(x**2)-(8*x)-11

plt.plot(x,y, marker= 'x' ,color='k', linestyle='--', label='f(x)', linewidth=4)

plt.legend(loc="upper left")
plt.title('Graficando con python')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.savefig('Ej1b.png')
plt.show()#Luis Manuel Garcia Valdivia

