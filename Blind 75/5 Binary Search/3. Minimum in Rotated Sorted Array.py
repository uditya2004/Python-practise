"""
APPROACH
- Set the low at the starting and high at the end
- Out of low or high , whoever is bigger, we move that, ahead by 1 (in case of low) or backward by 1 (in case of high), until low and high becomes same.
- When the low or high becomes same, that's the smallest element in an array
"""
# Method - 1
# TC: O(N)  (Better solution)
# SC: O(1)
def findMin(nums: list[int]) -> int:
    low = 0
    high = len(nums) - 1

    while low != high:

        if nums[low] < nums[high]:
            high -=1
        
        elif nums[low] > nums[high]:
            low +=1
        else:
            low +=1
    
    return nums[low]

nums = [11,13,15,17]

print(findMin(nums))


#======================================
# Method - 2
# TC: O(LogN)   (Best solution)
"""
APPPROACH:
- In a rotated array we have 2 portions "left sorted array" and "right sorted array"
- Take 2 pointers low = 0 and high = len(lst) - 1
- Find the mid 

- Now check lst[low] <= lst[mid]:
    - If yes, means mid is in the left sorted portion, So now only search the right sorted portion   (low = mid + 1)
    - If no, means mid is in the right sorted portion, So now only search in the left sorted portion (high = mid - 1)

- After updating the low and high , check if low <= High:
    - If yes , our search space is now a sorted array and the first element of the sorted array is the smallest.
"""

def findMin(nums: list[int]) -> int:
    low = 0
    high = len(nums) - 1

    result = nums[0]
    while low <= high:

        if nums[low] < nums[high]:   # means we are in the sorted array portion. In a sorted array left most element is the smallest
            result = min(result, nums[low])
            break

        mid = (low + high) // 2

        result = min(result, nums[mid])

        if nums[mid] >= nums[low]: # means mid is in left sorted portion, so search in the right sorted portion
             low = mid + 1
        else:                      # if it's not in the left sorted porting, then it is in right sorted portion, so search in the left, as all the values to the right will be bigger than the current mid.
            high = mid - 1
    
    return result

nums = [4,5,6,7,0,1,2]

print(findMin(nums))

