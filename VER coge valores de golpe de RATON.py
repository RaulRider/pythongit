# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:51:11 2016
RAUL RUIZ FERRERO
@author: raul
"""
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    (event.button, event.x, event.y, event.xdata, event.ydata))

cid = fig.canvas.mpl_connect('button_press_event', onclick)


