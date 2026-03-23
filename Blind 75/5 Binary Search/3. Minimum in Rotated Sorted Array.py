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

class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            result = min(result, nums[mid])   # using the mid to update answer

            # Cutting down the search space
            """
            - nums[mid] > nums[right]  => means we can find smaller elements towards right => left = mid + 1 
            - nums[mid] <= nums[right] => means going towards right will only give us bigger values, so smaller value can be nums[mid] and towards left

            """
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        

        return result

nums = [4,5,6,7,0,1,2]

print(findMin(nums))

