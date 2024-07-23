"""
Given an integer n

an array of size N-1 containing N-1 numbers between 1 to N. Find the 1 missing num in the array.
"""
# def miss(lst,b):
#     for i in range(1,b+1):
#         if i not in lst:
#             return i

#     return None

# l=[1,3,4]
# n=4
# print(miss(l,n))

#==============
#Method 2 - Bruteforce
"""
Take all numbers between 1 to N , compare each number with all the elements in the array, if found return the number
"""
# def miss(lst,n):
    
#     for i in range(1,n+1):
#         flag = 0

#         for j in lst:
#             if j == i:
#                 flag =1
#                 break
#         if flag==0:
#             return i
        

# l=[1,3,4]
# n=4
# print(miss(l,n))

#=========================
#Method 3 - Summation
# def miss(lst,n):

#     #sum of list elements
#     Sum= (n*(n-1))/2

      #sum of first N natural num.
#     ExpectedSum = sum(lst)
    
#     return (ExpectedSum-Sum)
        

# l=[1,3,4]
# n=4
# print(miss(l,n))
#============================

#Method 4- Using XOR
"""
Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2
"""
def miss(lst,n):

    
    XOR1 =0  #Xor of num 1 to n
    XOR2=0   #Xor of array elements
    for i in range(0,n-1):
        XOR1 = XOR1 ^ i+1        # XOR up to [1...^N-1]
        XOR2 = XOR2 ^ lst[i]     #The list lst has n-1 elements, so last element index is n-2
    
    XOR1 = XOR1 ^ n   # For making XOR up to [1...^ N-1 ^ N]
    return XOR1 ^ XOR2


l=[1,3,4]
n=4
print(miss(l,n))



