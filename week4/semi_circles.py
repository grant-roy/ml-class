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

    return pd.DataFrame(data={'x': r*np.cos(phi)+x_scaler,
                              'y': r*np.sin(phi)+y_scaler,
                              'classification': sign,
                              'scalar': 1})

def semi_circular_samples(x_scaler=0, y_scaler=0):
    semi_circles = pd.DataFrame()

    for radius_step in np.arange(1., .49, -.01):
        semi_circles = semi_circles.append(xy(radius_step, y_scaler=.5))
        semi_circles = semi_circles.append(xy(radius_step, x_scaler=1, sign=-1))

    return pd.concat([semi_circles[semi_circles['classification']==1].sample(n=1000),
                      semi_circles[semi_circles['classification']==-1].sample(n=1000)],
                      axis=0).reset_index()

w = pt.perceptron(samples)
sc.scatter(samples, w)
