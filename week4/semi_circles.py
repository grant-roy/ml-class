import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

sys.path.append('../utility')
import scatter_plot as sc
import perceptron as pt


# our function to actually create the points on the x,y plane
# that creates a semi-circle
def xy(r, x_scaler=0, y_scaler=0, sign=1):
    phi = sign * np.arange(0, 3.14, .01)

    return pd.DataFrame(data={'x':r*np.cos(phi)+x_scaler,
                              'y':r*np.sin(phi)+y_scaler,
                              'classification': sign,
                              'scalar': 1})

# we would like a semi-circle arc of a particular width. We
# specify the starting and ending radius, along with the decrement
# step as the third argument
columns = ['x', 'y','classification','scalar']
red = pd.DataFrame(data=np.zeros((0, len(columns))), columns=columns)
blue = red.copy()

# generate points on an x,y plane that will form a positive and negative
# semi-circle. 'red' will be like the St. Louis arch, and 'blue' will be flipped
# upside down.
for radius_step in np.arange(1., .49, -.01):
    red = pd.concat((red, xy(radius_step, y_scaler=.5)), axis=0, ignore_index=True)
    blue = pd.concat((blue, xy(radius_step, x_scaler=1, sign=-1)), axis=0, ignore_index=True)

# we will now sample 1000 random points from each of our semi-circle dataframes
all_samples = pd.concat([red.loc[np.random.choice(len(red), 1000)],
                         blue.loc[np.random.choice(len(blue), 1000)]],
                         axis=0, ignore_index=True)

w = pt.perceptron(all_samples)
sc.scatter(all_samples, w)
