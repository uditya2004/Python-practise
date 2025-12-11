"""
- Question:- Array is sorted , count the no. of occurance of target in the given array
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
                right = mid - 1
            
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
                left = mid + 1
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