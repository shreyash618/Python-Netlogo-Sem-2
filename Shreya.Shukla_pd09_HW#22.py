# Shreya Shukla
# Intro CS2 pd 09
# HW # 22 : FunFunFunctions
# 2019--03--18

def gcd (a, b):
    """ prints the greatest common factor of a and b """
    factors = [ ]
    for i in range (1, (min (a, b) + 1)): 
        if a % i == 0:
            if b % i == 0:
                factors += [i]
    if i == min (a, b):
        print (max (factors))

gcd (22, 36) # should print 2
gcd (18, 36) # should print 18
gcd (104, 65) # shoud print 13
gcd (18, 21) # should print 3
gcd (1, 1) # should print 1
gcd (160, 144) # should print 16

def gcd3 (a, b, c):
    """prints the greatest common factor of a, b and c"""
    factors = [ ]
    for i in range (1, (min (a, b, c) + 1)):
        if a % i == 0:
            if b % i == 0:
                if c % 1 == 0:
                    factors += [i]
    if i == min (a, b, c):
        print (max (factors))

gcd3 (27, 300, 450) # should print 3
gcd3 (12, 18, 24) # should print 6
gcd3 (1, 1, 1) # should print 1
gcd3 (70, 16, 6) # should print 2
gcd3 (17, 19, 13) # should print 1
