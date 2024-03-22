## Shreya Shukla
## Intro CS2 09
## HW 14: While All This Is Happening
## 2019--03--07

## asks the user to input 10 integers, and then prints the largest
## odd integer that was entered. If no odd was entered,
## prints "None are odd integers."

biggestOdd = None

i = 10
while i > 0:
    number = int(input ('Please enter a integer:'))
    if number % 2 == 1 and (number != None or number > biggestOdd):
        biggestOdd = number
    i += -1
if i == 0:
    if biggestOdd == None:
        print ("None are odd integers.")
    else:
        print (biggestOdd)
