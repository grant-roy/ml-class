import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# our function to actually create the points on the x,y plane
# that creates a semi-circle
def xy(r, x_scaler=0, y_scaler=0, sign=1):
    phi = sign * np.arange(0, 3.14, 0.01)

    return pd.DataFrame(data={'x':r*np.cos(phi)+x_scaler,
                              'y':r*np.sin(phi)+y_scaler})

    #return r*np.cos(phi)+x_scaler, r*np.sin(phi)+y_scaler

# we would like a semi-circle arc of a particular width. We
# specify the starting and ending radius, along with the decrement
# step as the third argument
semi_circle_width = np.arange(1., .89, -.01)
columns = ['x', 'y']
red = pd.DataFrame(data=np.zeros((0, len(columns))), columns=columns)
blue  = red.copy(deep=True)

# generate points on an x,y plane that will form a positive and negative
# semi-circle. 'red' will be like the St. Louis arch, and 'blue' will be flipped
# upside down.
for index, radius_step in enumerate(semi_circle_width):

    #red_x, red_y = xy(radius_step, y_scaler=.5)
    #xy(radius_step, y_scaler=.5)
    red = pd.concat((red, xy(radius_step, y_scaler=.5)), axis=0)
    blue = pd.concat((blue, xy(radius_step, x_scaler=1, sign=-1)), axis=0)
    #print red
    #red['x'] = red_x
    #print red.tail()
    #red['y'] =red_y
    #blue.ix['x'], blue.loc['y'] = xy(radius_step, x_scaler=1, sign=-1)
print red.reset_index()
#plt.plot(*red[index], c='r', ls='-')
#plt.plot(*blue[-1], c='b', ls='-')


# here we are going to generate random points on an x,y plane. Some of these points
# will fall within our semicircle, others will not
#rand_x = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
#rand_y = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
#rand_coordinates = zip(rand_x, rand_y)

#for index, item in enumerate(semi_circle_width):
   # print red[index]

#rand_x = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
#rand_y = [round(np.random.uniform(low=-1.0, high=2.0), 2) for _ in xrange(100)]
#rand_coordinates = zip(rand_x, rand_y)
#plt.scatter(rand_coordinates,c='g')
# print rand_coordinates

# might be useful for generating random separating lines
#rand_x = np.random.uniform(low=-1.0, high=2.0, size=(1, 1))
#rand_y = np.random.uniform(low=-1.0, high=1.5, size=(1, 1))
#rand_coordinates = zip(rand_x, rand_y)


#plt.show()
