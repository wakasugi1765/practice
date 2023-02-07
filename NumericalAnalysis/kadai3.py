# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:50:20 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = np.full_like(t, gh.PI/2)
    for i in range(1, 100):
        y = y - np.sin(2*i*t)/i
        pass
    return y

if __name__ == "__main__":
    t = np.arange(-300, 300)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = π/2 - sin2t - sin4t/2 - ...", *gh.xticks(5))
    pass