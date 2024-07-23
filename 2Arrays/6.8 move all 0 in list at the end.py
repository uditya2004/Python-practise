# Method 1- Using remove and append
def move(lst):
    for i in lst:
        if i==0:
            lst.remove(i)
            lst.append(0)
    return lst

l=[1,0,0,2,3,0,6]
print(move(l))

# ----------------
# Method 2 - Bruteforce

def move(lst):
    temp =[]
    #for adding all non-zero elements to temp list
    for i in lst:  #O(N)
        if i !=0:
            temp.append(i)
    
    #for replacing all the elements of lst by temp
    for j in range(0, len(temp)):  #O(x)
        lst[j]=temp[j]
    
    #for adding zero's at the end
    for k in range(len(temp), len(lst)):  #O(N-x)
        lst[k]=0

l=[1,0,0,2,3,0,6]
move(l)
print(l)

# ----------------
# Method 3 - Optimal solution (Using 2 Pointers)

def move(lst):
    j=None
    
    # Setting the j pointer to the 1st "0" in the lst
    for i in range(0,len(lst)):  # O(N)
        if lst[i]==0:
            j=i
            break
    
    #if all elements in a list is non-zero, simply return the list
    if j==None:
        return(lst)
    
    for p in range(j+1,len(lst)):   # p is getting incremented through this loop

        if lst[p] !=0:            # just write condition when to increment j
            lst[j],lst[p]=lst[p], lst[j]
            j +=1   

    return lst


l=[1,0,2,3,6]
# l=[1,0,0,2,3,0,6]

print(move(l))
