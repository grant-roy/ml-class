import numpy as np
import pandas as pd
import scatter_plot as sp
from matplotlib import pyplot as plt

def regression(data):
    X = data.as_matrix()

    # linear algebra with numpy
    A = np.vstack([X[:, 0], np.ones(len(X))]).T
    m, c = np.linalg.lstsq(A, X[:, 1])[0]

    return [m,c]


def plot_regression(data,m,c):
    # set_a = data[data['classification']==1]
    # set_b = data[data['classification']==-1]
    #
    plt.scatter(data['x'], data['y'], marker='+')
    # plt.scatter(set_b['x'], set_b['y'], c='r', marker='o')

    X = data.as_matrix()
    plt.plot(X[:, 0], m*X[:, 0] + c, 'r', label='Fitted line')
    plt.show()
