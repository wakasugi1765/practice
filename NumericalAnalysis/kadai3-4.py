# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 00:03:58 2023

@author: Private
"""
import graph as gh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation, PillowWriter

def eq0(t, a=2.0):
    y = a**(t)
    return y

def eq1(t, a=2.0):
    y = (a**(t))/np.abs(np.log(a))
    return y

def plot_mult(x, y0, y1, text, xticks=None, xticklabels=None):
    fig = plt.figure(dpi=100)
    ax  = fig.add_subplot(
        111,
        xlabel = 't',
        ylabel = 'x(t)',
        xticks = xticks,
        xticklabels = xticklabels,
        )
    ax.plot(x, y0, color='red')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    ax.plot(x, y1, color='blue')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right')
    ax.text(0, 0, text)
    plt.grid(True)
    plt.show()
    plt.close(fig)

def output_gif(
        t,
        xticks=None, xticklabels=None,
        interval = 100
        ):
    fig = plt.figure(dpi=100)
    ax  = fig.add_subplot(
        111,
        xlabel = 't',
        ylabel = 'x(t)',
        xticks = xticks,
        xticklabels = xticklabels,
        )
    plt.grid(True)
    artist_list = []
    for i in range(20):
        a = 2.0 + i/10.0
        artist_list.append([
            plt.plot(t, eq0(t, a), color='red')[0], 
            plt.plot(t, eq1(t, a), color='blue')[0], 
            plt.text(0, 0, 'base = '+str(a))
            ])
    ani = ArtistAnimation(fig=fig, artists=artist_list, interval=interval)
    ani.save("kadai3-4.gif")
    plt.close(fig)
    pass

if __name__ == "__main__":
    t = np.arange(-200, 200)/100
    plot_mult(t, eq0(t, 2.718), eq1(t, 2.718), 'optimal base = 2.718', *gh.xticks(5))
    output_gif(t, *gh.xticks(5), interval=100)
    pass