# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:02:58 2021

@author: dogru
"""

import math
tetal= float(input("teta l: "))
tetar= float(input("teta r: "))


teta=(abs(180-tetal)+abs(180-tetar))*(1/2)
print("teta: {}".format(teta))
lamb=(16666)*(math.sin(math.radians(teta)))
print("lambda: {}".format(lamb))
lamt=float(input("theoretical lambda: "))
perror= (abs((lamt-lamb)*(1/lamt)))*100
dakika=(teta-int(teta))*60
dellamb=math.sqrt(((2/((int(teta)*60)+dakika))**2)+((500/16666)**2))
print("percentage error: {}".format(perror))
print("delta lambda: {}".format(dellamb))

