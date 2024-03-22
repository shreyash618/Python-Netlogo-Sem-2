#Shreya Shukla
#Intro CS2 pd 10
#HW06:Pairing Magic
#2019-02-14

(n , m) = (int(input ('magicPair n')), int(input('magicPair m')))

if n % 10 == m % 10:
    if (2 * (n % 10)) == ((n % 100) // 10) + ((m % 100) // 10):
        print ('True')
    else:
        print ('False')
    ## IF THE ONES DIGITS ARE EQUAL, THIS WILL PRINT TRUE
    ## WHEN THE SUM OF THE ONES DIGITS EQUALS THE SUM
    ## OF THE TENS DIGITS, FALSE OTHERWISE
        
elif ((n % 100) // 10) == ((m % 100) // 10):
        if (2 * ((n % 100) // 10)) == (n % 10) + (m % 10):
            print ('True')
        else:
            print ('False')
## IF THE TENS DIGITS ARE EQUAL, THIS WILL PRINT TRUE
## WHEN THE SUM OF THE TENS DIGITS EQUALS THE SUM
## OF THE ONES DIGITS, FALSE OTHERWISE
            
elif n % 10 == ((m % 100) // 10):
    if ((n % 10) + ((m % 100) // 10)) == ((m % 10) + ((n % 100) // 10)):
            print ('True')
    else:
            print ('False')

## If the ones digit of the first number and the tens digit of the
## second number are EQUAL, THIS WILL PRINT TRUE
## WHEN THE SUM of the tens digit of the first number and ones
# digit of the second number EQUALS THE SUM ones digit of the
## first number and the tens digit of the second number, false otherwise

elif m % 10 == ((n % 100) // 10):
    if ((m % 10) + ((n % 100) // 10)) == ((n % 10) + ((m % 100) // 10)):
            print ('True')
    else:
            print ('False')
## If the tens digit of the first number and the ones digit of the
## second number are EQUAL, THIS WILL PRINT TRUE
## WHEN THE SUM of the ones digit of the first number and tens
# digit of the second number EQUALS THE SUM tens digit of the
## first number and the ones digit of the second number, false otherwise

##Test the following:
#magicPair(12,10) -> True  (the 1's match, and the other two add up to 2)
#magicPair(43,54) -> True  (the 4's match, and the other two add up to 8)
#magicPair(53,31) -> True 13

#special case:
#magicPair(13,13) -> False  (the 1's match and 3's match but don't add up to each other)

