import numpy as np   # numpy is a powerful numerical library we will use for vector operations
import pandas as pd


'''
perceptron:      expects as an input a 4 column Pandas dataframe with the following columns:

x:               a column vector representing one dimension of the training data
y:               a column vector representing a second dimension of the traing data
classification:  the correct target function value for that point(i.e row)
scalar:          an added dimension to correspond with our weight vector
'''
def perceptron(training_data):
    x = training_data[['scalar','x','y']]
    y = training_data['classification']
    w = pd.DataFrame(np.random.randn(1, x.shape[1]))

    misclassified = 1
    while misclassified != 0:

        misclassified = 0

        for index, row in x.iterrows():

            y_hat = np.dot(w, row.T, out=None)
            if np.sign(y[index]) != np.sign(y_hat):

                misclassified += 1
                w = np.add(w, y[index]*row.values)
    return w
