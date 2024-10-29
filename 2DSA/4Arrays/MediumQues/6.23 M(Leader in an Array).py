"""
Ques:-
Given an array, print all the elements which are leaders. 
A Leader is an element that is greater than all of the elements on its right side in the array.

Note:- Last element will always be the leader
"""
#Method - 1: Using 2 pointers.
# TC: O(N^2)
#SC: O(N)
def findLeader(arr, n):
    leader= []
    
    for i in range(0, n):
        isLeader = True

        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                isLeader = False
                break
            else:
                isLeader = True
        
        if isLeader == True:
            leader.append(arr[i])

    return leader
        

arr = [10,22,12,3,0,6]
print(findLeader(arr, len(arr)))

#=========================================
#Method - 2: Using 2 pointers.
# TC: O(N)
#SC: O(N)
def findLeader(arr, n):

    # Step:- 1 - Collect all the leaders
    leader= []
    maxel= float("-inf")    
    for i in range(n-1, -1,-1):
        if arr[i] > maxel:
            maxel = arr[i]
            leader.append(arr[i])

    # Step:- 2 - Formatting the answer
    leader.reverse()    #Time complexity: O(N) 

    return leader 

arr = [10, 22, 12, 3, 0, 6]
print(findLeader(arr, len(arr)))
