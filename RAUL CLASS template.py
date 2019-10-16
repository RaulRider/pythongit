#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:05:43 2016

@author: raul
"""
''' Print option
np.set_printoptions(precision=3, suppress=True) 
para floating variables, suppress = to eliminate scientific notation
'''

#import numpy as np
import matplotlib.pyplot as plt

class numero: # use like this var = numero()
    variable_class = 1   # class variable shared by all instances

    def __init__(self, targetnumber = 100):
        """A simple example class to start with prime number"""
        self.targetnumber = targetnumber
        self.root = targetnumber ** .5
        self.root_int = round(self.root)
        self.curve_x = [self.root_int]
        self.curve_y = [self.targetnumber % self.root_int]
        self.test_x, self.test_y = [],[]
        self.p1, self.p2 = 0,0
        self.min = 0
        #self.max_upx, self.max_upy = 0 , 0
        #self.max_dwx, self.max_dwy = 0 , 0
        self.isprime = False # instance variable unique to each instance
        
        
    def add_data(self, value):  # a fuction in a class is a METHOD
        self.data.append(value) # por ejempplo num.add_data(100)
    
    def get_curve(self, span = 10): #METHOD to get the points of the parabolic
        self.min = self.targetnumber % self.root_int
        for i in range(-span,span):
            point = self.root_int + i
            self.test_x.append(point)
            self.test_y.append(self.targetnumber % point)
                               
        for i in range(1,span): # load curve_xy points 0 to span
            self.curve_x.append(self.root_int + i)
            self.curve_y.append(self.targetnumber % (self.root_int + i))
            if self.curve_y[i-1] >= self.curve_y[i]:
                #max_up = True
                self.max_upx = self.curve_x[i-1]
                self.max_upy = self.curve_y[i-1]
                break

        for i in range(1,span): # load curve_xy points 0 to (-)span
            self.curve_x = [self.root_int - i] + self.curve_x
            self.curve_y = [ (self.targetnumber % (self.root_int - i) )] + self.curve_y
            if self.curve_y[0] < self.curve_y[1]:
                #max_dw = True
                self.max_dwx = self.curve_x[1]
                self.max_dwy = self.curve_y[1]
                break

        # Eliminate the extrems if they are not the max value
        count = len(self.curve_x)
        if ( self.curve_y[count-1] < self.curve_y[count-2] ):
            self.curve_y.pop()
            self.curve_x.pop()
        if ( self.curve_y[0] <self.curve_y[1] ):
            self.curve_y.pop(0)
            self.curve_x.pop(0)
            


list_of_primes = [31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
curves = []

def get_all_curves(new_curves = [], 
                   start = 31, 
                   multiplicators = [31,37,41,43,47],
                   span = 30):            
        for i in range( 0 , len( multiplicators ) ):
            new_curves.append( numero(start * multiplicators[i]) )
            new_curves[i].get_curve(span)
            new_curves[i].p1 = start
            new_curves[i].p2 = multiplicators[i]
        return new_curves
        
######### START
curves = get_all_curves()
for i in range( 0 , len( curves ) ):
    # draw the minimum curves NOTE: including the factorizing P1 & P2
    plt.plot([curves[i].p1] + curves[i].curve_x + [curves[i].p2],
             [0] + curves[i].curve_y +[0], 
             label='Curve {0} x {1} : {2} ({3} pt)'.format( curves[i].p1 , 
                                                curves[i].p2, 
                                                curves[i].targetnumber, len(curves[i].curve_x)),
             marker='o', linewidth = 1)
    #include center axis for each curve
    #plt.plot([curves[i].root_int , curves[i].root_int], [0 , 30])
    
    # include boex with minimum points
    plt.text(curves[i].root_int , curves[i].min + 1, 
             'min : {0},{1}'.format( curves[i].root_int , curves[i].min ) , 
             style='italic', fontsize = 9,
             bbox={'facecolor':'white', 'alpha':1, 'pad':1}
             )

plt.legend(loc=2,prop={'size':9})
plt.show()

######### END

######### PLOT
'''
plt.xlabel('Eje x : NUMBER')
plt.ylabel('Eje y : REMINDER NUMERO Modulo PRIME')
plt.title('TARGET Number %s :' % a.targetnumber)
'''


######### PRINT
'''
a = numero(23*73)
print('Numero :', a.targetnumber)
print('Root :', a.root)
print('Root:int :', a.root_int)

print('Curve_y :', a.curve_y)
print('Curve_x :', a.curve_x)

a.get_curve(20)

print('Curve_y :', a.curve_y, len(a.curve_y))
print('Curve_x :', a.curve_x, len(a.curve_x))

print('Max UP:',a.max_upx, a.max_upy)
print('Max DW:',a.max_dwx, a.max_dwy)
'''



