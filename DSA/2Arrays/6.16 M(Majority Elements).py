"""
Ques:- Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array.
"""
#Method 1 - Two Pointer   (Brute Force)
#TC: O(N^2)
#SC: O(1)
def findnum(arr, n):
    for i in range(0,n):
        num_count =0
        for j in range(0,n):
            if arr[j] == arr[i]:
                num_count +=1
        
        if num_count > n/2:
            return arr[i]



arr = [2,2,1,1,1,2,2]

N= 7     #N/2 - 4
print(findnum(arr, N))      # Output:- 2

print()

#===============================
#Method 2- Hashing using Dictionary (Better Solution)
#TC: O(2N)
#SC: O(N)
def findnum(arr, n):
    dict1 = {}
    
    #storing the elements with its occurnce:
    for i in range(0, n):
        if arr[i] in dict1:
            dict1[arr[i]] +=1
        
        else:
            dict1[arr[i]] = 1
    
    #searching for the majority element:
    for i in dict1.items():
        if i[1] > n//2:
            return i[0]


arr = [2,2,1,1,1,2,2]

N= 7     #N/2 - 4
print(findnum(arr, N))      # Output:- 2

print()


#==================
#Method 2.2 - Hashing using array  
# Time Complexity: O(n + m)  -> The list lst is initialized with a size of max(arr) + 1, which is m
# Space Complexity: O(m)           
def findnum(arr, n):
    lst = [0] * (max(arr) +1)
    
    for i in range(0, n):
        lst[arr[i]] +=1
    
    for i in range(0,len(lst)):
        if lst[i] == n//2:
            return i



arr = [3,2,3]
N= 3
print(findnum(arr, N))      # Output:- 2


#==========================================
#Method - 3: Moore’s Voting Algorithm (Optimal Solution)
#TC:- O(2N)
#SC:- O(1)
def findnum(arr, n):
    #Applying Moore's Algo
    majority_element = arr[0]
    count = 1

    for num in arr[1:]:
        if count == 0:
            majority_element = num
        
        if num == majority_element:
            count += 1
        else:
            count -= 1
    
    # Checking if the stored element is the majority element
    count2 = 0
    for j in arr:
        if j == majority_element:
            count2 +=1
    
    if count2 > n//2:
        return majority_element
    else:
        return -1
        

arr = [2,2,1,1,1,2,2]
N= 7
print(findnum(arr, N))      # Output:- 2



