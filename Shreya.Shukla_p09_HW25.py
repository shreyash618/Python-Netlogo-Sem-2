# Shreya Shukla
# Intro CS2 period 09
# HW #25: Turtle Tree
# 2019--01--04

#Ms. Khevelev, I could not write this function RECURSIVELY even after 3 attempts (described below).
import turtle
t = turtle.Turtle ()
t.lt (90)

# ATTEMPT 1
# draws a fractal tree of degree x and length Length
def TreeFunc (Length, x):
    ''' Takes in two positive numerical values, Length and x.
Turns turtles Length units forward and x degrees right and left.'''
    origL = Length
    if Length > 20:
        TurnLeft (Length, x)
        TurnRight ((Length - 20) // 4, x, Length)
    
## HELPER fxn: Moves the turtle left and reduces the length of each stride
def TurnLeft (length, x):
          t.fd (length)
          t.lt (x)
          length -= 2
          if length > 20:
              TurnLeft (length, x)
          else:
              return length
# Helper fxn: Moves the turtle right and increases the length of each stride untill it's original length is restored.
def TurnRight (Length, x, origL):
        t.bk (Length)
        t.rt (2.0 * x)
        t.fd (Length)
        t.bk (Length)
        t.lt (6.0/4.0 * x)
        Length += 2
        if Length < origL:
            TurnRight (Length, x, origL)
        
TreeFunc (33, 6)

# ATTEMPT 2
origL = 0
def TreeFunc1 (LENGTH, x):
    '''Assumes LENGTH and x are positive integers.
Creates a tree with max length LENGTH, that rotates x degrees right or left at each turn.'''
    origL = LENGTH
    goForward (LENGTH, x)
    goBack ((LENGTH - 10) // 4, x)
# moves forward
def goForward (Length, x):
    if Length <= 10:
        return None
    else:
        t.lt (x)
        t.fd (Length)
        Length -= 4
        goForward (Length, x)
#origL = 120
#moves back
def goBack (Length, x):
    if Length == origL:
        return None
    else:
        t.bk (Length)
        t.rt (2 * x)
        t.fd (Length)
        t.bk (Length)
        t.lt (x)
        Length +=4
        goBack (Length, x)

#goBack (16, 12.6)
TreeFunc1 (120, 33)

## ATTEMPT 3 - has no base case or reductive call idk
TreeFunc (120, 33)
def TreeFunc2 (Length, x):
    if Length <= 7:
        t.bk (Length)
        t.rt (2*x)
        t.fd (Length)
        t.bk (Length)
        t. lt (x)
        Length += 2
        TreeFunc2 (Length, x)
    else:
        t.fd (Length)
        t.lt (x)
        Length -= 2
        TreeFunc2 (Length, x)
        
TreeFunc2 (22, 22)
