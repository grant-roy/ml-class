import pandas as pd
import numpy as np



def pocket(classification_targets, iterations=150):
    scalar = pd.Series([1] * (len(classification_targets)+1), name='scalar')
    y = classification_targets['Classification']
    classification_targets['scalar'] = scalar
    x = classification_targets.drop(['Classification'], axis=1)
    #x = pd.concat((scalar, classification_targets.loc[:,:]), axis=1, join_axes=classification_targets.index).reset_index()


    # set th weight values
    w = w_save = pd.DataFrame(np.random.randn(1, x.shape[1]))

    misclassified = 0
    min_error_count = float('inf')
    # we are going to run the pocket algorithm for 1000 iterations
    for i in range(iterations):

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

    return {'min_error': min_error_count, 'w': w_save}
