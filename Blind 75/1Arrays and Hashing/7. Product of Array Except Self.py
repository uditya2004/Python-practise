"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Using two pointers - Brute Force
#TC: O(N^2)
#SC: O(N)
def productExceptSelf(nums):
    result = []               #SC: O(N)

    for i in range(0,len(nums)):
        temp = 1
        for j in range(0,len(nums)):
            if i != j:
                temp *= nums[j]
        result.append(temp)
    
    return result


nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))

#=======================
# Using two pointers - Best Solution
#TC: O(2N) = O(N)
#SC: O(N)
def productExceptSelf(nums):
    result = [1]*len(nums)  #SC: O(N)
    
    #Moving forward in "nums" and multiplying  to get prefix multiplied in result for corresponding element
    prefix = 1
    for i in range(0, len(nums)):
        result[i] *= prefix
        prefix *= nums[i]        #updating prefix
    
    #Moving backward in "nums" and multiplying  to get suffix multiplied in result for corresponding element
    suffix = 1
    for j in range(len(nums)-1,-1,-1):
        result[j] *= suffix
        suffix *= nums[j]        #updating suffix
    
    return result

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))

#=======================
# Using Division operator - NOT ALLOWED
#TC: O(N^2)
#SC: O(N)
def productExceptSelf(nums):
    zero_count = 0
    product = 1

    for element in nums:
        if element == 0 :       
            zero_count +=1       #Counting number of zeroes in an array
        else:
            product *= element   #Finding the product of all non-zero elements
    
    if zero_count > 1:           #If there are more than one zero in the array, the result for all elements should be zero.
        return [0] * len(nums)
    

    result = []
    for num in nums:
        if zero_count == 0:
            result.append(product // num)
        else:
            if num == 0:                 # If there is exactly one zero, all elements except the one corresponding to the zero should be zero.
                result.append(product)   # For zeroth element , append the product itself
            else:
                result.append(0)
    
    return result

nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))