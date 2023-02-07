# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:46:00 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.ones_like(t)
    for i in range(1, 19):
        y = y + (t**i)/np.math.factorial(i)
        pass
    return y

if __name__ == "__main__":
    t = np.arange(-300, 301)/100
    y = equation(t)
    #y = np.exp(t)
    gh.plot(t, y, "x(t) = exp(t)", *gh.xticks(5))    
    pass