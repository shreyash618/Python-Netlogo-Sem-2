# Shreya Shukla
# IntroCS2 pd09
# HW 09: Controlled Randomness
# 2019--02--27

import random

# simulates flipping a two sided coin, with equal probability for heads and tails
def flipCoin () :
    num = random. randint (0, 1)
    side = lambda num: "Heads" if num == 1 else "Tails"
    print (side (num) )


flipCoin()
flipCoin()
flipCoin()

# simulates rolling one fair n-sided die
def rollDie (n):
    num = random. randint (1, n)
    print (num)
    
rollDie (1) # should give 1
rollDie (2) # should give 1 or 2

rollDie (6) # should give any number in between 1 and 6
rollDie (6) # should give any number in between 1 and 6
rollDie (6) # should give any number in between 1 and 6

rollDie (10) # should give any number in between 1 and 10
