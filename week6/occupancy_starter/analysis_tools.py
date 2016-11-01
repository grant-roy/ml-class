from __future__ import division
import pandas as pd
import numpy as np
import math


# return the number of misclassified points and the percentage misclassified
def misclassified_count(w, data):


# calculate the VC term in the generalization bound, see notebook for details
def vc_bound(N=1, tolerance=.01, mH=1):


# load data from file, rename the column representing 'y' to the string passed as 'y_name'
# in the case of our Occupancy data set the column in named 'Occupancy'
def load_data(file_name='', y_name=''):


# nicely format some print strings for the results, nothing too fancy, just string concatenation
def print_results(e_in, e_test, vc):
