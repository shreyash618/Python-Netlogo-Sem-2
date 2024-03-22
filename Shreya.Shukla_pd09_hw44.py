# Shreya Shukla
# Intro CS2 pd09
# HW 44: Let's sort the bubbles
# 2019--23--05

# sorts a numerical list into ascending order using the method bubble sort
def bubbleSort (nums):
    '''Inputs a numerical list, nums.
Returns nums in increasing numerical order.'''
    for n in range (0, len(nums)):#traverses through each number upto the length of the list,nums
        for i in range(0, len(nums)-n-1): #shortens the length of the list, nums, that
            #is being processed in each run by exactly 1 (n increases by 1, and the len(nums)-n-1
            #decreases by 1. This way, the last number of the list that was sorted
            #is not going to be sorted again.
            if nums[i] > nums[i + 1]: # checks if the Ith term is greater than the previous term
                nums [i], nums[i +1] = nums[i+1], nums[i] #if so, switches the terms so that the greater number is on the right
    print (nums) #prints the sorted list
    
bubbleSort([5,3,1]) # should print [1,3,5]
bubbleSort ([10,7,8,3,2,5]) # should print [2,3,5,7,8,10]
bubbleSort ([11, 5, 10, 3]) # should print [3,5,10,11]
bubbleSort([12,2,14,5,16,3,12,2]) # should print [2, 2, 3, 5, 12, 12, 14, 16]

