# The given list should be sorted and non-duplicate element list for applying binary search.

#Method 1- using recursion
# def Search(arr,ele, low, high):
#     if low > high:
#         return -1
#     midind= (low+high) // 2

#     if arr[midind] == ele:
#         return midind
    
#     elif ele < arr[midind]:
#         return Search(arr,ele, low, midind-1)
    
#     else:
#         return Search(arr,ele, midind + 1, high)

# lst=[3,2,5,6]
# low = 0
# high = len(lst)-1
# key = 5

# print(Search(lst,key,low,high))

#================================

#Method 2 
def Search(arr,ele, low, high):
    
    while low <= high:         #We will stop when low and high crosses each other
        midInd= (low + high) // 2

        if arr[midInd] == ele:
            return midInd

        elif ele < arr[midInd]:
            high = midInd - 1
        
        else:
            low = midInd + 1
    
    return -1

lst=[3,2,5,6]
low = 0
high = len(lst)-1
key = 1

print(Search(lst,key,low,high))