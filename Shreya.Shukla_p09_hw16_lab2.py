# Shreya Shukla
# IntroCS2 pd 09
# Labwork 2 (HW 16)
# 2019--03--12

# TASK 1: Prints a w * h rectangle of *
w = int (input ("enter width: "))
h = int (input ("enter height: "))

print (h * ("*" * w + "\n")) ## print h lines, with w asterisks in each line 

## if w = 3 and h = 4, then you should get:
##   * * *
##   * * *
##  * * *
##   * * *

# TASK 2: Prints a n by n checkerboard of repeating -* where lines start with alternating characters
# ie: if line 1 starts with -*, line 2 starts with *-

n = int (input ("enter a postive #: "))

if n % 2 == 0:
    print ((n/2) * ("-*" * (n/2) + "\n" + "*-" * (n/2) + "\n")) # if n is even, print 2 lines, with
    # alternating start characters (-* and *-), n/2 times
elif n % 2 == 1:
    print (
        ((n//2) *
        ("-*" * (n//2) + "-" + "\n" + "*-" * (n//2) + "*" + "\n"))
          + "-*" * (n//2) + "-" + "\n" )
# if n is odd, print 2 lines with alternating start characters (-* and *-), n/2 times,
# and print a additional line.

# Test Case: enter a positive #:10 should print
#  -*-*-*-*-*
#  *-*-*-*-*-
#  -*-*-*-*-*
#  *-*-*-*-*-
#  -*-*-*-*-*
#  *-*-*-*-*-
#  -*-*-*-*-*
#  *-*-*-*-*-
#  -*-*-*-*-*
#  *-*-*-*-*-


# TASK 3: Writes a script to simulate tossing a fair coin n times. Then determines the longest consecutive sequence of tails and heads.
import random
flipCoin = lambda : random.choice(['H','T']) # gives heads and tails a equal chance of occuring

NumOfTosses = int (input ("enter a # to flip a coin n times: ")) ## takes input for how many tosses
side = 0 ## creates a variable, side
memory = [] ## creates a variable / list that stores all the results of each toss
hList = tList = [1] ## creates two lists, which start off with the value 1 and store the values of each
## streak. hList stores the streaks for heads and tList stores the streaks for tails

hStreak = tStreak = 1 ## creates two variables, which store the duration of each streak for heads and tails, respectively

while NumOfTosses > 0: ##while the number of tosses left is still greater than 0
    side = flipCoin () ## side gets a value- heads or tails
    
    memory += side ## memory stores the current side, adding it to the list of previous outcomes
    
    if side == memory [ len (memory) - 2] and len (memory) > 1: ## if the side matches the last outcome
        ## ie- if side is Heads, and the last toss also yielded heads, then this condition is true
        if side == memory [ len (memory) - 3] and len (memory) >= 3: ## if this is a ongoing streak

            if side == 'T':
                tStreak += 1
            elif side == 'H':
                hStreak += 1
                ## adds one to the corresponding streak
                
        else: ## if this is a new streak, meaning the previous streak broke
            if side == 'T':
                hList = [hStreak] + hList ## the previous streak gets stored in a list corresponding to its side
                hStreak = 1 ## the streak value for the other side gets set to default, which is 1
                tStreak += 1 ## the current streak gets updated by 1
                
            if side == 'H': ## same as above
                tList = [tStreak] + tList
                tStreak = 1
                hStreak += 1
                
    elif side != memory [len (memory) -2]: ## if there is no streak, meaning the current side does
        ## not match the previous outcome
        ## all streaks get stored in lists, and then broken
        tList = [tStreak] + tList
        hList = [hStreak] + hList
        ## the streak values get set to default
        tStreak = 1
        hStreak = 1
                
    NumOfTosses += -1 ## recursive part of while loop, number of tosses remaining decrease with each new toss

tList = [tStreak] + tList
hList = [hStreak] + hList

print (memory)
print ('The longest sequence of "T" is ', (max (tList))) ## prints the max streak value for tails
print ('The longest sequence of "H" is ', (max (hList))) ## prints the max streak value for heads

## something like enter # of trials: 7 would return
## 'HHTHTTT'
## The longest sequence of H: 2
## The longest sequence of T: 3

