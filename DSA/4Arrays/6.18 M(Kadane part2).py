"""
Ques:- 

Given an array arr[], with 0-based indexing, select any two indexes, i and j such that i < j. 
From the subarray arr[i...j], select the smallest and second smallest numbers and add them, you will get the score for that subarray. 
Return the maximum possible score across all the subarrays of array arr[].
"""
#Method - 1: 3 pointers 
#TC: O(N^3)
#SC: O(1)
# def maxScore(arr):
#     result = float('-inf')

#     for i in range(len(arr)):
        
#         for j in range(i+1, len(arr)):
#             small = float('inf')
#             secsmall= float('inf')

#             for k in range(i,j+1):
#                 if arr[k] <small:
#                     secsmall = small
#                     small = arr[k]
                
#                 elif arr[k] >small and arr[k] <secsmall:
#                     secsmall = arr[k]
            
#             result = max(result , small + secsmall)

#     return result



# arr = [4, 3, 1, 5, 6]
# print(maxScore(arr))


#========================================
#Method - 1: 2 pointers 
#TC: O(N^2)
#SC: O(1)
def maxScore(arr):
    result = float('-inf')

    for i in range(0, len(arr) -1):     #We go till len-1 as we want our array to have atleast 2 elements (because of condition i<j)
        small = arr[i]
        secsmall = float('inf')


        for j in range(i+1, len(arr)):
            if arr[j] < small:
                secsmall = small
                small = arr[j]
            
            elif arr[j] >small and arr[j]<secsmall:
                secsmall = arr[j] 

            if secsmall != float('inf'):
                result = max(result, small + secsmall)
            
    return result



arr = [4, 3, 1, 5, 6]  
print(maxScore(arr))    #11


