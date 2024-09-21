"""
find the contiguous subarray (containing at least one number) which has the largest sum and returns its sum and prints the subarray.
"""

#Method:- Finding sum of all possible subarray and return the max sum -> Brute Force
#TC:- O(N^3)
#SC:- O(1)
# def largestsum(arr,n):
#     max_sum = 0
#     for i in range(0,n):  #Iterate all starting array indexes

#         for j in range(i,n):     #Iterate all ending array indexes
    
#             temp_sum = 0
#             for k in range(i,j+1):   #Used for summation of all the elements between i and j
#                 temp_sum += arr[k]
        
#             max_sum = max(max_sum, temp_sum)
    
#     return max_sum



# arr = [-2,1,-3,4,-1,2,1,-5,4]      #[4,-1,2,1] has the largest sum = 6. 
# print(largestsum(arr, len(arr)))


#===============================
#Method:- Finding sum of all possible subarray and return the max sum -> Better Solution
#TC:- O(N^2)
#SC:- O(1)
# def largestsum(arr,n):
#     max_sum = 0
#     for i in range(0,n):  #Iterate all starting array indexes
#         temp_sum = 0
#         for j in range(i,n):     #Iterate all ending array indexes
#             temp_sum +=arr[j]
#             max_sum = max(max_sum, temp_sum)
            
    
#     return max_sum



# arr = [-2,1,-3,4,-1,2,1,-5,4]      #[4,-1,2,1] has the largest sum = 6. 
# print(largestsum(arr, len(arr)))

#===============================
#Method:- Kadane's Algorithm -> Optimal Solution
#TC:- O(N)
#SC:- O(1)

"""
- Keep on adding elements to sum and compare with max_sum on each step . But if the sum becomes -ve , then make the sum=0 and then move forward
"""
import math
def largestsum(arr,n):
    max_sum = -math.inf
    sum = 0
    ansStart = -1   #Used for printing indexes
    ansEnd = -1     #Used for printing indexes

    for i in range(0,n):
        if sum == 0:
            ansStart = i

        sum +=arr[i]
        
        if sum>max_sum:
            max_sum = sum
            ansEnd = i


        if sum<0:
            sum = 0
    
    #if the max_sum is -ve , then return 0 instead
    if max_sum < 0: 
        max_sum = 0

    return max_sum , [ansStart, ansEnd]



arr = [-2,1,-3,4,-1,2,1,-5,4]      #[4,-1,2,1] has the largest sum = 6. 
result1, result2 = largestsum(arr,len(arr))
print(result1)
print(result2)



