import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# we'll read in a data file for ABT Options contracts that covers  large historical period
# NOTE: this is REAL data, and data investment banks have probably wagered billions using. This is
# NOT a toy data set.

# fill in the missing method for reading in text data
df = pd.  ('ABT.txt', colspecs='infer', widths=None, header=0,
                 names=['optionid','issuer','date','cp_flap','exercise_style','index_flag','exdate','root','suffix',
                        'last_date','open_interest','ss_flag','div_convention','flag','ticker','best_bid','best_offer',
                        'volume','strike_price','cfadj','impl_volatility','delta','gamma','theta','vega'])

# this data set has REAL problems, by that I mean it's not perfect,
# there are errors and omissions in columns that will screw up numeric calculations.
# things like a '.' in some rows where there should be numbers, so if you try do a calculation
# that one particular row will screw the whole thing up. This is ETL(Extract Transform Load).
# Luckily, there is a Pandas method that can help with this

# Fill in the missing method
abt_vol = df.tail(100000). (convert_numeric=True)

# add a method on to the end here that will return a matrix from a pandas data frame
X = abt_vol[['date', 'impl_volatility']].

# blow out any rows(note axis=1) that contain NaN values
X = X[~np.isnan(X).any(axis=1)]

# linear algebra with numpy
A = np.vstack([X[:, 0], np.ones(len(X))]).T

# numpy has a method for doing least square using linear algebra
m, c = np. (A, X[:, 1])[0]

# here we'll plot the resulting regression
abt_vol.plot(kind='scatter', x='date', y='impl_volatility')
plt.plot(X[:, 0], m*X[:, 0] + c, 'r', label='Fitted line')
plt.show()