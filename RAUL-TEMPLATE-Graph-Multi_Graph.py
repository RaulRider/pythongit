# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:50:43 2016

@author: rrferrero
"""

import matplotlib.pyplot as plt
import numpy as np


############ FIGURE 1
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
plt.title('Easy as 1, 2, 3') # subplot 211 title

plt.subplot(212)             # the second subplot in the first figure
plt.plot([1, 2, 3], label='line 1', marker = 'o', linewidth = 2)
plt.yscale('linear') # Options: linear, log, symlog, logit
plt.title('Easy as 1, 2, 3')
plt.legend() # To show the labels


############ FIGURE 2
plt.figure(2)                # a second figure
datos = np.random.random((20,20)) 
plt.imshow(datos, cmap=plt.cm.jet, interpolation='nearest')
# plt.imshow(datos) creates a subplot(111) by default


############ back to FIGURE 1
plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current

plt.show()
