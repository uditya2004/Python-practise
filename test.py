def lenOfLongSubarr (arr, n, k) : 
    dict1 = {}
    sum = 0
    maxLen = 0

    for i in range(0, n):
        sum += arr[i]

        if sum == k:
            maxLen = max(maxLen, i+1)

        remaining = sum - k

        if remaining in dict1:
            length = i - dict1[remaining]
            maxLen = max(maxLen, length)
        
        if sum not in dict1:
            dict1[sum] = i


    
    return maxLen
 
arr = [1, 2, 3, 1, 1, 1, 1]
N = 7     #Length of a
k = 3     #Sum

print("Final Answer:- ", lenOfLongSubarr(arr,N,k))