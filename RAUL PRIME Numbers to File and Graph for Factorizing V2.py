#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:57:42 2016

@author: raul
"""

import numpy as np
import matplotlib.pyplot as plt


# Creates an array with True if it is a prime [0] = 0
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(4,n,2):              #Eliminates EVEN numbers
        sieve[i] = False

    for i in range(3,int(n**0.5)+1,2):  #Starts the sieve
        if sieve[i]:
            for j in range(i, n, i):
                sieve[j] = False
            #sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
            sieve[i] = True
    sieve[0] = False                    #Eliminates ZERO
    sieve[1] = False                    #Eliminates ONE
    
    return sieve


# Creates an array with True if it is a prime [0] = 0 
# and print it to a file PRIMES.TXT   
def write_primes_to_file(n):
    p_list = primes(n)
    foo = open('primes.txt', 'r+')           #Opens the file PRIMES.TXT
    for i in range(n):
        if p_list[i]:
            foo.write(str(i)+'\n')
        
    foo.close()        

    
# WE START THE GAME
'''Primes:
      2      3      5      7     11     13     17     19     23     29 
     31     37     41     43     47     53     59     61     67     71 
     73     79     83     89     97    101    103    107    109    113 
    127    131    137    139    149    151    157    163    167    173 
'''
# Large prime numbers = 83, 137, 277, 6343, 9929, 12343, 22573
# 151 * 157 = 23707
#  41 * 277 = 11357
'''
Primes seguidos: 10037, 10039, 10061, 10067
Primes: 23677 , 23687 , 23689, 23719

Try:
3239 = 41 * 79
6191 = 41 * 151
23689
23707 = 151 * 157 NOT PRIME
23719
14507 = 89 * 163
''' 

# Initial Values   
upto_n = 20000 #numero maximo al que va a contar primos
num_fact = 10067 #numero que se va a analizar
max_n = 5000 # numero hasta el que dibuja grafico

max_xaxis = 1000     

list_primes = primes(upto_n) #general la lista de primos con la funcion primes
rango = 0

# Count number of primes
for i in range(2,upto_n):
    if list_primes[i]:
        rango += 1

# Create x, y as arrays of dimension RANGO
x = np.zeros((max_n-2,), dtype=np.int)
y = np.zeros((max_n-2,), dtype=np.int)
der_y = np.zeros((max_n-2,), dtype=np.int) #to calculate derivate of graph

# Fills the values of X, Y 
# with the primes and reminders module prime
position = 0
for i in range(2,max_n):
    x[position] = i          # Graph of prime number
    # x[position] = position # Graph of prime position
    y[position] = num_fact % i
    der_y[position] = 1 * ( y[position] - y[position - 1] ) / ( x[position] - x[position - 1] )
    position += 1


# Draw the graph
# plt.xlim(0,10000)

plt.axis([0,250,-50,200])

plt.xlabel('Eje x : PRIME')
plt.ylabel('Eje y : REMINDER NUMERO Modulo PRIME')
plt.title('TARGET Number {0} :'.format(num_fact ))

plt.grid(True)

plt.plot(x , y,     color='red',  label='P Mod n', linestyle='dashed', marker='o', linewidth = 1)
plt.plot(x , der_y, color='blue', label='Derivate', linestyle='solid' , marker='.', linewidth = 2)

plt.legend(loc=2,prop={'size':9})
plt.savefig('Numero-{0}.png'.format(num_fact), dpi=900)
plt.show()







   