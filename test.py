
def longSubArray(array, N, k):
    maxLength = 0
    sum = 0
    for i in range(0, N):

        for j in range(i, N):
            if sum <k:
                sum += array[j]
            
            if sum == k:
                maxLength = max(maxLength, j-i + 1 )

            if sum>= k:
                sum = 0
                break

                
    
    return maxLength


N = 3
k = 5     #Sum
array = [2,3,5]

print("FInal Answer:- ", longSubArray(array, N, k))