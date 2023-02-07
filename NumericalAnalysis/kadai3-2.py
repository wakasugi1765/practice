# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:08:24 2023

@author: Private
"""
import graph as gh
import numpy as np

def eq0(t):
    y = 1**t
    return y

def eq1(t):
    y = 2**t
    return y

def eq2(t):
    y = 3**t
    return y

if __name__ == "__main__":
    t = np.arange(-300, 300)/100
    datas = [eq0(t),eq1(t),eq2(t)]
    labels = ["x(t) = 1^t", "x(t) = 2^t", "x(t) = 3^t"]
    gh.plot_mult(t, datas, labels, *gh.xticks(5))
    pass