# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:00:16 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.cos(gh.PI*t)
    return y

if __name__ == "__main__":
    t = np.arange(-300, 300)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = cos(πt)", *gh.xticks(5))
    pass