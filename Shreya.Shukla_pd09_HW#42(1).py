# Shreya Shukla
# Intro CS2 pd 09
# HW 42: BucketList
# 2019--05--21

# Note: I don't know what the bucket list method is; I wasn't in class

#returns the arithmetic mean of the numeric elements in list nums. 
def mean_list(nums):
    newlist = [0]
    for i in nums:
        newlist[0] = newlist[0] + i
    return newlist[-1]/len(nums)

print(mean_list([1,2,3,4,5])) #returns 3.0
print(mean_list([30,40,50,60,70,80,90])) #returns 60

#returns the mode, as a list, of the set of numeric elements in list nums.
def mode_list(nums):
    newlist, n = [], 0
    while n < len(nums):
        newlist.append (nums.count(nums[n]))
        n = n + 1
    maxL = max (newlist)
    del newlist [0: len(newlist) + 1]
    if maxL == 1:
        print (newlist)
    else:
        for i in nums:
            if nums.count (i) == maxL:
                newlist.append (i)
                nums.remove (i)
        print (newlist)
mode_list([1,2,3,4,5]) # should return []
mode_list([0,5,7,3,2,3] ) # returns [3]
mode_list([0,5,7,3,7,3] ) # returns [3,7]
mode_list([8,8,8,4,4,4,2,2,2,242]) # should return [2,4,8] 


# takes a list of non-negative integers and prints a horizontal bar for each
# index, commensurate with the value at said index
def bar_graphify (nums):
    for i in nums:
        print (min(nums), ':', '=' * min (nums))
        nums.remove(min (nums))
        nums.append (max(nums))
#should return bar lines of the corresponding lengths in numerical order
bar_graphify ([0,1,2,3])
bar_graphify ([3,1,2,0])
bar_graphify ([4,6,2,8])

