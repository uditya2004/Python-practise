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
    def maxSubarraySum(self, arr, k):
        maxSum = float('-inf')
        currSum = 0

        i = 0
        for j, item in enumerate(arr):
            # adding the current element of j
            currSum += item

            # if the window size > k , we move i one time, as it's fixed sized window, window will outgrow only by 1 unit
            if j-i+1 > k:
                currSum -= arr[i]
                i +=1
            
            # if window size == k, it is a valid window, update result
            if j-i+1 == k:
                maxSum = max(maxSum, currSum)
        
        return maxSum



obj = Solution()
arr= [100, 200, 300, 400]
k = 1
print(obj.maxSubarraySum(arr, k))