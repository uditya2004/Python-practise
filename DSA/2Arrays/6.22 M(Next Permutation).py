"""
CONCEPT
1. Find the longest Prefix match :- a[i] < a[i+1]   (i.e find the breaking point {traversing right to left in the array and arrange elements (in mountain shape) such that smaller element is smaller than bigger on, the point where the graph moves down is the breaking point })
        - let the element that cause breaking point be a[i]

2. Find "just greater number" than a[i] , so that you stay close. Once found , swap with that element with a[i]
3. Reverse the part of the array a[i+1] to a[n-1]   (Place the rest of the digits on right in sorted order(ascending)).

Note:- 
- if "index_of_breaking_point_element" = -1, then reverse the number and that will be your answer
"""

#Method - 1 (Optimal Solution) :- In this we used our implemented reverse function
# TC:- O(3N)
# SC: O(1)   
def reverse(arr, low, high):
    
    while low<high:
        arr[low], arr[high] = arr[high], arr[low]
        low +=1
        high -=1
    
    return arr


def nextPermutation(arr,n):

    # Step 1: Find the break point:
    ind = -1                          # initializing breaking point as -1
    for i in range(n-2, -1,-1):       # traversing from right to left in array
        if arr[i] < arr[i+1]:         # We compare current element with i+1 (i.e it's just next element on it's right) . 
            ind = i                   # If a[i] < a[i+1] then break point is found. 
            break                     # Break the loop as we found the break point, purpose of this loop is done.
    

    # Step 1.1:- HANDLE EDGE CASE:- If break point does not exist:
    if ind == -1:                      # ind= -1 means the whole array is in descending order and the value of ind didn't change.
        # reverse the whole array:
        arr= reverse(arr, 0, n-1)      # If the whole array is in descending order then reverse the whole array and that will be your answer
        return arr
    

    # Step 2: Find the next greater element 
    for j in range(n-1, ind, -1):                  # Traversing from n-1 till ind+1
        if arr[j] > arr[ind]:                      # The element moving from n-1 till ind+1 will be in increasing order. So the 1st element that is greater than arr[ind] is the next greater element.
            arr[j], arr[ind] = arr[ind], arr[j]    # now swap that element with arr[ind]:
            break                                  # We break as the purpose of this loop is over.
    
    # Step 3: reverse the right half:
    arr = reverse(arr, ind+1, n-1)             # reverse this part of the array -> from ind+1, n-1
    return arr

    
arr = [1,3,2]
print(nextPermutation(arr,len(arr)))


#===============
#Method 1.1:- We use python reversed feature

# def nextPermutation(nums):

#     # Step 1: Find the break point:
#     ind = -1         # break point
#     for i in range(len(nums)-2, -1,-1):
#         if nums[i] < nums[i+1]:
#             ind = i
#             break


#     # If break point does not exist:
#     if ind == -1:
#         # reverse the whole numsay:
#         nums.reverse()
#         return nums


#     # Step 2: Find the next greater element 
#     for j in range(len(nums)-1, ind, -1):
#         if nums[j] > nums[ind]:
#             nums[j], nums[ind] = nums[ind], nums[j]    #and swap it with nums[ind]:
#             break

#     # Step 3: reverse the right half:
#     nums[ind+1:] = reversed(nums[ind+1:])
#     return nums

    
# nums = [1,3,2]
# print(nextPermutation(nums))