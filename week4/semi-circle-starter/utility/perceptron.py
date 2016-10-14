import numpy as np
import pandas as pd


'''
you will need to fill create a function that will classify the data passed to it using the
perceptron algorithm. Create the function based on the specification below
'''


'''
perceptron:      expects as an input a 4 column Pandas dataframe with the following columns:

x:               a column vector representing one dimension of the training data
y:               a column vector representing a second dimension of the traing data
classification:  the correct target function value for that point(i.e row)
scalar:          an added dimension to correspond with our weight vector
'''
def _


    misclassified = 1
    while misclassified != 0:

        misclassified = 0

        for index, row in x.iterrows():

            y_hat = np.dot(w, row.T, out=None)
            if np.sign(y[index]) != np.sign(y_hat):

                misclassified += 1
                w = np.add(w, y[index]*row.values)
    return w
