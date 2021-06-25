# -*- coding: utf-8 -*-
"""
Created on Wed May 19 22:55:19 2021

@author: dogru
"""
import pylab as pl

fr_averager=[1.365,1.33,1.305,1.285,1.235,1.215,1.19,1.17,1.145,1.13,1.115]
sc_averager=[2.305,2.27,2.215,2.195,2.145,2.115,2.085,2.055,2.01,1.96,1.925]
wavelength=[0.194,0.189,0.185,0.181,0.177,0.173,0.170,0.167,0.164,0.161,0.158]

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

a,b = best_fit(wavelength, fr_averager)
pl.dot(wavelength, fr_averager)
yfit = [a + b * xi for xi in wavelength]
pl.plot(wavelength, yfit,color='red',label='First Ring')


pl.errorbar(wavelength,fr_averager, xerr = 0, yerr = 0.02)
pl.errorbar(wavelength,sc_averager, xerr = 0, yerr = 0.02)

pl.title('Wavelength vs. Average Radius')
pl.xlabel('Wavelength (A)')
pl.ylabel(' Average Radius (cm)')
pl.legend(loc='upper left',fancybox=True, framealpha=1)
pl.show