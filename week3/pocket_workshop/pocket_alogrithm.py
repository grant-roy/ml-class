# import statements go below


# read in the digits data from 'digits_training_features.csv'
digits = "code here"

# we actually only want to do binary classification at this stage
# so we'll take only the rows from digits that correspond
# to '1' or '5'(these values are in column 0, and represent our 'y')
classification_targets = digits["code here"].reset_index(drop=True)

# this will allow us to match the three columns our weight vector will have
scalar = "create our scalar column of ones"

# create our x vector with the added scalar column by concatenation,
x = pd.concat("code here to combine 'scalar' with 'classificaton_targets'", axis=1)

# the first column of classification_targets are the actual numeric digits themselves
y = classification_targets.loc[:, 0]

# we have a problem...our 'y' is currently either '1' or '5', not '1' or '-1' that we need
# we must remedy that situation by converting this columns values to the '1' or '-1' that we need
y = y.apply(lambda digit: "code here to transform the values of y to '1' or '-1'")

# set th weight values to an initial random value, along with 'w_save' which is the weight vector
# representing
w = w_save = pd.DataFrame(np.random.randn(1, x.shape[1]))

# what follows should be the pocket algorithm, use the perceptron as a guide but think
# carefully about the modifications that will be needed for it to function correctly
