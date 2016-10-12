import matplotlib.pyplot as plt
import numpy as np


def xy(r, x_scaler=0, y_scaler=0, sign=1):
    phi = sign * np.arange(0, 3.14, 0.01)
    return r*np.cos(phi)+x_scaler, r*np.sin(phi)+y_scaler

semi_circle_width = np.arange(1., .89, -.01)
red, blue = [], []

for x in semi_circle_width:
    red.append(xy(x, y_scaler=.5))
    blue.append(xy(x, x_scaler=1, sign=-1))
    plt.plot(*red[-1], c='r', ls='-')
    plt.plot(*blue[-1], c='b', ls='-')


# rand_x = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
# rand_y = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
# rand_coordinates = zip(rand_x, rand_y)
# print rand_coordinates

# might be useful for generating random separating lines
#rand_x = np.random.uniform(low=-1.0, high=2.0, size=(1, 1))
#rand_y = np.random.uniform(low=-1.0, high=1.5, size=(1, 1))
#rand_coordinates = zip(rand_x, rand_y)


plt.show()

