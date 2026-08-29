"""
QUESTION
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
"""

# TC: O(N)
# SC: O(1)
# FIXED SIZED SLIDING WINDOW OF SIZE -> K
class Solution:
    def maxSumSubarray(self, arr, size)->int:
        n = len(arr)

        # sliding window -> Fixed window
        result = float('-inf')
        currSum = 0

        i = 0
        j = i
        while j < n:   # in fixed size window, j will reach last element then we have to stop. "i" will never hit last element.
            # 1. CALCULATION:- ADD the incoming element (always)
            currSum += arr[j]     

            # 2. If window overgrew, SHRINK from left => In fixed window, we move i one time, as window will outgrow only by 1 unit
            if j-i+1 > size:        
                currSum -= arr[i]
                i += 1

            # 3. If window is exactly size, it's a valid answer → RECORD
            if j-i+1 == size:
                result = max(result, currSum)

            # 4. MOVE j
            j += 1

        return result 


obj = Solution()
arr= [1,2,3,4,5,6,7,8]
size = 3
print(obj.maxSumSubarray(arr, size))