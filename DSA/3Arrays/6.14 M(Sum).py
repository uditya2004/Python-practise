"""
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
"""

# Method 1 - Two Pointers  (Brute Force)
# TC: O(N)
# SC: O(1)
def findsum (n, arr, target) : 

    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i,j], "YES"
    
    return [-1,-1], "NO"


result1, result2 = findsum(n = 5, arr= [2,6,5,8,11], target = 15)
print(result1)
print(result2)

#==============================================

#Method 2 - Hashing  (Better Solution)
#TC: O(N)
#SC: O(N)
def findsum (n, arr, target) : 
    dict1 = {}

    for i in range(0,n):
        
        remaining = target - arr[i]

        if remaining in dict1:
            return "Yes", [dict1[remaining], i]
        else:
            dict1[arr[i]] = i
    
    return "No", [-1,-1]


result1, result2 = findsum(n = 5, arr= [2,6,5,8,11], target = 10)
print(result1)
print(result2)


#============
#Method 3 - Two Pointer  (Better Solution)
#TC: O(N)
#SC: O(N)
def findsum (n, arr, target) :
    nums = sorted(arr)              # We sort the array -> Now from left if we move forwards we increase the sum . From the right if we move backwards we decrease the sum, we use this calculation to find the target.
    left = 0
    right = n-1

    while left<right:
        if nums[left] + nums[right] > target:
            right -=1

        elif nums[left] + nums[right] == target:
            return "YES"

        else:
            left +=1
    
    return "NO"


print(findsum(n = 5, arr= [2,6,5,8,11], target = 1))
