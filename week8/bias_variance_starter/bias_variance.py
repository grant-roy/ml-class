from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


def create_lines(x="an array of two hundred points [-1,1] in steps of .01",
                 y="our function value for every point in x"):

    return "a data frame with structure: data={'x': 200 points on the interval [-1, 1]  , 'y': sin(pi * x)}"


def fit_fx(N=2):
    # create f(x) = sin(pi * x)
    target = create_lines(x=, y=)

    # think about how you will use the following two arrays in this function
    g_x = []
    y_lines = []

    for i in range(1000):
        sample = "sample two points from target"
        fit_y = "this is your h_x calculation"

        # here you are interested in creating the horizontal fit line
        y_line = create_lines(y= )


    return {'target': target, 'g_x': g_x, 'y_lines': y_lines, 'fits': fits }

def calculate_bias(target=None, g_x=None):
    g_bar =
    bias =
    return bias


def calculate_variance(g_x=None):
    g_bar =
    variance =
    return variance


def plot(target=None, y_lines=None):
    "how will you plot both the sin curve and you fit lines?"
