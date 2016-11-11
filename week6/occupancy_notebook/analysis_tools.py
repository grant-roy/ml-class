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


def vc_bound(N=1, tolerance=.14, d_vc=1):
    return math.sqrt( (8/N) * math.log(
                                (4 * math.pow(2 * N, d_vc) + 1) /tolerance ) )


def load_data(file_name='', y_name=''):
    data = pd.read_csv(file_name, header=0)
    data = data.rename(columns = {y_name:'Classification'})
    del data['date']
    data['Classification'] = data['Classification'].apply(lambda value: value if value==1 else -1)
    return data


def print_results(e_in, e_test, vc):

    print "\n"
    print "E_in number misclassified: " + str(e_in['misclassified']) + ", percentage error: " + str(e_in['ratio_misclassified'])
    print "E_test number misclassified: " + str(e_test['misclassified']) + ", percentage error: " + str(e_test['ratio_misclassified'])
    print "VC bound: " + str(vc)
    print "\n"
