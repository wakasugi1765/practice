# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:49:34 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.sin(gh.PI*t)
    return y

if __name__ == "__main__":
    t = np.arange(-300, 300)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = sin(πt)", *gh.xticks(5))
    pass
    