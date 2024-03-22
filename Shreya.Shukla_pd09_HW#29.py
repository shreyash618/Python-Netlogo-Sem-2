# Shreya Shukla
# Intro CS2 pd 09
# HW # 29: Leonardo of Pisa
# 2019--04--14

def fibI (n):
    '''Takes in a non-negative integer n.
Returns the nth term in the Fibbonachi sequence.'''
    ans = 0
    for i in range (0, n +1):
        if i == 0:
            a = 0
            ans = a
        if i == 1:
            b = 1
            ans = b
        if i != 0 and i != 1:
            ans = a + b
            a = b
            b = ans
    print (ans)

fibI (0) #shou;d return 0
fibI (1) # should return 1
fibI (3) # should return 2
fibI (5) # should return 5

fibI (9) # should return 34
fibI (12) # should return 144

fibI (30) # should return 832040
