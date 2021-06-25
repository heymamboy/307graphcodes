# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:40:55 2021

@author: dogru
"""

import matplotlib.pyplot as plt 


I=[-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30]
v=[-93.8938,-81.5815,-71.3713,-58.5585,-48.048,-35.2352,-20.02,-10.01,1.3013,12.7127,24.1241,35.4354,46.4464,]


def linear_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('Linear fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

a, b = linear_fit(I,v)
yfit = [a + b * xi for xi in I]
plt.plot(I, yfit,color='green',linestyle=':',label="Linear fit: y = {:.2f}x {:.2f}".format(b,a))

plt.plot(I,v,color="r",marker="o", label="Part 1")

plt.title('Current vs Hall Voltage')
plt.xlabel('Current (mA)')
plt.ylabel('Hall Voltage (mV)') 
plt.xlim((-35,35))

plt.legend(loc='upper left',fancybox=True, framealpha=1)
plt.grid()
plt.show()


