import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def scatter(data, weights):
    '''
    set_a will be the red semi-cicle pulled from 'data'
    set_b will be the blue semi-cicle pulled from 'data'
    '''
    set_a = _
    set_b = _

    '''
    the scatter function will need the x and y columns from each set
    '''
    plt.scatter(set_a _ , set_a _ , marker='+')
    plt.scatter(set_b _ , set_b _ , c='r', marker='o')

    '''
    the following is complete code for plotting the separating line from
    'weights'
    '''
    a = -weights.loc[0, 1] / weights.loc[0, 2]
    xx = np.linspace(data['x'].min(), data['x'].max())
    yy = a * xx - (weights.loc[0, 0] * (1./weights.loc[0, 2]))
    plt.plot(xx, yy, 'k-')

    plt.show()
