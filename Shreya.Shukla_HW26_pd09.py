## Shreya Shukla
## Intro CS2 pd 09
## HW #26: Float like a butterfly, sting like a bee
## 2019--04--06

def minPos(L):
    '''Takes in L, a list enclosed in [ ] containing only numeric elements.
Returns the index of smallest value in L. '''
    MAX, MaxPos = None, None
    for i in range (len (L)):
        if MAX == None or int (L[i]) > MAX:
            MAX= int (L[i])
            MaxPos =  i
    return MaxPos
print (minPos ([9, 1, 3, 2, -1])) # 0
print (minPos ([2, 3, 44, 1])) # 2
print (minPos ([0, 4, 18, 11])) #2
print (minPos ([2, 32])) #1

print (minPos ([False,True])) # 1
print (minPos ([2.0, 6/3])) # 0
print (minPos ([6/3, 2.0])) # 0
