def longSubArray(array, N, k):
    maxLength = 0
    sum = 0
    for i in range(0, N):

        for j in range(i, N):
            if sum <k:
                sum += array[j]
            
            else:
                sum = 0
                break 
            
            if sum == k:
                maxLength = max(maxLength, j-i + 1 )

                
    
    return maxLength

 
array = [2,3,5]
N = 3     #Length of array
k = 5     #Sum

print("Final Answer:- ", longSubArray(array, N, k))