from __future__ import division
from numpy.linalg import inv

import pandas as pd
import numpy as np
import math

def calculate_probs(x1=0, x2=0,x3=0):
    data = pd.read_csv('datatraining.csv', header=0)

    # our weight values corresponding to [scalar, x1, x2, x3]
    y_hats = []
    w = [-2.5, .161, .992, .444]

    X = data[['scalar','x1','x2','x3']]

    # pull only the rows where the x values math those passed into this function
    subset = X[(X['x1']==x1) & (X['x2']==x2) & (X['x3']==x3)]

    for index, row in subset.iterrows():
        dot_product = np.dot(w, row.T, out=None)
        probability = math.pow(math.e, dot_product) / (1 + math.pow(math.e, dot_product))
        y_hats.append( probability)


    y_hat = np.sum(y_hats)/len(subset)
    return y_hat
