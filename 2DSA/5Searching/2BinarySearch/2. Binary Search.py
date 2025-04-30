"""
Concept:- 
- For applying Binary Search in a list, following things needed:-
        1. List should be sorted
        2. List can have duplicate or non-duplicate elements

Steps:- 
1. Take 2 pointers low and high and calculate mid= (low+high) // 2
2. Compare the target with the mid and accordingly move the low or high pointer to trim down the search space.
"""

#Method 1- using recursion      (Assume Non-duplicate elements present in list)
#TC: Log2(N)
# SC: O(log n)     (due to function call stack)
def Search(arr,ele, low, high):
    if low > high:
        return -1
    
    midind= (low+high) // 2

    if arr[midind] == ele:
        return midind
    
    elif ele < arr[midind]:
        return Search(arr,ele, low, midind-1)
    
    else:
        return Search(arr,ele, midind + 1, high)

lst=[3,2,5,6]
low = 0
high = len(lst)-1
key = 5

print(Search(lst,key,low,high))

#================================

#Method 2 : Using simple loop method
# TC: Log2(N)
# SC: O(1)
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
key = 5

print("Index of ", key," is:",Search(lst,key,low,high))