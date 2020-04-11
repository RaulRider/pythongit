# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:05:44 2016

@author: raul
"""

import cmath 
import sys
import numpy as np
import matplotlib.pyplot as plt


# esta es una curva
# linspace define el rango
maximo_x = cmath.pi * 2
xa = np.linspace(- maximo_x, maximo_x, 100)
ya = np.sin(xa)
y1 = xa
y2 = y1 - (xa ** 3) / np.math.factorial(3)
y3 = y2 + (xa ** 5) / np.math.factorial(5)
y4 = y3 - (xa ** 7) / np.math.factorial(7)
y5 = y4 + (xa ** 9) / np.math.factorial(9)

# Para definir una funcion en un RANGO
# x = np.arange(0, 5, 1);
# y = 2 * x

print(sys.version)
print(cmath.e)
print(cmath.pi)

# Imprimir los puntos de para evr si funciona
print('Puntos')
for i in range(len(xa)):
    print('{:05.3f}'.format(xa[i]) , 
          '{:05.3f}'.format(ya[i]) ,
          '{:05.3f}'.format(y1[i]) ,
          '{:05.3f}'.format(y2[i]) ,
          '{:05.3f}'.format(y3[i]) ,
          '{:05.3f}'.format(y4[i]) )
 

# PARAMETROS DEL GRAFICO
# Para rellenar el area: plt.fill(x, y, 'r')
# plt.xlim(xmin = -cuadro, xmax = cuadro)
# plt.ylim(ymin = -cuadro, ymax = cuadro)

plt.xlim(xmin = - maximo_x * 2, xmax = maximo_x * 2)
plt.ylim(ymin = -2, ymax = 2)
plt.xlabel('Eje x : valor x')
plt.ylabel('Eje y : valores de Funcion y Serie de Taylor')
plt.title('Series de Taylor')
plt.grid(True)


plt.plot(xa,ya, 'ro')
plt.plot(xa,y1)
plt.plot(xa,y2)
plt.plot(xa,y3)
plt.plot(xa,y4)
plt.plot(xa,y5)

plt.savefig('Raul_Grafico_output_file.png') #Para sacar grafico a fichero

plt.show()