import pandas as pd
import numpy as np
import pocket_plot as pl


# read in the digits data from text file
digits = pd.read_csv('digits_training_features.csv', header=None)

# we actually only want to do binary classification at this stage
# so we'll take only the rows from digits that correspond to '1' or '5'
classification_targets = digits[digits.loc[:, 0].isin([1, 5])].reset_index(drop=True)

# create the scalar vector of '1's..this is the bit of trickery that let's us turn our summation into
# a convenient dot product. we will add this as a column along with 'size' and 'mass' from our coin data
# this will allow us to match the three columns our weight vector will have
scalar = pd.Series([1] * len(classification_targets), name='scalar')

# create our x vector with the added scalar column, we don't want the first column which is the classification
x = pd.concat((scalar, classification_targets.loc[:, 1:]), axis=1)

# the correct value for the digits is the first column of our data
y = classification_targets.loc[:, 0]

# we need to convert these digits 1 and 5 into a binary signal [1,-1]
y = y.apply(lambda digit: digit if digit==1 else -1)

# set th weight values
w = w_save = pd.DataFrame(np.random.randn(1, x.shape[1]))

misclassified = 0
min_error_count = float('inf')
# we are going to run the pocket algorithm for 1000 iterations
for i in range(150):

    # iterate through all the rows of x
    for index, row in x.iterrows():

        y_hat = np.dot(w, row.T, out=None)

        if np.sign(y[index]) != np.sign(y_hat):

            w = np.add(w, y[index]*row.values)
            break

    # evaluate w on all the next candidates
    for index, row in x.iterrows():

        y_hat = np.dot(w, row.T, out=None)

        if np.sign(y[index]) != np.sign(y_hat):
            misclassified += 1

    if misclassified < min_error_count:
        w_save = w
        min_error_count = misclassified

    misclassified = 0

print "min error count: " + str(min_error_count)
print(w_save)

# let's examine our weight vector
pl.plot_pocket(w_save, classification_targets)