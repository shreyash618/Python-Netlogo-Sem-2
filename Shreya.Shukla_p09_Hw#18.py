## Shreya Shukla
## Intro CS2 pd 10
## HW 18: Home Home On The Range...
## 2019--03--14

# prints out the decimal equivalents of 1/2, 1/3, 1/4, ..., 1/ 10.
def fractions ():
    for i in range (2, 11):
        print ('1/' + str (i) + ' = ' + str (1.0 / i) + '\n')
fractions ()
## should yield :
# 1/2 = 0.5
# 1/3 = 0.333333333333
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.166666666667
# 1/7 = 0.142857142857
# 1/8 = 0.125
# 1/9 = 0.111111111111
# 1/10 = 0.1

# sum of the odd integers from 1 to n.
def sumOdd ():
    num = int (input ('enter a positive number: '))
    sum = 0
    for i in range (1, num + 1):
        if i % 2 == 1:
            sum = sum + i
    if i == num :
        print ('sum of odds from 1 to '+ 'num: '+ str(sum))
sumOdd()
## ie: enter a positive number : 9 would yield 25 because 1+3+5+7+9 == 25

# prints the integers from 10 to 30, with n integers per line
def nPerLine ():
    numPerLine = int (input ('enter a positive number : '))
    list = [ ]
    n = 10
    j = 0

    while n <= 30:
        while j <= numPerLine:
            if j == numPerLine:
                print (list)
                list = [ ]
                j = 0
            if n > 30:
                if j < numPerLine and j != 0:
                    print (list)
                break
            else:
                list = list + [n]
                j += 1
                n += 1
             
nPerLine ()
# ie: enter a positive number : 3 would produce 7 lines, with each line containing 3 consecutive integers
## after 10 and below 31
## [10, 11, 12]
## [13, 14, 15]
## [16, 17, 18]
## [19, 20, 21]
## [22, 23, 24]
## [25, 26, 27]
## [28, 29, 30]
