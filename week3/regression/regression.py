import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# we'll read in a data file for ABT Options contracts that covers  large historical period
# NOTE: this is REAL data, and data investment banks have probably wagered billions on. This is
# NOT a toy data set.
df = pd.read_fwf('ABT.txt', colspecs='infer', widths=None, header=0,
                 names=['optionid','issuer','date','cp_flap','exercise_style','index_flag','exdate','root','suffix',
                        'last_date','open_interest','ss_flag','div_convention','flag','ticker','best_bid','best_offer',
                        'volume','strike_price','cfadj','impl_volatility','delta','gamma','theta','vega'])

# get the last 500000 rows of data
# convert_objects is performing a great service to us, it is replacing
# nonsensical values with Nan, thereby allowing us to do the conversion to numeric
# data even though some of our data is "spurious". This "spurious" data is a major
# source of pain in data analysis. Extracting data and getting it into a usable from for
# analysis is known as 'ETL'....Extract Transform Load
abt_vol = df.tail(100000).convert_objects(convert_numeric=True)

X = abt_vol[['date', 'impl_volatility']].as_matrix()

# blow out any rows(note axis=1) that contain NaN values
X = X[~np.isnan(X).any(axis=1)]

# linear algebra with numpy
A = np.vstack([X[:, 0], np.ones(len(X))]).T
m, c = np.linalg.lstsq(A, X[:, 1])[0]

abt_vol.plot(kind='scatter', x='date', y='impl_volatility')
plt.plot(X[:, 0], m*X[:, 0] + c, 'r', label='Fitted line')
plt.show()

