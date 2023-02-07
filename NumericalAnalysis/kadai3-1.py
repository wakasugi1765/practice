# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:04:06 2023

@author: Private
"""
import graph as gh
import numpy as np

def eq0(t):
    y = t
    return y

def eq1(t):
    y = t**2
    return y

def eq2(t):
    y = t**3
    return y

if __name__ == "__main__":
    t = np.arange(-300, 300)/100
    datas = [eq0(t),eq1(t),eq2(t)]
    labels = ["x(t) = t", "x(t) = t^2", "x(t) = t^3"]
    gh.plot_mult(t, datas, labels, *gh.xticks(5))
    pass
