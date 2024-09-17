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
        
        if sum not in dict1:    # If the sum is not in the dictionary, we can add it to the dictionary with the index i.
            dict1[sum] = i


    
    return maxLen
 
array = [1, 2, 3, 1, 1, 1, 1]
N = 7     #Length of array
k = 3     #Sum

print("Final Answer:- ", longSubArray(array, N, k))