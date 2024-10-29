#Sort any array of 0's , 1's and 2's

#Method - 1 -> Use any sorting algo  (for merge Sort TC: NlogN  , SC: O(N))


#Method - 2 ->Using two loops (Better solution)
#TC : O(2N)
#SC : o(1)
def sorting(arr):
    zero = 0         #We count the number of 0's , 1's and 2's and overwrite the array 
    one = 0
    two = 0

    for i in range(0,len(arr)):
        if arr[i] == 0:
            zero +=1
        elif arr[i] == 1:
            one +=1
        
        else:
            two +=1
    
    for j in range(0,len(arr)):
        if zero >0:
            arr[j] = 0
            zero -=1
        
        elif one>0:
            arr[j] =1
            one -=1
        
        else:
            arr[j] =2
            two -=1
    
    return arr

print(sorting(arr = [2,0,2,1,1,0,2]))      # Output:- [0,0,1,1,2,2]


#===========================
#Method 3:- Dutch National Flag Algo (Optimal solution)

"""
Rule 1 :-

1. [0...low-1]       -> 0
2. [low......mid-1]  -> 1
3. [mid....high]     -> 0 or 1 or 2 (random)
3. [high+1....n-1]   -> 2


Rule 2:- 
1.  arr[mid]= 0   -> swap( arr[low] and arr[mid])  and low ++   and mid ++
2.  arr[mid]= 1   -> mid++
3.  arr[mid]= 2   -> swap(arr[mid] and arr[high])   and  high --
"""
#TC: O(N)
#SC: O(1)
def sorting(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid <=high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low +=1
            mid +=1
        
        elif arr[mid] == 1:
            mid +=1
        
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -=1
    
    return arr

print(sorting(arr = [2,0,2,1,1,0,2]))      # Output:- [0,0,1,1,2,2]