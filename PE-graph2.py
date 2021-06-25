# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:08:27 2021

@author: dogru
"""
import numpy as np
import pylab as pl

#I do not want to add data set as text. Therefore, I wrote them as lists.

v=np.array([1.918,1.472,1.314,0.780,0.780])
f=np.array([821*10**(12),740*10**(12),688*10**(12),549*10**(12),520*10**(12)])

pl.errorbar(f, v, xerr = 0.1, yerr = 0.1, label='error',linestyle="None")
m, n = np.polyfit(f, v, 1)
pl.plot(f, v, 'o')
pl.plot(f, m*f + n, label='y= 3.77e-15*f - 1.25') # m = slope, n = intercept


pl.title(' Potential vs. Frequency')
pl.ylabel('Potential (V)')
pl.xlabel(' Frequency (Hz)')
pl.legend(loc='upper right',fancybox=True, framealpha=1)
pl.show