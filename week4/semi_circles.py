import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# our function to actually create the points on the x,y plane
# that creates a semi-circle
def xy(r, x_scaler=0, y_scaler=0, sign=1):
    phi = sign * np.arange(0, 3.14, .001)

    return pd.DataFrame(data={'x':r*np.cos(phi)+x_scaler,
                              'y':r*np.sin(phi)+y_scaler})

# we would like a semi-circle arc of a particular width. We
# specify the starting and ending radius, along with the decrement
# step as the third argument
columns = ['x', 'y']
red = pd.DataFrame(data=np.zeros((0, len(columns))), columns=columns)
blue = red.copy(deep=True)

# generate points on an x,y plane that will form a positive and negative
# semi-circle. 'red' will be like the St. Louis arch, and 'blue' will be flipped
# upside down.
for radius_step in np.arange(1., .89, -.001):
    red = pd.concat((red, xy(radius_step, y_scaler=.5)), axis=0)
    blue = pd.concat((blue, xy(radius_step, x_scaler=1, sign=-1)), axis=0)

# we will now sample 2000 random points from each of our semi-circle dataframes
red_samples = red.reset_index(drop=True).loc[np.random.choice(red.index, 2000)]
blue_samples = blue.reset_index(drop=True).loc[np.random.choice(blue.index, 2000)]

# assign classification to each semicircle
red_samples['classification'] = pd.Series([1] * 2000, index=red_samples.index)
blue_samples['classification'] = pd.Series([-1] * 2000, index=blue_samples.index)

all_samples = pd.concat([red_samples, blue_samples], axis=0).reset_index(drop=True)
all_samples['scalar'] = pd.Series([1] * len(all_samples), index=all_samples.index)
print all_samples.head()
print all_samples.tail()
#print pd.concat([red_samples, pd.Series([1] * 2000, name='scalar')], join='inner', axis=1)

# next create a full dataset from semi-circles with 'y' values for classification
# this will allow us to match the three columns our weight vector will have
#all_samples = pd.concat((red_samples, blue_samples), axis=0)
#print all_samples.reset_index(drop=True).tail()

# scalar = pd.Series([1] * len(coin_data), name='scalar')
#
# # create our x vector with the added scalar column
# x = pd.concat((scalar, coin_data.loc[:, ['size', 'mass']]), axis=1)
#
# # plot red and blue semicircles from sampled points
# plt.scatter(red_samples['x'], red_samples['y'], c='r')
# plt.scatter(blue_samples['x'], blue_samples['y'], c='b')
# plt.show()
