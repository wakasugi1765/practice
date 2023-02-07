# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:59:54 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.cos(2*t + gh.PI/2)
    return y

if __name__ == "__main__":
    t = np.arange(-500, 500)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = cos(2t + π/2)", *gh.xticks_PI(5))
    pass