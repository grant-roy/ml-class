import random
import numpy as np
from random import randint
from matplotlib import pyplot as plt


def monte_carlo_pi(n):
    inside=0
    for point in range(n):
        x, y = random.random(), random.random()
        if(x*x + y*y < 1.0):
            inside+=1
    return 4.0*inside/n

def plot_unit_circle(n):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    circ = plt.Circle((0, 0), radius=1, edgecolor='b', facecolor='None')
    ax.add_patch(circ)
    x,y =  zip(*[(np.random.uniform(low=-1, high=1),np.random.uniform(low=-1, high=1)) for point in range(n)])

    plt.scatter(x,y,c='r')
    plt.show()
