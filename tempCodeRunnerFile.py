#Method - Hashing using array
def findnum(arr, n):
    count = round(n/2)
    print("N/2:- ", count)
    lst = [0] * (max(arr) +1)
    
    for i in range(0, n):
        lst[arr[i]] +=1
    
    print(lst)
    for i in range(0,len(lst)):
        if lst[i] == count:
            return i



arr = [3,2,3]
N= 3
print(findnum(arr, N))      # Output:- 2