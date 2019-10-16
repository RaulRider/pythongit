# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
import matplotlib
# matplotlib.use('PDF')   # generate PDF output by default
# esto hay que hacerlo antes de llamar a matplotlib.pyplot

import matplotlib.pyplot as plt
# matplotlib.pyplot.ion()   # Turn interactive mode on.
# matplotlib.pyplot.ioff()  # Turn interactive mode off.
# matplotlib.pyplot.isinteractive() # Return status of interactive mode.
print('- Modo interactivo :', matplotlib.pyplot.isinteractive())

import os
my_path = os.path.abspath(__file__) 
print('- Directorio de uso:', my_path)




# definicion de la función a dibjuar
dim = 20
datos = np.random.random((dim,dim)) 
print(datos)
datos = datos * 2
# Fin

figura1 = plt.figure(1) # se define un grafico por si hay varios

# figura1.savefig(my_path + '/Sub_Directory/graph.png')
plt.xlabel('time')          
plt.ylabel('volts')        
plt.title('A simple plot from RAUL')   

plt.imshow(datos) # grafico a mostrar

figura1.savefig('Grafico_Raul_1')
plt.show() #should be the last line of your script




