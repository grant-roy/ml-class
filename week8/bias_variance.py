from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from scipy.stats import linregress

def create_lines(x=np.arange(-1, 1, .01), y=None):

    return pd.DataFrame(data={'x': x, 'y': y})


def fit_fx(N=2,horizontal=True):
    target = create_lines(y=np.sin(np.arange(-1, 1, .01) * math.pi))

    g_x = []
    y_lines = []
    fits = []
    for i in range(100):
        sample = target.sample(n=2).reset_index()
        #b = (sample.loc[0]['y'] + sample.loc[1]['y'])/ N
        if horizontal:
            fit_y = (sample.loc[0]['y'] + sample.loc[1]['y'])/ N
            y_line = create_lines(y=fit_y * np.ones(len(target)))
        else:
            lin = linregress(sample['x'], sample['y'])
            #print lin

            a = lin.slope

            #print a
            b = lin.intercept
            #print b
            x_1 = sample['x'].min()


            diff = np.subtract(target['x'], x_1)

            #print sample
            fit_y = np.add(a * diff, b) # divide this by 1000 and you get the bias
            #fit_y  = np.sum(fit_y) / len(target['x'])
            #fit_y  = a * np.arange(-1, 1, .01) + b
            #print fit_y
            fit_y  = np.sum(np.subtract(fit_y, target['y']))
            y_line  = create_lines(y=fit_y)

        g_x.append(fit_y)
        y_lines.append(y_line)
        #fits.append(fit_y)

    return {'target': target, 'g_x': g_x, 'y_lines': y_lines, 'fits': fits }

def calculate_bias(target=None, g_x=None,h1=False):
    g_bar = np.sum(g_x) / len(g_x)
    bias = np.sum(np.subtract(g_bar, target['y']) ** 2) / len(target)

    return bias


def calculate_variance(g_x=None):
    g_bar = np.sum(g_x) / len(g_x)
    variance = np.sum(np.subtract(g_bar, g_x) ** 2 ) / len(g_x)
    return variance


def plot(target=None, y_lines=None):
    plt.plot(target['y'])
    for line in y_lines:
        plt.plot(line['y'], c='r')
    plt.show()
