import numpy as np
from matplotlib import pyplot as plt


def plot_pocket(weights, digits):

    set_a = digits[digits.loc[:, 0].isin([1])].reset_index(drop=True)
    set_b = digits[digits.loc[:, 0].isin([5])].reset_index(drop=True)

    plt.scatter(set_a.loc[:, 1], set_a.loc[:, 2], marker='+')
    plt.scatter(set_b.loc[:, 1], set_b.loc[:, 2], c='green', marker='o')

    a = -weights.loc[0, 1] / weights.loc[0, 2]
    xx = np.linspace(0, .6)

    yy = a * xx - (weights.loc[0, 0] * (1./weights.loc[0, 2]))
    plt.plot(xx, yy, 'k-')
    plt.show()


