"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
"""

class Solution:
    def maxSubarraySum(self, arr, k):
        maxSum = float('-inf')

        n = len(arr)
        i = 0
        j = 0
        sum = 0
        
        while j < n:

            # add arr[j] to sum
            sum += arr[j]

            # Then check condition
            # 1. If windows size less than k, only move j
            if (j-i+1) < k:  
                j +=1

            # 2. If window size equals k, it is a valid window, So update the maxSum value, remove element from back, move both pointers forward
            else:   
                maxSum = max(maxSum, sum)
                sum -= arr[i]
                j +=1
                i +=1
            
        return maxSum


obj = Solution()
arr= [100, 200, 300, 400]
k = 1
print(obj.maxSubarraySum(arr, k))