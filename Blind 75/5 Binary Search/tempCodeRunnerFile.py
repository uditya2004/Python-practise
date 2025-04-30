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
        elif nums[mid] <= nums[high]:  # means mid is in right sorted portion, so search in the left sorted portion
            high = mid - 1
    
    return result

nums = [11,13,15,17]

print(findMin(nums))
