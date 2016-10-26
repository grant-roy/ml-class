from __future__ import division
import pandas as pd
import numpy as np
import math



def misclassified_count(w, data):
    scalar = pd.Series([1] * (len(data)+1), name='scalar')
    y = data['Classification']
    data['scalar'] = scalar
    x = data.drop(['Classification'], axis=1)

    misclassified = 0
    for index, row in x.iterrows():

        y_hat = np.dot(w, row.T, out=None)

        if np.sign(y[index]) != np.sign(y_hat):
            misclassified += 1
    return {'misclassified':misclassified, 'ratio_misclassified':misclassified/len(data)}


def vc_bound(N=1, tolerance=.14, mH=1):
    return math.sqrt( (8/N) * math.log((4 * 2 * mH)/tolerance ) )


def print_results(e_in, e_out, vc):

    print "\n"
    print "E_in number misclassified: " + str(e_in['misclassified']) + ", percentage error: " + str(e_in['ratio_misclassified'])
    print "E_out number misclassified: " + str(e_out['misclassified']) + ", percentage error: " + str(e_out['ratio_misclassified'])
    print "VC bound: " + str(vc)
    print "\n"
