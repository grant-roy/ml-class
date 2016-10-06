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

# get the last 10000 rows of data
abt_vol = df.tail(50000)

# We have some problems with our data. First, we need to convert the dates to numbers,
# which isn't too big a deal. Our larger problem though is the column that we are interested in
# analyzing: 'impl_volatility; has missing values that show up as '.' in the column. This is a
# nightmare, however it is a real life nightmare that you must know how to deal with. There is
# a reason some people say ETL(Extract Transform Load) is at least half the battle.

# convert dates
abt_vol['date'] = abt_vol['date'].astype(float)

abt_vol['impl_volatility'][abt_vol['impl_volatility'] == '.'] = None
abt_vol['impl_volatility'] = abt_vol['impl_volatility'].astype(float)

X = abt_vol[['date', 'impl_volatility']].as_matrix()

# blow out any rows(note axis=1) that contain NaN values
X = X[~np.isnan(X).any(axis=1)]
print X

# linear algebra with numpy
A = np.vstack([X[:, 0], np.ones(len(X))]).T
m, c = np.linalg.lstsq(A, X[:, 1])[0]

abt_vol.plot(kind='scatter', x='date', y='impl_volatility')
plt.plot(X[:, 0], m*X[:, 0] + c, 'r', label='Fitted line')
plt.show()
