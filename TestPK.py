# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:24:49 2023

@author: James Curtis Buckler
"""
import numpy as np
import MCintegrate as mc

def f(x):
    return(x+x**2)

a = 0
b = 1
n = 500000
integral = mc.MCint(f,a,b,n)

print(f'integral +{integral:0.3f}')
