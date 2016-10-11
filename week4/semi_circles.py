import matplotlib.pyplot as plt
import numpy as np


def xy(r, phi):
    return r*np.cos(phi), r*np.sin(phi)


phis1 = np.arange(0, 3.14, 0.01)
r1 = 1.
plt.plot(*xy(r1, phis1), c='r', ls='-')


phis2 = np.arange(0, 3.14, 0.01)
r2 = .9
plt.plot(*xy(r2, phis2), c='r', ls='-')


phis3 = -np.arange(0, 3.14, 0.01)
r3 = 1.
plt.plot(*xy(r3, phis3), c='b', ls='-')

phis4 = -np.arange(0, 3.14, 0.01)
r4 = .9
plt.plot(*xy(r4, phis4), c='b', ls='-')


plt.show()