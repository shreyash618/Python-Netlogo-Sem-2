## Shreya Shukla
## Intro CS2 pd 09
## HW # 17 : WhatFor?
## 2019--03--13

# Ask the user for two positive integers, and print all the odd integers on [a, b).
def posOdds ():
    a = int (input ('Enter a positive integer: '))
    b = int (input ('Enter another positive integer: '))
    
    for i in range (a, b) :
        if i % 2 == 1:
            print (i)
        
posOdds ()
#Test Run #1:     Enter a positive integer: 2 Enter another: 15
 #    3     5   7   9   11  13 (in seperate lines)

# Test Run #2:    Enter a positive integer: 9    Enter another: 1
 #    1     3   5   7


# reverses the characters in a string.
def reverseWord ():
    UserInput = str (input ('enter a word: '))
    reverse = ' '
    for i in UserInput:
        reverse = i + reverse
        if len (reverse) == len (UserInput) + 1 :
            reverse = reverse [: -1]
            print (reverse)

    if UserInput [::-1] == reverse :
        print ('It works!')
    else:
        print ('It does not work.')
        
reverseWord ()

# Test Case: enter word: stressed
#   desserts
#   It works.

# reads a word and prints the first letter that repeats. FOR LOOP VERSION
def firstRepeat ():
    UserInput = str (input ('enter a word: '))
    mylist = []
    repeat = 'no'
    for i in UserInput:
        if i in mylist:
            print (i)
            repeat = 'yes'
            break
        else:
            mylist = mylist + [i]
    if repeat == 'no':
        print ('No letter repeats')
    elif repeat == 'yes':
        print ('The first letter that repeats is', i)

firstRepeat ()

# Test case: enter word:  camel
#  No letter repeats.
#   enter word: mississippi
#  The first letter that repeats is s.


# reads a word and prints the first letter that repeats. WILD LOOP VERSION
def firstRepeat2 ():
    UserInput = str (input ('enter a word: '))
    mylist = []
    repeat = 'no'

    x = 0
    while x < len (UserInput):
        if UserInput [x] in mylist:
            print (UserInput [x])
            repeat = 'yes'
            break
        else:
            mylist = mylist + [UserInput [x]]
        x +=1
    if repeat == 'no':
        print ('No letter repeats')
    elif repeat == 'yes':
        print ('The first letter that repeats is', UserInput [x] )
firstRepeat2 ()
