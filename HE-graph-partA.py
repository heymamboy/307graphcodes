# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:14:26 2021

@author: dogru
"""
import matplotlib.pyplot as plt 



B=[20,40,60,80,100,120,140,160,180,200,220,240,260,280,300]
vh=[-14.9149,-9.9099,-5.2052,-0.3003,4.6046,9.2092,13.9139,18.018,22.5225,26.7267,30.8308,34.8348,38.6386,42.4424,46.046]

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

a, b = linear_fit(B,vh)

yfit = [a + b * xi for xi in B]
plt.plot(B, yfit,color='grey',linestyle=':',label="Linear fit: y = {:.2f}x {:.2f}".format(b,a))

plt.plot(B,vh,color="b",marker="o", label="Part 1")

plt.title('Hall Voltage vs. Flux Density')
plt.xlabel('Flux Density (mT)')
plt.ylabel('Hall Voltage (mV)') 

plt.legend(loc='upper left',fancybox=True, framealpha=1)
plt.grid()
plt.show()




