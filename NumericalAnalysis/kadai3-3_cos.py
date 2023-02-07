# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:39:25 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.ones_like(t)
    for i in range(1, 11):
        n = 2*i
        sign = -1 if i%2 == 1 else 1
        y = y + sign*(t**n)/np.math.factorial(n)
        pass
    return y

if __name__ == "__main__":
    t = np.arange(-200, 201)/100 * gh.PI
    y = equation(t)
    gh.plot(t, y, "x(t) = cos(t)", *gh.xticks_PI(5))    
    pass