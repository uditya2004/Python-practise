def search(nums: list[int], target: int) -> int:
    
    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:  # left half is sorted
            if nums[low] <= target < nums[mid]:
                # search in the left sorted portion itself
                high = mid -1
            else:
                # search in the right side
                low = mid + 1
                
        else:  # right half is sorted

            if nums[mid] < target <= nums[high]:
                # search in the right sorted portion itself
                low = mid + 1
            else:
                # search in the left side
                high = mid - 1
                
    return -1



nums = [5,1,3]
target = 5
print(search(nums, target))