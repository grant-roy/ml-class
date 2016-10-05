import numpy as np

from matplotlib import pyplot as plt


def scatter(weights, digits):

    set_a = digits[digits.loc[:, 0].isin([1])].reset_index(drop=True)
    set_b = digits[digits.loc[:, 0].isin([5])].reset_index(drop=True)


    plt.scatter(set_a.loc[:, 1], set_a.loc[:, 2], marker='+')
    plt.scatter(set_b.loc[:, 1], set_b.loc[:, 2], c='green', marker='o')

    print "min x value: " + str(set_a.loc[:,1].min())
    print "max x value: " + str(set_b.loc[:,1].max())
    a = -weights.ix[0, 1] / weights.ix[0, 2]
    xx = np.linspace(-1.0602, 1.528)

    yy = a * xx - (weights.ix[0, 2] * 1. / weights.ix[0, 1])

    plt.plot(xx, yy, 'k-')

    plt.show()


