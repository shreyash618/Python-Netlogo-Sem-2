# Shreya Shukla
# Intro CS2 pd 09
# HW 27: MapsMaps
# 2019-04-08

import random

def mymap(f, L):
    '''Assume f is a function and L is a list.
Returns a list.'''
    print (list (map (f, L)))

mymap (lambda x: x **2, [0, 3]) # should print [0, 9]
mymap(lambda x: x**2, [1,2,3])## should print [1, 4, 9]
mymap(lambda s: len(s) , ['cat' , 'frog']) # should print [3,4] 

def random_list (n, limit):
    '''Takes into two non-negative numbers: n and limit.
Returns a list of n random integers in the range [0, limit).'''
    print (list (map (lambda n: random.choice (range (0, limit)) , range (0, n))))

random_list (4, 9) # should return 4 random numbers >= zero and < 9
random_list (2, 7) # should return 2 random numbers >= zero and < 7
random_list (1, 8) # should return 1 random number >= zero and < 8
random_list (0, 0) # should return empty set

def bar_graph (L):
    '''Takes a list of non-negative integer values.
Returns a string of a bar graph representation of the data. '''
    print ('\n'.join (list (map (lambda n: str(n) + ': ' + L[n] * '=', range (0, len (L))))))

bar_graph ([3,2,4,5, 6])
bar_graph ([2,3,4])
