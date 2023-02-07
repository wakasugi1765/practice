# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:00:28 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.sin(2*t + gh.PI/2)
    return y

if __name__ == "__main__":
    t = np.arange(-500, 500)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = cos(πt)", *gh.xticks_PI(5))
    pass