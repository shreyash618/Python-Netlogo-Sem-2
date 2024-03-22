## Shreya Shukla
## Intro CS2 09
## HW 14: While All This Is Happening
## 2019--03--07

def countDown(n):
    i = n
    if i < 0 :
        print ("Please enter a positive integer!")
    elif i == 0:
        print ("Blast Off!")
    else:
        while i > 0:
            print (i)
            i += -1
            if i == 0:
                print ("Blast Off!")
        






countDown(3)
## should print 3, 2, 1, Blast Off!
countDown (-1)
## should return "Please enter a positive integer!"
countDown (0)
## should return "Blast Off!"
