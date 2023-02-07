# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:38:53 2023

@author: Private
"""
import numpy as np
import matplotlib.pyplot as plt
PI = np.pi
plt.rcParams['font.family'] = 'MS Gothic'

def plot(x, y, label, xticks=None, xticklabels=None, yscale="linear"):
    fig = plt.figure(dpi=100)
    ax  = fig.add_subplot(
        111,
        xlabel = 't',
        ylabel = 'x(t)',
        xticks = xticks,
        xticklabels = xticklabels,
        yscale = yscale,
        )
    ax.plot(x, y, label=label)
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    plt.grid(True)
    plt.show()
    plt.close(fig)
    
def plot_mult(x, datas, labels, xticks=None, xticklabels=None):
    fig = plt.figure(dpi=100)
    ax  = fig.add_subplot(
        111,
        xlabel = 't',
        ylabel = 'x(t)',
        xticks = xticks,
        xticklabels = xticklabels,
        )
    for y, label in zip(datas, labels):
        ax.plot(x, y, label=label)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    plt.grid(True)
    plt.show()
    plt.close(fig)
    
def xticks_PI(cycle=1):
    xticks = np.arange(-cycle*2, cycle*2+1)/2*PI
    plus, minus = [], []
    for i in range(1, cycle+1):
        half = 2*i-1
        minus.append(str(-half)+"π/2")
        minus.append(str(-i)+"π")
        plus.append(str(half)+"π/2")
        plus.append(str(i)+"π")
    xticklabels = minus[::-1]+["0"]+plus
    return xticks, xticklabels

def xticks(cycle=1):
    xticks = np.arange(-cycle*2, cycle*2+1)/2
    plus, minus = [], []
    for i in range(1, cycle+1):
        half = i-1
        minus.append(str(-half)+".5")
        minus.append(str(-i))
        plus.append(str(half)+".5")
        plus.append(str(i))
    xticklabels = minus[::-1]+["0"]+plus
    return xticks, xticklabels