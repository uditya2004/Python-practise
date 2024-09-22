"""
Ques:-
There's an array "A" of size "N" with an equal number of positive and negative elements. 
Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
Note: Start the array with positive elements.
"""
# Method 1:- Two Pointer - One for traversing array , another for find the element to swap.

# TC:- O(N^2)
# SC:- O(1)

# 0 -> +
# 1 -> -
# def Rearrange(arr,N):
#     prevSign = -1
#     currsign = -1

#     for i in range(0,N):
        
#         #updating current element sign
#         if arr[i]<0:
#             currsign = 1
#         elif arr[i] > 0:
#             currsign = 0
        
#         if currsign == 1 and i== 0:   # 1st element is -ve, as per question it should be +ve, we have to swap with +ve one
#             for j in range(i+1, N):
#                 if arr[j] > 0:
#                     arr[i], arr[j] = arr[j],arr[i]
#                     break

#         if currsign == prevSign:  # Current and prev element both were +ve. So We have to swap current with a -ve num
#             for j in range(i+1, N):
#                 if currsign == 0 and arr[j] < 0:         # Current and prev element both were +ve. So We have to swap current with a -ve num
#                     arr[i], arr[j] = arr[j],arr[i]
#                     break

#                 elif currsign == 1 and arr[j] > 0:       # Current and prev element both were -ve. So We have to swap current with a +ve num
#                     arr[i], arr[j] = arr[j],arr[i]
#                     break
        
#         #Before we move to next element we update the prev sign
#         if arr[i] < 0:
#             prevSign = 1  
#         else:
#             prevSign = 0 
        
        
#     return arr


# arr = [1,2,-3,-1,-2,3]
# N = 6

# print(Rearrange(arr,N))


#=================================
# Method - 2 Separate +ve and -ve elements and merge   (Brute Force -> 2 iteration solution)

#TC:- O(2N)
# SC: O(N/2 + N/2) = O(N) 

# def Rearrange(arr,N):
#     # Create separate lists for positive and negative numbers.
#     positive = []
#     negative = []

#     for i in arr:
#         if i<0:
#             negative.append(i)
#         else:
#             positive.append(i)
    
#     # Merge the positive and negative lists alternately into the original array.
#     for j in range (0,N//2):
#         arr[2*j] = positive[j]       # Putting +ve numbers in even places
#         arr[2*j + 1] = negative[j]   # Putting -ve numbers in odd places

#     return arr


# arr = [1,2,-3,-1,-2,3]
# N = 6

# print(Rearrange(arr,N))


#=================================
# Method - 3 Separate +ve and -ve elements and merge   (Better Solution -> 1 iteration solution)

#TC:- O(N)
# SC: O(N/2 + N/2) = O(N) 

def Rearrange(arr,N):
    # Create separate lists for positive and negative numbers.
    result = [0]*N
    
    pos_Ind = 0
    neg_Ind = 1

    for i in range(0,N):
        if arr[i] > 0:
            result[pos_Ind] = arr[i]
            pos_Ind +=2
        
        elif arr[i] < 0:
            result[neg_Ind] = arr[i]
            neg_Ind +=2
    
    return result


arr = [1,2,-3,-1,-2,3]
N = 6

print(Rearrange(arr,N))

