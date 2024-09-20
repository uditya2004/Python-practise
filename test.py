import math
def maxSubArray(arr,n):
    max_sum = -math.inf
    sum = 0

    for i in range(0,n):
        sum +=arr[i]
        max_sum = max(max_sum, sum)

        if sum<0:
            sum = 0
            
    if max_sum < 0: 
        max_sum = 0

    return max_sum



nums = [-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10 ]      #Output should be 0
print(maxSubArray(nums, len(nums)))


