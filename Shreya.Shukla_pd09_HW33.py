# Shreya Shukla
# Intro CS2 pd 09
# HW33: Filter, Reduce
# 2019--04--30

from functools import reduce

def filterOdd ():
    '''Takes in a range of values.
Returns a list with all the even integers in that range.'''
    L = range (int(input('Enter lower bound for range: ')), int(input('Enter higher bound for range:  ')) + 1)
    return list(filter (lambda x: x % 2 == 0, L))

# Test Cases
# Enter lower bound for range: 0
# Enter higher bound for range:  6
# Result: [0, 2, 4, 6]

# Enter lower bound for range: -6
# Enter higher bound for range:  2
# Result : [-6, -4, -2, 0, 2]

def AllTogetherNow (L):
    '''Takes a list.
Joins the items of the list and returns them as a string.'''
    return reduce((lambda x, y: x + y), L)

print (AllTogetherNow (['Testing ', 'shows ', 'the ', 'presence',
                        ', ','not ', 'the ', 'absence ', 'of ', 'bugs']))
# should return 'Testing shows the presence, not the absence of bugs.'

print (AllTogetherNow (['You ', 'are ' , 'a ', 'sad, ', 'strange ', 'little ', 'man ',
                        'and ', 'you ', 'have ', 'my ', 'pity. ','Farewell,']))
