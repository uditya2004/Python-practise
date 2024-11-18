"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""
#Two Pointers:- Brute Force
#TC: O(N^2)
# #SC: O(1)

def hasDuplicate(nums):

    for i in range(0, len(nums)):

        for j in range(i+1, len(nums)):
            
            if i != j and nums[i] == nums[j]:
                return True
    
    return False
            

    
nums = [1,1,1,3,3,4,3,2,4,2]
print(hasDuplicate(nums))

#=======================
#Using sort() :- Better Solution
#TC: O(NLogN + N) = O(NLogN)
#SC: O(N)
def hasDuplicate(nums):
    if len(nums) == 1:
        return False
    else:
        tempnum = sorted(nums)   #O(n log n)
        
        
        for i in range(0, len(tempnum)):
            if tempnum[i] == tempnum[i-1]:
                return True
        
        return False
    
nums = [1,2,3,4]
print(hasDuplicate(nums))

#==========================
#Using Dictionary :- Best Solution
#TC: O(N)
#SC: O(N)
def hasDuplicate(nums):
    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] +=1
            return True

        else:
            dict1[i] =1

    return False
    
nums = [1,1,1,3,3,4,3,2,4,2]
print(hasDuplicate(nums))


#====================
#Comparing with set(nums) length
#TC: O(N) , The function converts the list nums to a set, which requires iterating through all elements of nums.
#SC: O(N),  The function creates a set from the list nums. In the worst case, if all elements in nums are unique, the set will have the same number of elements as nums
def containsDuplicate(nums):
    if len(nums) == 1:
        return False
    
    return (True if len(set(nums))  < len(nums) else False)

nums = [1,2,3,1]
print(containsDuplicate(nums))

