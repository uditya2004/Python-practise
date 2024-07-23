#Ques:- Place all the unquie element of the sorted array to the start , rest of the elements can be anything. Return the length of non-duplicate element list

#METHOD 1:-  Adding every element to set (BRUTE FORCE) , Time complexity - O(NlogN + N), space complexity - O(N)
def checkdub(list1):
    set1 = set()
    for i in list1:    # Add every element to the set and only unique elements will be accepted by the set.
        set1.add(i)    # Time complexity - O(NlogN)

    k = len(set1)

    #Placing all the unquie element of the sorted array to the start
    j=0                 #Placing pointer in list
    for i in set1:      # Time complexity - O(N)
        list1[j] = i
        j +=1
    
    return k

l=[0,1,1,1,2,2,3,3,4]

print("Original List: ", l)
print(checkdub(l))
print(l)

#===================
#METHOD 2 - USING 2 POINTERS  , TC - O(N) , SC - O(1)
def checkdub(lst):
    i=0
    for j in range(1,len(lst)):
        if lst[i] != lst[j]:
            lst[i+1] = lst[j]
            i +=1
            
    return i+1   #returning the length ( length will be one greater than the index i)



l=[0,1,1,1,2,2,3,3,4]

print("Original List: ", l)
print("Lenght: ", checkdub(l))
print(l)