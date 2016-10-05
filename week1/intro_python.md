## General development setup

The first step is download and install the [anaconda python distribution](http://www.continuum.io/downloads), version 2.7. This will setup all of the necessary libraries to get stated doing serious work in python. The anaconda distribution is available for all major platforms.

The next thing to consider is the question of an IDE(Integrated Development Environment) or text editor.

The following list is arranged in alphabetical order so as to alleviate any concerns that the author may be giving preferential ranking to any of the options, and therefore is not engaging in the holiest of programming wars(one’s choice of editor).

> IDE

* [Enthought Canopy](https://www.enthought.com/products/canopy/)

* [NinjaIDE](http://ninja-ide.org/)

* [PyCharm](https://www.jetbrains.com/pycharm/)

* [Rodeo](https://www.yhat.com/products/rodeo)

* [Wingware](https://wingware.com/)

> Text Editors

* [Atom](https://atom.io/)

* [Emacs](https://www.gnu.org/software/emacs/)

* [Sublime Text](https://www.sublimetext.com/)

* [Vim](http://www.vim.org/)

Regardless of which setup you land on, I would advise having the following at a minimum:

* Syntax Highlighting and syntax checking

* Code completion/autocomplete

* Module Awareness, can alert you when something is missing

Skills you need to master:

* Search,Search,Search!!!! - You must be able to quickly locate files and function definitions

* Debugging! You **must** be comfortable with your debugging setup.
---
# Python Tutorial

The following are examples of much of the important python you will need to know(including libraries), when working in Machine Learning or Data Science.  

Of course these examples are not exhaustive of absolutely *everything*, but rather try to include a good outline of the basics.


### Starting python

When python starts you will see the **>>>** prompt. This is where we will enter statements
for the python interpreter to execute.

#### Unix(OS X, Linux)

At the terminal type python(for OSX you can launch the terminal by hitting command+spacebar and then by typing 'terminal' in the finder)

```bash
$ python
Python 2.7.12 |Anaconda 4.1.1 (x86_64)| (default, Jul  2 2016, 17:43:17)
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>>
```
#### Windows

You can type 'cmd' into the Cortana search to bring up the terminal on Windows. Alternatively you can type 'cmd' into the run box.

```bash
\> python
```
---
## Basic Math

As a language widely used in scientific computing, python has extensive numerical libraries and routines, here we will only look at the very basics.

```python
$ python

# addition
>>> 44 + 12
56

# subtraction
>>> 44 - 12
32
# multiplication
>>> 44 * 12
528

# division
>>> 44/12
3 #what the heck, should be 3.66....?

# exponentiation (44 to the power of 12)
>>> 44 ** 12
52654090776777588736L

```
---
## Strings

Strings are how we represent textual data in a programming language. The idea of a quoted series of characters, show below, is universal to almost all languages. Python does not think of this data numerically, and the math operations above do not work the same way.  

```python
>>> 'This is text content'
'This is text content'

# can't use double quotes
>>> "hello "someone""
   "hello "someone""
                  ^
SyntaxError: invalid syntax

# can mix ' with ""
>>> "So's this"
"So's this"

# use quotes however you'd like by escaping
>>> "Cake \"and\" eat"
'Cake "and" eat'

# adding strings
>>> "hello " + "world"
"hello world"

>>> "hello " / "world"
TypeError: unsupported operand type(s) for /: 'str' and 'str'

>>> "hello " * "world"
TypeError: can't multiply sequence by non-int of type 'str'
```
---
## Boolean Comparisons

Often it is *very* useful to be able to check whether some value is the same as another. We
do this with comparison operators.

```python
# 10 is equivalent to 12
>>> 10 == 12
False

# 5 is equivalent to 5
>>> 5 == 5
True

# 10 is greater than 12
>>> 10 > 12
False

# 10 is less than 12
>>> 10 < 12
True

# 10 is less than OR equal to 12
>>> 10 <= 12
True

# 10 is greater than OR equal to 12
>>> 10 >= 12
False

# *and* keyword signifies both statements should be true
>>> True and False
False

>>> True and not 5==6
True
```
---
## Assignment Statements

Assignment occurs when a *RHS*-right hand side value, is assigned to a LHS-left hand side target, sometimes called an *identifier*, or more commonly just a name. In the example directly below...you could read it as *x <- 12*, where the value 12 is being assigned to the variable x.

```python
# be careful not to confuse equivalence(==) with assignment(=)
>>> val = 12
>>> val
12

# don't do this if you mean to assign a value to a variable
>>> val2 == 12  # this is an equality check, not an assignment
NameError: name 'val2' is not defined

# numeric values and strings are all fair game for assignment, objects too...but more on that later
>>> car  = 'Ford'
```
---
## Conditional Expressions

A conditional statement is used to control the flow of programming. The code inside of the conditional block will only execute if the result of evaluating the conditional expression is true. *Remember*, blocks of code are defined in Python based on indentation.

```python
# a neat implementation of absolute value
>>> x = -11
>>> x if x > 0 else -x
11

# a conditional will evaluate to True or False
>>> if x == -11:
...    print(x)
...
-11
```
---
## Sets

Mathematically, a set in a collection of unique, unordered items.

```python
# let's see what this looks like in Python
>>> {'a', 'b', 'c'}
set(['a', 'c', 'b'])

# the set will only keep the unique items, discarding duplicates
>>>  {'a','a','c'}
set(['a', 'c'])

# sets can have members of different types
>>> {'a',1+4,'d'}
set(['a', 'd', 5])
```

### some operations on Sets

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

# set union, the unique numbers that appear in EITHER s or t
>>> t = {4,8,10}
>>> s | t
set([2, 4, 8, 10])

# set intersection, the unique numbers that appear in BOTH s and t
>>> s & t
set([8, 4])
```

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

### set comprehensions

It is useful to create another set out of the mutated values of another set.


For example, we might want to square every number in a set

```python
>>> s = {1,2,3}

# in words: for each item in the set s above, I'm going to assign to that item an arbitrary placeholder name of x, and square that item x, then put it in a new collection
>>> {x ** 2 for x in s}

set([1, 4, 9])
```

We can add  a condition to our comprehension as well.

```python
# square the item only if it's value is greater than 1
>>> {x ** 2 for x in s if x > 1}
set([9, 4])
```

Double comprehensions can be very useful as well
```python
# cartesian product
>>> {x*y for x in {1,2,3} for y in {4,5,6}}
set([4, 5, 6, 8, 10, 12, 15, 18])

# let's try it with a condition
>>> {x*y for x in {1,2,3} for y in {4,5,6} if y < 2*x}
set([12, 15])
```
---
## Lists

A list in python is comparable to the notion of an 'array' in other programming languages.

There are no restrictions on the items in a list, *order* is significant because we can access an item based on its position in the list.

```python
>>> [1,4,5]
[1, 3, 5]

>>> [1, {2,4}, 'a', 3+5]
[1, set([2, 4]), 'a', 8]

# number of items in the list
>>> len([1,2,3])
3
```
###list indexes,slices,prefixes, and suffixes

> indexing into a list

```python
# it's important to understand that list indices start at 0
>>> l = [1,2]

# grab the first item in the list
>>> l[0]
```

> slicing an array

```python
>>> l = ['a','b','c','d','e','f','g']

# grab items from the third to the fourth(5 is our non inclusive stop)
>>> l[2:5]
['c', 'd', 'e']
```

> prefix access

```python
# the following says 'grab the first two items'...and NOT 'grab all the items up to the 2nd index..
# which would be items in positions 0,1,2
>>> l[:2]
['a', 'b']
```

> suffix access

```python
# return everything but the first two items
>>> l[2:]
['c', 'd', 'e', 'f', 'g']
```


Adding lists together
```python
# the plus operator is a simple way to do this
>>> ['cat','dog']+ ['bird','squirrel']
['cat', 'dog', 'bird', 'squirrel']

# or we can use sum by providing '[]' as the second argument
sum([ [1,2,3],[4,5,6],[10,12] ],[])
[1, 2, 3, 4, 5, 6, 10, 12]
```

List comprehensions

```python
# we can construct a comprehension in the same way we did for lists
>>> l = [1,2,3,4]
>>> [x ** 2 for x in l]
[1, 4, 9, 16]
```

---
## Unpacking

accessing list elements based on index:

```python
# note: left hand side is not a list
# a,b,c and see are individual items, and NOT
# part of one list.
>>> a,b,c = [1+2,2+3,3+4]
>>> a
3
>>> b
5
```

Unpacking a list with a comprehension

```python
>>> nested_list = [[3,4],[5,6],[7,9] ]
>>> [y for [x,y] in nested_list]
[4, 6, 9]
```

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
## Tuples

tuples are **immutable** sets, therefore they can be elements of sets

```python
# defining a tuple, a tuples uniqueness is determined
# by considering all of it's members
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
# element wise multiplication of two lists
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> [x*y for (x,y) in zip(x,y)]
[4, 10, 18]
```
---
## Dictionaries

A dictionary is a data structure defined by *key* and *value* pairs. It works as you may suspect, similar to a dictionary, where you look up a word by it's name in order to retrieve its 'value' or 'meaning'.

```python
# define a dictionary
>>> dict  = {'a': 'first letter', b:'second letter'}

# retrieve the value for the key of 'a'
>>> dict['a']
'first letter'

# testing if a key is present in the dictionary
>>> 'c' in dict
False

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

Loops are the usual means of iteration over some collection of items in programming languages. Along with conditionals this provides for the facility of executing complicated logic.


```python
# python delineates functions based on whitespace,
# so you must be careful to indent each line # # # properly, either at least one space from the line above or a tab(and yes if you watch Silicon Valley on HBO this is the argument Richard gets into with his girlfriend.....'spaces or tabs?')
>>> for x in [1,2,3,5]:
...   if x < 2 or x > 3:
...     print(x)
...
1
5
```

while loops are also useful, *especially in a situation where you do not know the length of your collection or stream.*

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

These are the python libraries that you will absolutely be using day to day working in ML…..or…..uhhggg…do I have to say it???……..Data Science.

---
## Numpy

Numpy is a python library for dealing with arrays and operations on those arrays. It provides a very convenient syntax

#### Array Representations

Below we will specify the precision on the floating point numbers: 32 bits

```python
>>> import numpy as np

>>> x = np.array([10, 11, 12], dtype=np.float32)

>>> x
array([ 10., 11., 12.], dtype=float32)

>>> y = np.array([10, 11, 12])
>>> y
array([10, 11, 12])
```

Consider carefully the difference between these two representations and their consequences

```python
>>> y[0]/20
0

>>> x[0]/20
0.5
```

It is very important to realize that in python 2.7, and many dynamic programming languages, division does not default to floating point division. Awareness of this and its effects is very important as you do not want unexpected values in your numerical code.

#### Element-wise operations

Given the importance of things like linear algebra to numerical computing, numpy’s element-wise operations

on arrays proves to be especially useful.

Consider taking the dot product of the two arrays **x**, and **y** from the previous section.

```python
>>> np.dot(x,y)
365.0
```

Yes, it’s that easy! We will make extensive use of this.

#### Array shaping and slicing

Consider again the array we started with: **x**

```python
>>> z = np.array([1, 2, 3,4,5,6,7,8,9], dtype=np.float32)

>>> z.shape
(9,)
````

Above, numpy is telling us that our array has 9 elements along a single dimension, and only one index which runs from 0:8(remember array indices start at 0)

```python
>>> z[0]
1.0

>>> z[8]
9.0

>>> z[9]
IndexError: index 9 is out of bounds for axis 0 with size 9
```

You can think of z as running along a single dimension, a straight line, and our indices from 0 through 8 can pull out the elements of the array along that line.

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
IndexError: index 8 is out of bounds for axis 0 with size 3
```

We have created a new array *grid* by reshaping z from a line to a square essentially, giving it 3 rows of 3 columns each.


Matrix multiplication is direct with two numpy arrays

```python
# we'll create two square matrices
>>> n =  z.reshape(3,3)
>>> m = z.reshape(3,3)
>>> m * n
array([[  1.,   4.,   9.],
       [ 16.,  25.,  36.],
       [ 49.,  64.,  81.]], dtype=float32)
```
Easy!!(for a fun weekend/week/month, try implementing matrix multiplication in the C programming language-with bounds checks:)

---
## Pandas

Pandas is a library that allows you to work with *series* and *dataframes*. It is a particularly convenient way to work with and group data.

Series are one dimensional objects like arrays.

```python
>>> import pandas as pd
>>> import numpy as np

>>> d = pd.Series([3,5,23,45,69,8])

>>> d
0     3
1     5
2    23
3    45
4    69
5     8
dtype: int64

# numpy is also welcome to the party
>>> np.sum(d)
153
```

We can then access the data in a few ways

```python
>>> d[0]
3
>>> d.iloc[3]
45
>>> d.iloc[:2]
0    3
1    5
dtype: int64
```

Let's look at another example more realistic example using Dataframes

```python
>>> dates = pd.date_range('20160824', periods=8)
>>> dates
DatetimeIndex(['2016-08-24', '2016-08-25', '2016-08-26', '2016-08-27',
               '2016-08-28', '2016-08-29', '2016-08-30', '2016-08-31'],
              dtype='datetime64[ns]', freq='D')

>>> df = pd.DataFrame(np.random.randn(8,4), index=dates,columns=['APL','CAT','MSFT','AMZN'])
>>> df
                AMZN       APL      MSFT       CAT
2016-08-24  0.977701  0.626827  0.092562  0.665338
2016-08-25 -0.479462  0.936397  0.622918  2.669262
2016-08-26 -0.902339 -0.113534  0.534006 -0.608284
2016-08-27  0.643675 -3.022262  1.419254  0.298500
2016-08-28 -0.867178 -1.893478  0.497380  0.260983
2016-08-29  0.674422 -0.045431 -0.564568  0.695902
2016-08-30  0.493063 -0.352214 -0.164529  0.172528
2016-08-31  0.580986 -0.042730  0.472628  0.099552
```

#### Accessing data in the frame

```python
>>> df.columns
Index([u'AMZN', u'APL', u'MSFT', u'CAT'], dtype='object')

>>> df.values
array([[ 0.97770056,  0.62682653,  0.09256168,  0.66533826],
       [-0.47946154,  0.93639679,  0.62291818,  2.66926169],
       [-0.9023387 , -0.11353439,  0.53400597, -0.60828406],
       [ 0.64367534, -3.02226204,  1.4192545 ,  0.2985004 ],
       [-0.86717792, -1.8934784 ,  0.49737974,  0.26098303],
       [ 0.67442181, -0.04543117, -0.56456751,  0.69590161],
       [ 0.49306293, -0.35221402, -0.16452926,  0.17252779],
       [ 0.58098614, -0.04272962,  0.4726284 ,  0.09955228]])


>>> df.index
DatetimeIndex(['2016-08-24', '2016-08-25', '2016-08-26', '2016-08-27',
               '2016-08-28', '2016-08-29', '2016-08-30', '2016-08-31'],
              dtype='datetime64[ns]', freq='D')
>>> df.dtypes
df.dtypes
AMZN    float64
APL     float64
MSFT    float64
CAT     float64
dtype: object
```

Useful sorting of data

```python
# sort the column 'CAT'
df.sort_values(by='CAT')
                AMZN       APL      MSFT       CAT
2016-08-26 -0.902339 -0.113534  0.534006 -0.608284
2016-08-31  0.580986 -0.042730  0.472628  0.099552
2016-08-30  0.493063 -0.352214 -0.164529  0.172528
2016-08-28 -0.867178 -1.893478  0.497380  0.260983
2016-08-27  0.643675 -3.022262  1.419254  0.298500
2016-08-24  0.977701  0.626827  0.092562  0.665338
2016-08-29  0.674422 -0.045431 -0.564568  0.695902
2016-08-25 -0.479462  0.936397  0.622918  2.669262
```

Basic selection of data

```python
# grabbing a single column
>>> df['APL']
2016-08-24    0.626827
2016-08-25    0.936397
2016-08-26   -0.113534
2016-08-27   -3.022262
2016-08-28   -1.893478
2016-08-29   -0.045431
2016-08-30   -0.352214
2016-08-31   -0.042730
Freq: D, Name: APL, dtype: float64
# selecting a certain number of rows

>>> df[2:5]
                AMZN       APL      MSFT       CAT
2016-08-26 -0.902339 -0.113534  0.534006 -0.608284
2016-08-27  0.643675 -3.022262  1.419254  0.298500
2016-08-28 -0.867178 -1.893478  0.497380  0.260983

# grab first 5 rows
>>> df.head() # 5 is the default number
                AMZN       APL      MSFT       CAT
2016-08-24  0.977701  0.626827  0.092562  0.665338
2016-08-25 -0.479462  0.936397  0.622918  2.669262
2016-08-26 -0.902339 -0.113534  0.534006 -0.608284
2016-08-27  0.643675 -3.022262  1.419254  0.298500
2016-08-28 -0.867178 -1.893478  0.497380  0.260983


>>> df.tail(2) # grab the last 2, again 5 would be the default
                AMZN       APL      MSFT       CAT
2016-08-30  0.493063 -0.352214 -0.164529  0.172528
2016-08-31  0.580986 -0.042730  0.472628  0.099552
```

More advanced selecting

```python
# selecting more than one column
>>> df.loc[:,['APL','AMZN']] # the '1:3' means rows 1 through 3
                 APL      AMZN
2016-08-24  0.626827  0.977701
2016-08-25  0.936397 -0.479462
2016-08-26 -0.113534 -0.902339
2016-08-27 -3.022262  0.643675
2016-08-28 -1.893478 -0.867178
2016-08-29 -0.045431  0.674422
2016-08-30 -0.352214  0.493063
2016-08-31 -0.042730  0.580986


# selecting rows by specified date range
>>> df['20160824':'20160827']
                AMZN       APL      MSFT       CAT
2016-08-24  0.977701  0.626827  0.092562  0.665338
2016-08-25 -0.479462  0.936397  0.622918  2.669262
2016-08-26 -0.902339 -0.113534  0.534006 -0.608284
2016-08-27  0.643675 -3.022262  1.419254  0.298500

# we can combine both
# select the given range of rows, but only for the given columns
>>> df.loc['20160824':'20160827', ['APL','AMZN']]
                 APL      AMZN
2016-08-24  0.626827  0.977701
2016-08-25  0.936397 -0.479462
2016-08-26 -0.113534 -0.902339
2016-08-27 -3.022262  0.643675
```

Power tools: the *apply* function. You may need to ask certain questions about the data you have,
in the case of stocks, maybe you want to know the cumulative returns, or the maximum spread over the period.

```python
>>> df.apply(np.cumsum)  # the cumulative total over the range
                AMZN       APL      MSFT       CAT
2016-08-24  0.977701  0.626827  0.092562  0.665338
2016-08-25  0.498239  1.563223  0.715480  3.334600
2016-08-26 -0.404100  1.449689  1.249486  2.726316
2016-08-27  0.239576 -1.572573  2.668740  3.024816
2016-08-28 -0.627602 -3.466052  3.166120  3.285799
2016-08-29  0.046820 -3.511483  2.601553  3.981701
2016-08-30  0.539882 -3.863697  2.437023  4.154229
2016-08-31  1.120869 -3.906426  2.909652  4.253781

>>> df.apply(lambda x: abs(x.min() - x.max()))  # look at peak vs trough
AMZN    1.880039
APL     3.958659
MSFT    1.983822
CAT     3.277546
```

#### Time Series

Pandas started as a time series(think stock tick data) library on Wall Street, where data science was born(surprise! it wasn't silicon valley)

Let's have a quick look at some of the time series functionality in Pandas
```python
# create a time series range at the granularity of 1 second
>>> time  = pd.date_range('20160204', periods=200, freq='S')
>>> time
DatetimeIndex(['2016-02-04 00:00:00', '2016-02-04 00:00:01',
               '2016-02-04 00:00:02', '2016-02-04 00:00:03',
               '2016-02-04 00:00:04', '2016-02-04 00:00:05',
               '2016-02-04 00:00:06', '2016-02-04 00:00:07',
               '2016-02-04 00:00:08', '2016-02-04 00:00:09',
               ...
>>> time_series  = pd.Series(np.random.randint(0,500,len(time)),index=time)
>>> time_series.head()
2016-02-04 00:00:00    435
2016-02-04 00:00:01    486
2016-02-04 00:00:02    363
2016-02-04 00:00:03    315
2016-02-04 00:00:04    324
Freq: S, dtype: int64
```
We can resample the data at say 1MIN intervals

```python
>>> time_series.resample('1Min').sum()
2016-02-04 00:00:00    15024
2016-02-04 00:01:00    14832
2016-02-04 00:02:00    14583
2016-02-04 00:03:00     4378
Freq: T, dtype: int64
```

We can also adjust time_zone

```python
>>> ts_utc  = time_series.tz_localize('UTC')
>>> ts_utc.head() # notice +00:00
2016-02-04 00:00:00+00:00    435
2016-02-04 00:00:01+00:00    486
2016-02-04 00:00:02+00:00    363
2016-02-04 00:00:03+00:00    315
2016-02-04 00:00:04+00:00    324
Freq: S, dtype: int64

# convert from UTC to US/Eastern
>>> ts_eastern = ts_utc.tz_convert('US/Eastern')
>>> ts_eastern.head() # notice -05:00
2016-02-03 19:00:00-05:00    435
2016-02-03 19:00:01-05:00    486
2016-02-03 19:00:02-05:00    363
2016-02-03 19:00:03-05:00    315
2016-02-03 19:00:04-05:00    324
Freq: S, dtype: int64
```

#### Working with external data

We can easily save/read in our data

```python
# save data to new file 'test.csv'
>>> ts_utc.to_csv('test.csv')

# when reading in data, if you do not have a header row, it's
# important to specify 'header=None', otherwise by default pandas
# will think the first row of your data is the header, resulting in
# a data set that is missing one value
>>> data = pd.read_csv('test.csv',header=None)
>>> data.head()
                           0    1
0  2016-02-04 00:00:00+00:00  435
1  2016-02-04 00:00:01+00:00  486
2  2016-02-04 00:00:02+00:00  363
3  2016-02-04 00:00:03+00:00  315
4  2016-02-04 00:00:04+00:00  324
```
We can also easily work with excel files

```python
# let's save the data we just read in to an excel file
>>> data.to_excel('test.xlsx',sheet_name='test')

>>> excel_data = pd.read_excel('test.xlsx','test',header=None)
>>> excel_data.head()
````
---
## Jupyter Notebooks

You can start an interactive session of Ipython at the command line

```bash
# inside your directory run the following
$ jupyter notebook
```

We'll look at some basic functionality. Create a new notebook and
then add the following code

```python
import numpy as np


x  = np.array([1.,2.,3.])
````

> To execute a code cell: Type *shift + enter*

Let's look at a nice way to do inline plots


```python
# type the following into a new cell under the one above
import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(x)
plt.show()
````

You should see a graphic underneath the code cell

Another feature is tab completion

```python
# in another, or the same cell type the following,
# HIT TAB after typing the dot to see completions
plt.
```
---
## Matplotlib

Matplotlib is the de-facto visualization library for python. Many different kinds of graphics can be generated.

Let’s plot something using numpy. We’ll see how we can quickly put together a plot.

```python
# we will do all of the following from within jupyter notebook,
# same as above, make sure to import matplotlib and declare
# %matplotlib inline

# calculate the sign for the range of number 1:99
sin=np.sin(np.array(range(1,100),dtype=np.float32) )
plt.plot(sin)
plt.show()
```

Often for a good plot we want to give a little for textual
information as to what it is exactly we are showing. The following example is more in depth, and will
illustrate some common issues you will run into when actually trying to plot something that looks decent.


Let's first look at a straightforward plot of some return data, and see where matplotlib initially falls a bit
short.  **NOTE**- The following two plots will have different values for the actual lines drawn, this is because we
are generating the data randomly each time.

```python
import matplotlib.pyplot as plt

%matplotlib inline

# we going to create some fake simulated return for APL stock
dates = pd.date_range('20160824', periods=8)
df = pd.DataFrame(np.random.randn(8,4), index=dates,columns={'APL','CAT','MSFT','AMZN',})
apl_cumulative = df['APL'].apply(np.cumsum)


# set the plot with the data
plt.plot(apl_cumulative)


# here we'll create a nice label for the whole figure using string concatenation
plt.xlabel("APL cumulative returns " + str(df.index[0]) + " through " + str(df.index[-1]))

plt.show()
```

<img src="quiver-image-url/A77A19F819C20F415C66B28317FD2837.png" style="width:400px;height:350px" />

Below we add in code that will clean up our plot quite a bit and make it presentation worthy.

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

%matplotlib inline

# we going to create some fake simulated return for APL stock
dates = pd.date_range('20160824', periods=8)
df = pd.DataFrame(np.random.randn(8,4), index=dates,columns={'APL','CAT','MSFT','AMZN',})
apl_cumulative = df['APL'].apply(np.cumsum)

#we are going to look for days in our tick data
days =  mdates.DayLocator()

# we want the format to show up: 'month-day' only
daysFmt = mdates.DateFormatter('%m-%d')

# set the plot with the data
plt.plot(apl_cumulative)

# If we try to use the dates directly from our index to
# build a string to label our data, we will see that the string
# comes out looking like this:'2016-08-24 00:00:00',
# which is not a very nice looking format.
nice_dates = df.index.map(lambda x: x.strftime('%m-%d-%Y'))

# here we'll create a nice label for the whole figure using string concatenation
# notice the neat trick of a [-1] index to retrieve the last item from a python list
# tuck this trick away in your memory, you will likely need it often.
plt.xlabel("APL cumulative returns " + nice_dates[0] + " through " + nice_dates[-1])

# we are telling matplotlib what we are looking for in the labels
plt.gca().xaxis.set_major_locator(days)

# specify what the format should be when displaying the dates on the axis
plt.gca().xaxis.set_major_formatter(daysFmt)

# we strive for perfection, without this the x and y tick lables
# at the bottom left corner will be too close, this pushes the x-axis
# tick labels down a bit
plt.gca().tick_params(axis='x',pad=10)

plt.show()
```
<img src="quiver-image-url/8D813244580BE29E25CCA9B01CA2919E.png" style="width:400px;height:350px" />

---
## pdb - the python debugger

As stated in the introduction, debugging is **absolutely critical** to becoming a decent programmer, so we've saved the best for last.

First let's create and save a file in the current directory we are in. Use your favorite IDE/text editor to add the following to the file:

> say_hello.py

```python
def say_hello(name):
   print name

name = 'Angela'
say_hello(name)
```
At the *(Pdb)* prompt we can use various control statements to *step* through our
code and gain insight into what is going on at the time of execution.

> Basic control flow statements

* *next* - execute the current statement, move cursor to next statement
* *print* - use with a variable name to print out the value of that variable
* *continue* - stop debugging but let the program finish running
* *list* - show the area of the source code currently being executed


Now, at the command line we can use pdb to run the file

```bash
# the '-m' is the module switch, you are
# telling python to run the pdb module
$ python -m pdb say_hello.py
```

This will run the *test_pdb.py* file using the debugger

```python
$ python -m pdb test_pdb.py
> /Users/you/say_hello.py(1)<module>()
-> def say_hello(name):

(Pdb) <you can type control statements here>
```

Go a head and step all the way through the code

```python
# type next once and then keep pressing enter
# to step all the way through the code
# if you don't give Pdb a new command, hitting enter
# will execute the last command
(Pdb) next
```

OK, that was great.....I just ran the program a lot slower than normal,
but what's the point?

To understand the real value of pdb, we are going to have to look at a more complicated example. In the same folder, create and save the following file

> iteration_test.py

```python
import say_hello as say

for x in range(10):
    for i in range(10):
        if i==10:
            print say.say_hello(i)
```

The above code listing is a *loopdee-loop*(an unofficial term for a nested, or loop within a loop, I believe the term originated in the roller coaster industry).

Basically what the code will do is the outer loop will execute 10 times, and **each time** the outer loop executes, the inner loop will execute 10 times, for a total of 100 loop executions.

What we expect is that our *say_name* function will only print **i** when **i** is 10. Let's run our code and see what happens

```python
$ python iteration_test.py
Angela
```

We are not seeing what we expect, which is i printing 10 times. Let's try to find out what's going on.

Arguably the most critical debugging capability is being able to set conditional breakpoints, in other words, the ability to stop code execution when a variable has a particular value.

In our case, ideally we would like to stop execution when *i==10*, to figure out what's going wrong.

```python
$ python -m pdb iteration_test.py

# below we set the breakpoint at line 6,
# conditional on when i is 10
(Pdb) break 5, i==10
Breakpoint 1 at /Users/erin/iteration_test.py:6

# by typing continue, the program will execute until
# it hits our breakpoint
(Pdb) continue
Angela
The program finished and will be restarted
> /Users/erin/iteration_test.py(1)<module>()
-> import test_pdb
```

Okay what gives? The program just finished without stopping which doesn't seem right.

What happens if we set the breakpoint for **i==9**?

```python
$ python -m pdb iteration_test.py

(Pdb) break 5, i==9
Breakpoint 1 at /Users/erin/iteration_test.py:6
(Pdb) continue

# these two lines that pdb prints out show us where
# execution has stopped at
> /Users/erin/iteration_test.py(5)<module>()
-> if i==10:

# type i and hit enter to print out the value of i
(Pdb) i
9
```

This is where logic kicks in, we are clearly getting to 9 in our loop but not 10, so why is that? If we were to look up the specification of the *range()* function in python, we would see that the range is up to, but not including the number we pass to it. So in the case of our code: range(10), this actually returns 0 through 9, which *is* a range of 10 numbers.

We could fix our code like the following:

```python
import say_hello as say

for x in range(10):
    for i in range(10):
        if i==9:
            print say.say_hello(i+1)
```

Now let's see what happens when we run it again

```python
$ python iteration_test.py
Angela
10
None
10
None
10
None
10
None
10
None
10
None
10
None
10
None
10
None
10
None
```

Great! We see 10 printed 10 times as we would like, however there is that odd 'Angela' being printed once at the very beginning.  Now we may already know where that is coming from, but if we didn't, it's good to know about one of pdb's more useful features, being able to step into external modules that are being imported into the code you are executing.
Let's see how we can step into and debug code in an external module that our code is using.
```python
$ python -m pdb iteration_test.py

# we must first import the module into pdb
(Pdb) import say_hello

# immediately we see that Angela is printed out
Angela

# we can set a breakpoint at line 2 of the say_hello module
(Pdb) b say_hello:2
Breakpoint 1 at /Users/erin/say_hello.py:2

# hitting continue we will see that execution stops at
# -> print name
(Pdb) continue
> /Users/erin/say_hello.py(2)say_hello()
-> print name

# typing name shows that it is 10, and if we continue
# hitting enter we will see that each time the program
# execution stops, name is 10, which does indeed verify
# that our code is working properly
(Pdb) name
10
```

As we noticed, 'Angela' is being printed immediately, and only at the time of import, which is explainable by the fact that the following lines are only executed once, when
the module is loaded.

```python
# this functionality is hard coded, meaning we
# are creating a specific name, and then invoking
# the function. This only happens once, as subsequently
# we call the function say_hello with a different name each time

name = 'Angela'
say_hello(name)
```

We have now seen how to step though our code at execution time and examine the value of variables, and also how to set conditional breakpoints, and even breakpoints in modules that our code will load. These are powerful tools for debugging that need to be mastered.
