# Shreya Shukla
# Intro CS2 pd 09
# HW#29B - Leonardo of Pisa
# 2019--16--04

def fibI_recur (n):
    '''Takes in a non-negative integer n.
Returns the nth term in the Fibbonachi sequence.'''
    ans = 0
    if n == 1:
        ans = 0
        return ans
    else:
        if n == 2:
            ans = 1
            return ans
        else:
            ans += fibI_recur (n - 1) + fibI_recur (n - 2)
            return ans
    
##print (fibI_recur (1)) #should print 0
##print (fibI_recur (2)) # should print 1
##print (fibI_recur (4)) # should print 3
##print (fibI_recur (6)) # should print 5
##print (fibI_recur (10)) # should print 34
##print (fibI_recur (13)) # should print 144
##print (fibI_recur (31)) # should print 832040

def fib_List (num, first = 0, second = 1):
    '''Takes in a non-negative integer n.
Returns the nth term in the Fibbonachi sequence.'''
    if num > 1:
        return fib_List (num - 1, first + second, first)
    else:
       print (first)

fib_List (1) # should print 0
fib_List (2) # should print 1
fib_List (4) # should print 3
fib_List (6) # should print 5
fib_List (10) # should print 34
fib_List (13) # should print 144
fib_List (31) # should print 832040
