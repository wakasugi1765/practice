# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:00:04 2023

@author: Private
"""
import graph as gh
import numpy as np

def equation(t):
    y = 1 - np.sin(t)
    return y

if __name__ == "__main__":
    t = np.arange(-700, 700)/100
    y = equation(t)
    gh.plot(t, y, "x(t) = 1-sin(t)", *gh.xticks_PI(5))
    pass
