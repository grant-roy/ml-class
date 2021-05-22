import numpy as np
import pandas as pd
import scatter_plot as sp
from matplotlib import pyplot as plt

def regression(data):
    X = data.values

    # linear algebra with numpy
    A = np.vstack([X[:, 0], np.ones(len(X))]).T
    m, c = np.linalg.lstsq(A, X[:, 1],rcond=-1)[0]

    return [m,c]


def plot_regression(data,m,c):

    plt.scatter(data['x'], data['y'], marker='+')

    X = data.values
    plt.plot(X[:, 0], m*X[:, 0] + c, 'r', label='Fitted line')
    plt.show()
