# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:29:51 2021

@author: dogru
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

#define x and y dataset
#xdata = np.array( [8.5, 10.0, 13.0, 15.0, 18.0, 20.0] ) 
xdata = np.array( [8.0, 11.0, 13.0, 16.0, 18.5, 21.0] ) 
ydata = np.array( [1., 0., 1., 0., 1., 0. ] )

# Define the function for the fit 
def func(x,p1,p2,p3):
    return p1*np.sin(x*p2+p3)+0.5

# Start fitting, the results are kept in sonuc array)
sonuc, pcov = curve_fit(func, xdata, ydata, p0=(0.2, 1.2, 1.0))

# Gather the results of fitting 
p1=sonuc[0]
p2=sonuc[1]
p3=sonuc[2]

#Period of the sine function 
period=2*np.pi/p2

#recalculation of sin function, with linear density 200 between 5 and 25 on xaxis
xaxis = np.linspace(5, 25, 200) 
curve_y = func(xaxis, p1, p2, p3)

#add the fit curve to the plot
plt.plot(xaxis, curve_y, '-') 
#add the data to the plot 
plt.plot(xdata, ydata, 'ro') 
plt.title('Current vs Voltage') 
plt.xlabel('Voltage(V)') 
plt.ylabel('Current')
#show the plot print period
plt.show()
print(period)
# Voltage values at the peaks should be written in the data array.