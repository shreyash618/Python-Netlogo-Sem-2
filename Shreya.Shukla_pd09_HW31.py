# Shreya Shukla
# Intro CS2 pd 09
# HW 31: Towers of Hanoi
# 2019--22-04

# Rules for the tower of hanoi: a) each disk must be on a tower at all times, excluding transport. This
# means you cannot just put a disk down on a counter, it can only be moved to a tower 
# b) no smaller disk can have a larger disk on top of it
# c) each disk must be on one of three towers: tower 0, tower 1, or tower 2
# d) you want to arrange the disks in largest to smallest order, moving them from the starting tower (tower 0) to the final destination (tower 1)
def hanoi (num, start = '0', temp = '2',end = '1'):
    '''Takes in num, the number of disks being moving from Tower 0 to Tower 1.
Returns the steps of the shortest pathway to move the disks, one by one, such that no tower is atop a smaller tower'''
    if num == 1:
        print (start + ' to ' + end)
    elif num == 2:
        print (start + ' to '+ temp)
        print (start + ' to ' + end)
        print (temp + ' to ' + end)
    else:
        if num % 2 == 1:
            hanoi (num -1, start, end, temp)
            hanoi (1, start, temp, end)
            hanoi (num -1, temp, start, end)
        if num % 2 == 0:
            hanoi (num -1, start, end, temp)
            hanoi (1, start, temp, end)
            hanoi (num-1, temp, start, end)
            
## test cases:
## hanoi (1): 0 to 1
## hanoi (2): 0 to 2
##    0 to 1
##    2 to 1
## hanoi (3): 0 to 1
##    0 to 2
##    1 to 2
##    0 to 1
##    2 to 0
##    2 to 1
##    0 to 1
## hanoi (4)
##    0 to 2
##    0 to 1
##    2 to 1
##    0 to 2
##    1 to 0
##    1 to 2
##    0 to 2
##    0 to 1
##    2 to 1
##    2 to 0
##    1 to 0
##    2 to 1
##    0 to 2
##    0 to 1
##    2 to 1
