"""
Note: Subarray means , contiguous part of an array , (array mein se kahi se bhi pick krke subarray nhi bna skte, all collected elements should be next to each other.)
"""

#Method:- Two Pointer   -> Brute Force
#TC: O(N^2)
#SC: O(1)
# def longSubArray(array, N, k):
#     maxLength = 0

#     for i in range(0, N):
#         sum = 0      #Reset Sum

#         for j in range(i, N):
#             if sum <k:
#                 sum += array[j]
            
#             if sum == k:
#                 maxLength = max(maxLength, j-i + 1 )

#             if sum>= k:
#                 break     
    
#     return maxLength

 
# array = [2,3,5]
# N = 3     #Length of array
# k = 5     #Sum

# print("Final Answer:- ", longSubArray(array, N, k))


#===================
#Method :- Using Hash -> Better Solution
#TC: O(N)
#SC: O(N)
def longSubArray(array, N, k):
    dict1 = {}
    sum = 0
    maxLen = 0

    for i in range(0, N):
        sum += array[i]

        if sum == k:
            maxLen = max(maxLen, i+1)

        remaining = sum - k          

        if remaining in dict1:     
            len = i - dict1[remaining]   # If the remaining sum present in the dict1, we can get the length of the subarray.
            maxLen = max(maxLen, len)    # Update the maxLen.
        
        if sum not in dict1:             # If the sum is not in the dictionary, we can add it to the dictionary with the index i.
            dict1[sum] = i
    
    return maxLen
 
array = [1, 2, 3, 1, 1, 1, 1]
N = 7     #Length of array
k = 3     #Sum

print("Final Answer:- ", longSubArray(array, N, k))


#=====================================

#Method - Two Pointer  (Optimal Solution)
def getLongestSubarray(a, k):
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: 
            Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")




