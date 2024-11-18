"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
#Using Two Pointer:- Brute Force
#TC: O(N^2)
#SC: O(1)

def twoSum(nums, target):
    
    for i in range(0,len(nums)):

        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    
nums = [3,2,4]
target = 6
print(twoSum(nums, target))


#================
#Using Dictionary - Best Solution
# TC: O(N)
# SC: O(N)
def twoSum(nums, target):
    dict1 = {}
    

    for i in range(0, len(nums)):
        remaining = target - nums[i]

        if remaining in dict1:
            return [dict1[remaining], i]

        else:
            dict1[nums[i]] = i

    

nums = [3,2,4]
target = 6
print(twoSum(nums, target))