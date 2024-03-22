#Shreya Shukla
#IntroCS2 pd 09
#HW08 -- Script Writing
#2019--02--26

import math

# reads in 3 integer]s and prints the largest odd number among them.
# If none of the are] odd, prints "None of the numbers are odd."


def largest_odd (a, b, c):
    if a % 2 == 1:
        if b % 2 == 1:
            if c % 2 == 1:
                print (max (a, b, c))
            else:
                print (max (a, b))
        else:
            if c % 2 == 1:
                print (max (a, c))
            else:
                print (a)

    else:
        if b % 2 == 1:
            if c % 2 == 1:
                print (max (b, c))
            else:
                print (b)
        else:
            if c % 2 == 1:
                print (c)
            else:
                print ("None of the numbers are odd!")

## Test Cases:
largest_odd (1, 2, 4) #1
largest_odd (0, 3, 0) #3
largest_odd (1, 3, 9) #9

largest_odd (7, 9, 8) #9
largest_odd (10, 12, 3) #3
largest_odd (20, 21, 16) #21
    
largest_odd (0, 0, 0) # None of the numbers are odd!
largest_odd (7, 7, 7) #7
