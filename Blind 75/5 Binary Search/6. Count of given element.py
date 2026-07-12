"""
- Question:- Array is sorted , count the no. of occurence of target in the given array

APPROACH:
- If the array is sorted:
    - All the same elements stays together as group
    - So just find the start and end index of this group and do => end - start + 1 to get the count 
"""
# Solution 1
class Solution:
    def countElement(self, arr: list[int], target: int) -> int:
        
        # first occurance
        firstOccurence = -1
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                firstOccurence = mid
                right = mid - 1        # once the element is found, to get start index, we aim for lower index, hence move in left portion
            
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # last occurence
        lastOccurence = -1
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                lastOccurence = mid
                left = mid + 1        # once the element is found, to get end index, we aim for higher index, hence move in right portion
            elif arr[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        if firstOccurence == -1 and lastOccurence == -1:
            return 0
        else:
            return lastOccurence - firstOccurence + 1


obj = Solution()
arr = [2,5,10,10,10, 11, 18]
target = 100
print(obj.countElement(arr, target))