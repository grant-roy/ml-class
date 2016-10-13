import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# the following import statement show how you can import libraries not
# in your current path
import sys

sys.path.append('../utility')
import scatter as sc
import perceptron as pt


'''
function xy: returns data frame of semicircular points correspoding to 'x'
             and 'y' axis

r:           a radius number
x_scaler:    push the semi-circle along the x-axis
y_scaler:    push the semi-cicle along the y-axis
sign:        a positive or negative
'''
def xy(r, x_scaler=0, y_scaler=0, sign=1):
    phi = sign * np.arange(0, 3.14, .001)

    return pd.DataFrame(data={'x':r*np.cos(phi)+x_scaler,
                              'y':r*np.sin(phi)+y_scaler})

'''
initialize two data frames to hold points corresponding to red and blue semi-circles
'''
columns = ['x', 'y']
red = pd.DataFrame(data=np.zeros((0, len(columns))), columns=columns)
blue = red.copy(deep=True)


'''
how can we fill a semi-circular region like the ones shown??

replace the two '_' markers and fill in the loop body
'''
for _  in _
    red = pd.concat( _ ), axis=0)
    blue = pd.concat( _ ), axis=0)

'''
how can we sample 2000 random points from each dataframe??

'''
red_samples = red. _
blue_samples = blue. _

# assign classification to each semicircle
red_samples['classification'] = pd.Series([1] * 2000, index=red_samples.index)
blue_samples['classification'] = pd.Series([-1] * 2000, index=blue_samples.index)

all_samples = pd.concat([red_samples, blue_samples], axis=0).reset_index(drop=True)
all_samples['scalar'] = pd.Series([1] * len(all_samples), index=all_samples.index)

w = pt.perceptron(all_samples)
sc.scatter(all_samples, w)
