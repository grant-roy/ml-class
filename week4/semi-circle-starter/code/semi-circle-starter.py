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

- our loop needs to go through a range of 1. : .9 in very small steps(.001 to be exact)
  in other words we are looping backwards from a radius of 1. to .9. You will
  need to create this range to fill in the loop. Conceptually we are creating the outer
  arc, and then successively making the arcs very slightly smaller

- to build up our semi-cicles, we will use the 'xy' function inside the pd.concat statements
  in our loop body. The 'xy' function will return points along the arc of a cicles radius. Experiment
  with calling the function to gain some intuition of how it works. Conceputally the pd.concat statements
  is building up a dataframe of points specifying all of the arcs of each semi-circle


replace the  '_' markers and fill in the loop body
'''
for decrement  in _
    red = pd.concat( _ ), axis=0)
    blue = pd.concat( _ ), axis=0)

'''
how can we sample 2000 random points from each dataframe??

* hint: use numpys random number facilities to help grap random points in the dataframe
'''
red_samples = red. _
blue_samples = blue. _

'''
here we are adding the binary classification to our data in prepartion for the perceptron
'''
red_samples['classification'] = pd.Series([1] * 2000, index=red_samples.index)
blue_samples['classification'] = pd.Series([-1] * 2000, index=blue_samples.index)

'''
here we just add the two data frames together, creating one that has all of the points
next we add the neccessary scalar to the data
'''
all_samples = pd.concat([red_samples, blue_samples], axis=0).reset_index(drop=True)
all_samples['scalar'] = pd.Series([1] * len(all_samples), index=all_samples.index)

'''
use the *perceptron* module to classify the dataset and return the weights that give the correct classification
use the *scatter* module to plot the the data along with the separating line
'''
w = pt.perceptron(all_samples)
sc.scatter(all_samples, w)
