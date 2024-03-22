# Shreya Shukla
# Intro CS2 pd09
# HW 45: Of some sorts
# 2019--24--05

def selectionSort (nums):
    for n in range (0, len(nums)-1): #traverses through the entire list
        for i in range (n, len(nums)): #traverses through the unsorted list
            currentMin = nums[n] #sets the current min as the first element
            # of the section of the list being observed
            currentValue = nums [i] #keeps track of the Ith term
            if currentValue < currentMin : # if the current value is smaller
                # than the current min, the first element of the unsorted list becomes
                #the current value, and the current min takes the place of the current value
                #Also, the current min becomes the current value, since the current value is smaller
                nums[n], nums[i] = currentValue, currentMin
                currentMin = currentValue
    print (nums) #if you want to trace this, move the print statement inside the forloop
selectionSort ([20,12,10,15,2])
selectionSort ([2,4,3,1]) #should print [1,2,3,4]
selectionSort ([8,9,2,1]) #should print [1,2,8,9]
# A trace of the first function call should look like:
##[20, 12, 10, 15, 2] ==>

##[12, 20, 10, 15, 2]
##[10, 20, 12, 15, 2]
##[2, 20, 12, 15, 10]
##[2, 12, 20, 15, 10]
##[2, 10, 20, 15, 12]
##[2, 10, 15, 20, 12]
##[2, 10, 12, 20, 15]
##[2, 10, 12, 15, 20]

def insertionSort (nums):
    for i in range(1, len(nums)):  # Traverses through
        # every item of the list except for the first, repeating the same process
        CurrentValue = nums [i] #Stores the current number value from the list
        j = i-1 #J is the index of the number right before the current value
        while j >= 0 and nums[j] > CurrentValue: # if the Jth term is GREATER
            # THAN the current value, then: 
            nums[j+1] = nums[j] # shift the Jth term 1 index to the right
            j -= 1 #decrease the value of j by 1

        nums[j+1] = CurrentValue #the first index processed becomes current value
    print (nums)
insertionSort ([2,5,3,4,1,8,11,12,32]) # Should print
# [1, 2, 3, 4, 5, 8, 11, 12, 32]
insertionSort ([2,4,3,1]) #should print [1,2,3,4]
insertionSort ([8,9,2,1]) #should print [1,2,8,9]
