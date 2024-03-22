# Shreya Shukla
# IntroCS2 pd 09
# Labwork 2 (HW 16)
# 2019--03--12

# TASK 1: Prints a w * h rectangle of *
w = int (input ("enter width: "))
h = int (input ("enter height: "))

print (h * ("*" * w + "\n"))

# TASK 2: Prints a n by n checkerboard of repeating -* where lines start with alternating characters
# ie: if line 1 starts with -*, line 2 starts with *-

n = int (input ("enter a postive #: "))

if n % 2 == 0: ## if n is even
    print ((n/2) * ("-*" * (n/2) + "\n" + "*-" * (n/2) + "\n")) ## print a even number of * and- in each line

elif n % 2 == 1: ## if n is odd
    print (((n//2) * ("-*" * (n//2) + "-" + "\n" + "*-" * (n//2) + "*" + "\n"))
          + "-*" * (n//2) + "-" + "\n" ) ## print a uneven amount of * and - in each line, and begin lines
## with alternating characters

# TASK 3: Writes a script to simulate tossing a fair coin n times. Then determines the longest consecutive sequence of tails and heads.
import random
flipCoin = lambda : random.choice(['H','T'])

N = int (input ("enter a # to flip a coin n times: "))
side = 0
memory = []
hList = tList = [1]
hStreak = tStreak = 1

while N > 0:
    side = flipCoin ()
    
    memory += side
    
    if side == memory [ len (memory) - 2] and len (memory) > 1:
        if side == memory [ len (memory) - 3] and len (memory) >= 3:
            if side == 'T':
                tStreak += 1
            elif side == 'H':
                hStreak += 1
        else:
            if side == 'T':
                hList = [hStreak] + hList
                hStreak = 1
                tStreak += 1
            if side == 'H':
                tList = [tStreak] + tList
                tStreak = 1
                hStreak += 1
    elif side != memory [len (memory) -2]:
        tList = [tStreak] + tList
        hList = [hStreak] + hList
        tStreak = 1
        hStreak = 1
                
    N += -1

tList = [tStreak] + tList
hList = [hStreak] + hList

print (memory)
print ('The longest sequence of "T" is ', (max (tList)))
print ('The longest sequence of "H" is ', (max (hList)))
