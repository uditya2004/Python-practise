"""
Ques. Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
"""

# # #Method 1 - Time complexity O(N^2) and Space complexity O(1)
# def miss(lst):
    
#     for i in range(0,len(lst)):
#         count = 0
#         for j in range(0,len(lst)):
#             if lst[j]==lst[i]:
#                 count +=1
            
#             if count==2: #as all the elements have max freq. of 2, as soon as we hit 2, we will move to next "i" ,without comparing with other elements.
#                 break
        
#         if count ==1:
#             return lst[i]
    
#     return -1    # this is only executed when all the elements occur twice.

# arr1 = [4,1,2,1,2]
# arr2 = [2,1]
# arr3 = [1,1,2,2]

# print(miss(arr1))
# print(miss(arr2))
# print(miss(arr3))

#===============================
# #Method 1 - Using XOR. Time complexity O(N) and Space complexity O(1)
def miss(lst):
    Xor=0
    for i in lst:
        Xor= Xor^i
    
    if Xor !=0:
        return Xor
    else:
        return -1

arr1 = [4,1,2,1,2]
arr2 = [2,1]   # This case fails , also not expected by question
arr3 = [1,1,2,2]

print(miss(arr1))
print(miss(arr2))
print(miss(arr3))



