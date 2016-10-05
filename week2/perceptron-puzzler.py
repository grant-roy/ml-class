## Perceptron Puzzle

---

```python
# iterate through all the rows of x
for index, row in x.iterrows():
```

---

```python
# initialize a flag to tell us whether or not we have a missclassified point
misclassified = 1

while misclassified != 0:

    misclassified = 0
```

---
```python
# create the scalar vector of '1's..this is the bit of trickery that let's us turn our summation into
# a convenient dot product. we will add this as a column along with 'size' and 'mass' from our coin data
# this will allow us to match the three columns our weight vector will have
scalar = pd.Series([1] * len(coin_data), name='scalar')
```

---

```python
# we will create our y vector, y is the corresponding correct classification for each row of data
y = coin_data['classification']
```

---
```python
# here we will check that the signs of our actual data(in 'y') match the result
# of our multiplication of the weight vector 'w' and our row, which is a row from 'x' our
# data set.
if np.sign(y[index]) != np.sign(y_hat):
```
---
```python
# what this does is return a vector of random weights that matches the length of x. so in our case
# because x is length 3, we want a weight vector of 3 numbers as well so we can take the dot product
w = pd.DataFrame(np.random.randn(1, x.shape[1]))
```
---

```python
# import statements for the libraries we'll be using
import pandas as pd  # pandas gives us a data frame, which is a powerful tool for manipulating data
import numpy as np   # numpy is a powerful numerical library we will use for vector operations
```
---

```python
# keep track of how many points are missclassified
misclassified += 1
```
---

```python
# we adjust our weight vector 'w' by adding the result of y[index]*row to 'w'
w = np.add(w, y[index]*row.values)
```

---
```python
# create our x vector with the added scalar column
x = pd.concat((scalar, coin_data.loc[:, ['size', 'mass']]), axis=1)
```

---

```python
# iterate through all the rows of x
for index, row in x.iterrows():
```

---

```python
# read in the coin-data from an excel file
coin_data = pd.read_excel('coin-data.xlsx', 'coin-data', header=0)
```
