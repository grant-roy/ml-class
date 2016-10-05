## Comprehensions

1) Use a list comprehension to calculate the sign for the numbers 1:10

Answer:

```python
from math import sin

[sin(x) for x in range(1,10)]
```

2) Create a function with signature: *sequential_row(start, length)*

* example: sequential_row(10, 4) should return: [10,11,12,13]

```python
def sequential_row(start, length):
    return range(start, start + length)
```

3) Create a function with siganture: *tuple_sum(A, B)*
For each pairs of tuples in lists A and B, add the first element of each tuple,
and then the second element of each tuple
* example: A = [(2,10)(4,20)], B = [(1,2),(3,4)]
  tuple_sum(A,B) should return: [(6,30), (4,6)]

```python
A = [(2, 10), (4, 20)]
B = [(1, 2), (3, 4)]

def tuple_sum(A, B):
    return [map(sum, zip(x, y)) for x, y in zip(A, B)]

    # see below for a somewhat more intuitive idea of the operations taking place,this
    # will work of course only for tuples of length 2
    # [(x[0] + y[0], x[1] + y[1]) for x, y in zip(A, B)] # zip is needed to pair up A and B
```

4) Create a function that will sum all of the odd numbers in a list
* example [1, 2, 3, 4, 5, 6, 7, 8, 9] should return:
 25

```python
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_odds(A):
    return sum([x for x in A if x % 2 != 0])
```


5)  Given a dictionary `d = {'h':'e','e':'a','l':'r','l':'t','o':'h'}`, Create
a function that will output the concatenation of all the keys and all the values
in a sentence
* example output for d should be: `'hello earth'`

```python
d = {'o': 'e', 'r': 'a', 'b': 'r', 'i': 't', 't': 'h'}

def concatenate_kv(d):

    keys = [k for k in d.keys()]
    values = [v for v in d.values()]
    m1 = str.join('', swap(swap(keys, 0, len(keys)-1), len(keys)-2, len(keys)-1))
    m2 = str.join('', swap(swap(values, 0, len(values)-1), len(values)-2, len(values) - 1))
    print(m1 + ' ' + m2)


# switch positions of first and last, and second two last of both words
def swap(c, i, j):
    c[i], c[j] = c[j], c[i]
    return c
```

## Numpy

1)

2)

3)

4)

5)

## Pandas

1)

2)

3)

4)

5)

## Matplotlib

1)

2)

3)

4)

5)