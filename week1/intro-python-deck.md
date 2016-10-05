## General development setup

> Which python?

* Anaconda with python2.7

Anaconda bundles all of the libraries that we'll need for this class

Anaconda

---

###Alphabetical Order(to avoid flame war)
> IDE

* [Enthought Canopy](https://www.enthought.com/products/canopy/)

* [Ninja IDE](http://ninja-ide.org/)

* [PyCharm](https://www.jetbrains.com/pycharm/)

* [Rodeo](https://www.yhat.com/products/rodeo)

* [Wingware](https://wingware.com/)

---

> Text Editors

* [Atom](https://atom.io/)

* [Emacs](https://www.gnu.org/software/emacs/)

* [Sublime Text](https://www.sublimetext.com/)

* [Vim](http://www.vim.org/)

---

Regardless of which setup you land on, I would advise having the following at a minimum:

* Syntax Highlighting and syntax checking

* Code completion/autocomplete

* Module Awareness, can alert you when something is missing

---

Skills you need to master:

* Search,Search,Search!!!! - You must be able to quickly locate files and function definitions

* Debugging! You **must** be comfortable with your debugging setup.

---
##  Python

> We will be using Python 2.7.0

---

## Basic Math

```python
$ python

#addition
>>> 44 + 12
56

#subtraction
>>> 44 - 12

#multiplication
>>> 44 * 12
528

#division
>>> 44/12
3   #what the heck, should be 3.66....?

#exponentiation (44 to the power of 12)
>>> 44 ** 12
52654090776777588736L

```
---
## Strings
```python
>>> 'This is text content'
'This is text content'

#Better for text with apostrophe
>>> "So's this"
"So's this"

# Use quotes however you'd like
>>> "Cake \"and\" eat"
'Cake "and" eat'

```
---
## Boolean Comparisons

```python
# 10 is equivalent to 12
>>> 10 == 12
False

# 10 is greater than 12
>>> 10 > 12
False

# 10 is less than OR equal to 12
>>> 10 <= 12
True

>>> True and not (5 == 6)
True
```
---
## Assignment Statements

```python
# be careful not to confuse equivalence(==) with assignment(=)
>>> val = 12
>>> val
12

# don't do this iF you mean to assign a value to a variable
>>> val2 == 12
NameError: name 'val2' is not defined

# numeric values and strings are all fair game for
# assignment, objects too...but more on that later
>>> car  = 'Ford'
```
---
## Conditional Expressions

```python
# absolute value
>>> x = -11
>>> x if x > 0 else -x
11
```
---
## Sets

### Mathematically, a set in a unique unordered collection of items.

```python
# Let's see what this looks like in Python
>>> {'a', 'b', 'c'}
set(['a', 'c', 'b'])

# The set will only keep the unique items, discarding duplicates
>>>  {'a','a','c'}
set(['a', 'c'])

# Sets can have members of different types
>>> {'a',1+4,'d'}
set(['a', 'd', 5])
```
---
###some operations on Sets

```python
# sum over members
>>> s = {2,4,8}
>>> sum(s)
14

# test for membership, is 2 a member?
>>> 2 in s
True

# how about 3?
>>> 3 in s
False
```
---

```python
# set union, the unique numbers that appear in EITHER s or t
>>> t = {4,8,10}
>>> s | t
set([2, 4, 8, 10])

#set intersection, the unique numbers that appear in BOTH s and t
>>> s & t
set([8, 4])
```
---
### adding and removing members from a set

```python
# adding and removing a single member
>>> s = {7,8,9}
>>> s.add(10)
>>> s.remove(7)
>>> s
set([8, 9, 10])

# adding a set on an existing set
>>> s.update({11,22})
>>> s
set([22, 8, 9, 10, 11])

```
---
### set comprehensions

square every number in a set

```python
>>> s = {1,2,3}

# In words: for each item in the set s above,
#I'm going to assign to that item an arbitrary placeholder name of x,
#and square that item x, then put it in a new collection
>>> {x ** 2 for x in s}

set([1, 4, 9])
```
---

We can add  a condition to our comprehension as well.

```python
# square the item only if it's value is greater than 1
>>> {x ** 2 for x in s if x > 1}
set([9, 4])
```
---

Double comprehensions can be very useful as well

```python
# cartesian product
>>> {x*y for x in {1,2,3} for y in {4,5,6}}
set([4, 5, 6, 8, 10, 12, 15, 18])

# lets try it with a condition
>>> {x*y for x in {1,2,3} for y in {4,5,6} if y < 2*x}
set([12, 15])
```
---
## Lists

```python
>>> [1,4,5]
[1, 3, 5]

>>> [1, {2,4}, 'a', 3+5]
[1, set([2, 4]), 'a', 8]

# number of items in the list
>>> len([1,2,3])
3

```
---  
Adding lists together

```python
# the plus operator is a simple way to do this
>>> ['cat','dog']+ ['bird','squirrel']
['cat', 'dog', 'bird', 'squirrel']

#or we can use sum by providing '[]' as the second argument
sum([ [1,2,3],[4,5,6],[10,12] ],[])
[1, 2, 3, 4, 5, 6, 10, 12]
```
---

List comprehensions

```python
# we can construct a comprehension
# in the same way we did for lists
>>> l = [1,2,3,4]
>>> [x ** 2 for x in l]
[1, 4, 9, 16]
```
---
###list indexes,slices,prefixes, and suffixes

> indexing into a list

```python

# it's important to understand that list indices start at 0
>>> l = [1,2]

#grab the first item in the list
>>> l[0]
```
---
> slicing an array

```python
>>> l = ['a','b','c','d','e','f','g']

#grab items from the third to the fourth(5 is our non inclusive stop)
>>> l[2:5]
['c', 'd', 'e']
```
---
> prefix access

```python
# the following says 'grab the first two items'...
# and NOT 'grab all the items up to the 2nd index..
# which would be items in positions 0,1,2
>>> l[:2]
['a', 'b']
```
---
> suffix access

```python
#return everything but the first two items
>>> l[2:]
['c', 'd', 'e', 'f', 'g']
```
---
## Unpacking

accessing list elements based on index:

```python
#note, left hand side is not a list
[a,b,c] = [1+2,2+3,3+4]
>>> a
3
>>> b
5
```
---
Unpacking a list with a comprehension

```python

>>> nested_list = [[3,4],[5,6],[7,9] ]
>>> [y for [x,y] in nested_list]
[4, 6, 9]
```
---
list access and mutation

```python
>>> alist = [2,6,4]
>>> alist[1]
6
>>> alist[1] = 3
>>> alist
[2, 3, 4]
```
---
##Tuples

tuples are **immutable** sets, therefore they can be elements of sets

```python
#defining a tuple, a tuples uniqueness is determined
#by considering all of it's members
>>> (1,4,2*4)
(1, 4, 8)
>>> {1, (0,1)} | {5, (1, 2, 3)}

>>> {1, (0,1)} | {5, (0, 1 )}
set([(0, 1), 1, 5])
```
---
## Zip

A zip is constructed by taking one element from each of the input collections, providing that the collections are of the same length

```python

# element wise multiplication of two list
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> [x*y for (x,y) in zip(x,y)]
[4, 10, 18]

```
---
## Dictionaries

```python
# define a dictionary
>>> dict  = {'a': 'first letter', b:'second letter'}

#retrieve the value for the key of 'a'
>>> dict['a']
'first letter'

# testing if a key is present in the dictionary
>>> 'c' in dict
False
```
---
```python
# we can add to a dictionary
>>> mydict['c'] = 'third letter'
>>> mydict['c']
'third letter'

# we can also mutate the value of a key
>>> mydict['a'] = 'first letter in word apple'
>>> mydict['a']
'first letter in word apple'

# creating a dictionary with a comprehension
>>> dict =  {k:v for (k,v) in [('a','first'),('b','second')]}
>>> dict
{'a': 'first', 'b': 'second'}
```
---
Iterating over dictionaries

```python
# using the 'dict' dictionary created above, iterate over just the keys
>>> ['letter ' + k for k in dict.keys()]
['letter a', 'letter b']

# iterate over just the values
>>> [v + ' in alphabet' for v in dict.values()]
['first in alphabet', 'second in alphabet']

# iterate over the items, looking at each pair
>>> [k + ' is the ' + v for (k,v) in dict.items()]
['a is the first', 'b is the second']

```
---

## Functions

Functions map a set of inputs to an output, they are a fundamental building block of programming languages

```python
# hit enter twice in the interpreter after defining the function
>>> def greet(name): return 'Hello ' + name  
>>> greet('cat')
'Hello cat'
```
---
## Loops and conditionals

```python
# python delineates functions based on whitespace,
# so you must be careful to indent each line properly,
# either at least one space from the line above or a
# tab(and yes if you watch Silicon Valley on HBO this is
# the argument Richard gets into with his girlfriend.....'spaces or tabs?')
>>> for x in [1,2,3,5]:
...   if x < 2 or x > 3:
...     print(x)
...
1
5

```
---

```python
>>> vec1 = [1,2,5,7]
>>> vec2 = [4,3,5,8]
>>> match_found = False
>>> i = 0
while not match_found:
   if vec1[i] == vec2[i]:
     print("match of: " + str(vec1[i]))
     match_found = True
     break
   i++  
```
---
## Essential Libraries

* Numpy
* Pandas
* Matplotlib
* Scipy
* Sci-kit learn

###We'll look at Numpy, Pandas, and Matplotlib for this class
---

### Numpy

> Numpy is a python library for dealing with arrays and operations on those arrays.
 It provides a very convenient syntax

---
#### Array Representations

```python

>>> import numpy as np
>>> x = np.array([10, 11, 12], dtype=np.float32)
>>> x
array([ 10., 11., 12.], dtype=float32)

>>> y = np.array([10, 11, 12])
>>> y
array([10, 11, 12])
```
---

Consider carefully the difference between these two representations and their consequences

```python
>>> y[0]/20
0
>>> x[0]/20
0.5  
#conclusion: know whether you are using integers or floats
```
---

#### Element-wise operations

### Consider taking the dot product of the two arrays **x**, and **y** from the previous section.

```python
>>> np.dot(x,y)
365.0


```

###Yes, it’s that easy! We will make extensive use of this.

---

#### Array shaping and slicing
Consider again the array we started with: **x**

```python
>>> z = np.array([1, 2, 3,4,5,6,7,8,9], dtype=np.float32)
>>> z.shape
(9,)
````
---
Indexing along one dimension

```python
>>> z[0]
1.0
>>> z[8]
9.0
>>> z[9]
Traceback (most recent call last):
 File "\<stdin\>", line 1, in <module>
IndexError: index 9 is out of bounds for axis 0 with size 9
```
---

What happens if we change the dimensionality of z? Say by giving it 3 dimensions instead of 1?

```python
>>> grid = z.reshape(3,3)
>>> grid
array([[ 1., 2., 3.],
 [ 4., 5., 6.],
 [ 7., 8., 9.]], dtype=float32)
>>> grid[1,1]
5.0
>>> grid[8]
Traceback (most recent call last):
 File "\<stdin\>", line 1, in <module>
IndexError: index 8 is out of bounds for axis 0 with size 3
```
---

### Pandas

> Pandas is a library that allows you to work with *series* and *dataframes*. It is a particularly convenient way to work with and group data.

---
Series are one dimensional objects like arrays.
```python
>>> import pandas as pd
>>> d = pd.Series(index = range(6), data=[3,5,23,45,69,8])
>>> d
0 3
1 5
2 23
3 45
4 69
5 8
```
---

The important thing to keep in mind when working with Pandas is that you need to provide a sortable
index. Take the following example

```python
>>> d2=pd.Series(index = [’a’,’b’,’c’,’d’,’d’],data=[2,4,6,8,10])
>>> d2
a 2
b 4
c 6
d 8
d 10
```
---
We can then access the data in a few ways

```python
>>> d2.a #index by the index key
2
>>> d2.d
d 8
d 10
>>> d2.iloc[0] #positional indexing
2
>>> d2.iloc[:2]
a 2
b 4
```
---
Dataframes are particularly useful in Machine Learning because lots of data comes in spreadsheet form,
where we have rows of ‘X’ values, where one column is the ‘Y’ value.

```python
>>> f = pd.DataFrame({ ‘zip code’: [92646, 91023, 98768], ‘age’: [24,52,32], ‘party-affiliation’:[‘R’,’D’,’I’] })
0
1
2
3
```
---
### Matplotlib

> Matplotlib is the defacto visualization library for python. Many different kinds of graphics can be generated

---
Let’s plot something using numpy. We’ll see how we can

```python
# calculate the sign for the range of number 1:99
>>> sin=np.sin(np.array(range(1,100),dtype=np.float32) )
>>> pl.plot(sin)
>>> pl.show()
```
---
### Jupyter Notebooks (formerly Ipython)

```bash
$ ipython
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```
