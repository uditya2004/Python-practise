"""
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
"""

# def maxSum(lst, k):
#     result = 0
#     i = 0

#     sum = 0
#     for j in range(0, len(lst)):
#         sum +=lst[j]

#         if j >= k - 1:
#             result = max(result, sum)
#             sum -= lst[i]
#             i +=1
#     return result

# l = [2, 1, 5, 1, 3, 2] 
# k=3 
# print(maxSum(l,k))


# window size can be checked using j-i+1
def maximumSumSubarray (arr,k):
    result = 0
    i = 0
    sum = 0 

    for j in range(0, len(arr)):
        sum += arr[j]

        if (j-i+1) == k:
            result = max(result, sum)
            sum -= arr[i]
            i +=1
    return result


arr= [5,4,-1,7,8]
k = 6
print(maximumSumSubarray (arr,k))