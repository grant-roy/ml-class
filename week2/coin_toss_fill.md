## The goal of this exercise is to fill in the code blanks

The comment lines, marked with a preceding '#', indicate where code is missing that you will need
to fill in.

When you complete the following two functions, you should be able to run the code listing below and see
the output in the console.

> Strategies

* Try putting the entire code listing in a file named *coin_experiment.py*
and run that file from the command line. Read the error messages **very** carefully
* Cross-reference the parameters(inputs) of a function with how the function is being called
* Google is your friend, and specifically StackOverflow

> coin_experiment.py

```python
import random
from random import randint


def flip_coin():
    # missing implementation of a function that has a 50/50 chance of
    # returning an 'h' for heads or a 't' for tails


def run_experiment(num_flips,
                  # missing input parameter,
                   num_experiments):
    results = []
    head_count_coins = []
    #missing outer loop for how many experiments we will conduct
        for coin in range(num_coins):
            flips = [flip_coin() for i in range(num_flips)]
            # missing count variable of the number of heads, how do we get the percent heads in 'flips'?
            head_count_coins.append(count)

        results.append({'v1': head_count_coins[0], # 'v1' represents picking the first coin
                        # missing variable 'v_rand' that represents picking a random coin
                        # missing  variable'v_min' that represents picking the coin with the lowest distribution of heads
                        })
        head_count_coins = []

    return # missing return value

print(run_experiment(10,1000,1000))    
```

After building up the preceding two functions we can plot the results to gain insight into our data. For this code listing, the only thing you will need to do is implement the calculation for the Hoeffding inequality

> plotting.py

```python
import math
import matplotlib.pyplot as plt

def show_results(results):
    '''
       fig.add_subplot: arg1 is the number of rows
                        arg2 is the number of columns
                        arg3 is the individual plots order

       fig_obj.hist:    arg1 is the data to plot
                        arg2 is the number of bins to group the data in,
                        best to calculate this explicitly based on the data
                        arg3 is the color you would like the plot to appear in
    '''
    fig = plt.figure()

    a = fig.add_subplot(311)
    v1 = [result['v1'] for result in results]
    a.hist(v1, bins=sorted(set(v1)), color='blue')
    a.set_xlim([0, 1])
    a.set_title("picking the first #heads result from each trial")

    b = fig.add_subplot(312)
    v_rand = [result['v_rand'] for result in results]
    b.hist(v_rand, bins=sorted(set(v_rand)),  color='red')
    b.set_xlim([0, 1])
    b.set_title("picking a random #heads result from each trial")

    c = fig.add_subplot(313)
    c.hist([result['v_min'] for result in results], color='green')
    c.set_xlim([0, 1])
    c.set_title("picking the minimum #heads result from each trial")

    plt.tight_layout()

def show_prob_bounds(N):
    if len(N) != 3:
        raise Exception("pass a list or tuple for N of length 3")

    error_range = [x * .01 for x in range(1, 31)]

    fig = plt.figure()
    a = fig.add_subplot(311)

    a.plot(error_range, [hoeffding(N[0]) for error_term in error_range])
    a.set_title("N=" + str(N[0]))

    b = fig.add_subplot(312)
    b.plot(error_range, [hoeffding(N[1]) for error_term in error_range])
    b.set_title("N=" + str(N[1]))

    b = fig.add_subplot(313)
    b.plot(error_range, [hoeffding(N[2]) for error_term in error_range])
    b.set_title("N=" + str(N[2]))

    plt.tight_layout()


''' results is 10000 coins, each flipped 10 times, fraction of heads '''
def show_bounds_vs_experiment(results, epsilon, u, times_coin_tossed):

    hoeffding = 2 * math.e ** (-2 * (epsilon ** 2) * times_coin_tossed)
    fig = plt.figure()

    a = fig.add_subplot(311)
    v1_vs_u = [abs(fraction_heads["v1"] - u) for fraction_heads in results]
    a.plot(v1_vs_u)
    a.set_title("|v1 - u|")

    print("Probability bound given by Hoeffding inequality for N=" + str(times_coin_tossed) + ": " + str(hoeffding))
    print("Percentage of times |v1 - u| is greater than epsilon: " +
          # create list of results where: fraction of heads > epsilon
          # divide the length of that list(num of items) by the length of results to get a percentage
          # we need to type cast the length to float so that division gives a decimal, then cast the whole
          # expression to a string so that we can print it.
          str(float(len([fraction for fraction in v1_vs_u if round(fraction, 1) > epsilon]))/len(results)))

    b = fig.add_subplot(312)
    v_rand_vs_u = [abs(fraction_heads["v_rand"] - u) for fraction_heads in results]
    b.plot(v_rand_vs_u)
    b.set_title("|v_rand - u|")

    print("Percentage of times |v_rand - u| is greater than epsilon: " +
          str(float(len([fraction for fraction in v_rand_vs_u if round(fraction, 1) > epsilon]))/len(results)))

    c = fig.add_subplot(313)
    v_min_vs_u = [abs(fraction_heads["v_min"] - u) for fraction_heads in results]
    c.plot(v_min_vs_u)
    c.set_title("difference between epsilon and v_rand-u")

    print("Percentage of times |v_min - u| is greater than epsilon: " +
          str(float(len([fraction for fraction in v_min_vs_u if round(fraction, 1) > epsilon])) / len(results)))

    plt.tight_layout()



def hoeffding(n):    
    # implementation of hoeffding calulation goes here
```
## Jupyter Notebook

Now we can put everything we have together in a Jupyter Notebook

Open a terminal in the directory you have placed the above two files

```bash
# now type
$ jupyter notebook
```
Place the following in an **In[1]:** cell

```python
import coin_toss_p as ct
import coin_toss_p as ct
import plotting as pl

%matplotlib inline
results = ct.run_experiment(10,1000,1000)
pl.show_results(results)
```
