import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def scatter(data, weights):

    set_a = data[data['classification']==1]
    set_b = data[data['classification']==-1]

    plt.scatter(set_a['x'], set_a['y'], marker='+')
    plt.scatter(set_b['x'], set_b['y'], c='r', marker='o')

    a = -weights.loc[0, 1] / weights.loc[0, 2]
    xx = np.linspace(data['x'].min(), data['x'].max())
    yy = a * xx - (weights.loc[0, 0] * (1./weights.loc[0, 2]))

    plt.plot(xx, yy, 'k-')
    plt.show()
