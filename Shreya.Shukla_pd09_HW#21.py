## Shreya Shukla
## Intro CS2 pd 09
## HW #21:  NestIsMyLoophole
## 2019--03--17

# output all the prime numbers up to n (n is user input)
def AllPrimesUptoN ():
    n = int (input ('Enter a integer: '))
    for i in range (2, n + 1):
        for j in range (2, i + 1):
            if j < i :
                if i % j == 0:
                    #print (i, end = ' is not prime \n')
                    break
            else:
                if j == i:
                    print (i, end = ' is prime \n')



AllPrimesUptoN ()
## Test Case: Enter a integer : 9
#2 is prime 
#3 is prime 
#5 is prime 
#7 is prime 


# should yield a multiplication table/array where all numbers 1-10 are being multiplied by all numbers 1-10
def MultiplicationTable ():
    a = 0
    b = 8
    print ('           ', end = '')
    for k in range (1,11):
        if k == 10:
            print ('    ', k, end = '    ')
        else:
            print ('     ', k, end = '    ')
    print ('\n', '   ', ' +---------------------------------------------------------------------------------------------------------')

    for i in range (1,11):
        if len (str (i)) == 2:
            print ('    ', i, end = '|')
        if len (str (i)) == 1:
            print ('      ', i, end = '|')
        if a < 9:
            a = a + 1
        if b > 3:
            b = b -1
        for j in range (1, 11):
            if i != 1 and i == a and j >= b:
                print ('    ', i * j, end = '   ')
            elif i == 10 and j >= 2:
                print ('    ', i * j, end = '   ')
            elif len (str (i*j)) == 1:
                print ('      ', i * j, end = '   ')
            elif len (str (i*j)) == 2:
                print ('     ', i * j, end = '   ')
            elif len (str (i*j)) == 3:
                print ('    ', i * j, end = '   ')
            if j == 10:
                print ('\n')

MultiplicationTable ()
                
# produces a table of modular arithmetic addition for any value user inputs on [2,10) 
def Extension (n):
    if n >= 10 or n < 2:
        print ('Please enter a integer between [2, 10)')
    else:
        print ('        ', end = '  ')
        for k in range (1, n + 1):
                print ('    ', k, end = '    ')
        print ('\n', '   ', ' +---------------------------------------------------------------------------------------------------------')
        for i in range (1, n + 1):
            print ('    ', i, end = '|')
            for j in range (1, n + 1):
                if i == n and j == n:
                    print ('     ', n , end = '   ')
                else:
                    print ('     ', (i + j) % n, end = '   ')
                if j == n:
                    print ('\n')
Extension (6)
Extension (5)
