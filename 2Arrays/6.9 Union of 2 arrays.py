# def union(lst1,lst2):
#     return (sorted(list(set(lst1+lst2))))


# arr1 = [1,2,3,4,5]  
# arr2 = [2,3,4,4,5,6]
# print(union(arr1,arr2))

#======================================
#Method 2: Through every element of both lists in a set, only unique elements will be accepted by a set
# def union(lst1,lst2):
#     result = set()
#     for i in lst1:
#         result.add(i)

#     for i in lst2:
#         result.add(i)
    
#     return list(result)


# arr1 = [1,2,3,4,5]  
# arr2 = [2,3,4,4,5,6]
# print(union(arr1,arr2))

#=============================
#Method 3 - Optimal solution (Using 2 pointers)

"""
While traversing we may encounter three cases.

Case -1 arr1[ i ] == arr2[ j ] 
Here we found a common element, so insert only one element in the union. Let’s insert arr[i] in union and increment i.

NOTE: There may be cases like the element to be inserted is already present in the union, in that case, we are inserting duplicates which is not desired. So while inserting always check whether the last element in the union vector is equal or not to the element to be inserted. If equal we are trying to insert duplicates, so don’t insert the element, else insert the element in the union. This makes sure that we are not inserting any duplicates in the union because we are inserting elements in sorted order.

case 2 - arr1[ i ]  < arr2[ j ]
arr1[ i ] < arr2[ j ] so we need to insert arr1[ i ] in union.IF last element in  union vector is not equal to arr1[ i ],then insert in union else don’t insert. After checking Increment i.
-----
Case 3 - arr1[ i ] > arr2[ j ]
arr1[ i ] > arr2[ j ] so we need to insert arr2[ j ] in union. IF the last element in the union vector is not equal to arr2[ j ], then insert in the union, else don’t insert. After checking Increment j. After traversing if any elements are left in arr1 or arr2 check for condition and insert in the union.
"""
def union(lst1,lst2):
    i=0 # moves in lst1
    j=0 #moves in lst 2
    ans= []
    while i<len(lst1) and j<len(lst2):
        if lst1[i] <= lst2[j]:   # Case 1 and 2
            if lst1[i] not in ans:
                ans.append(lst1[i])
            i +=1
        
        elif lst1[i] > lst2[j]:  # Case 3
            if lst2[j] not in ans:
                ans.append(lst2[j])
            j +=1
           
    
    while i<len(lst1):  # If any elements left in arr1
        if lst1[i] not in ans:
            ans.append(lst1[i])
        i +=1
    
    while j<len(lst2):  # If any elements left in arr2
        if lst2[j] not in ans:
            ans.append(lst2[j])
        j +=1

    return ans


arr1 = [1,2,3,4,5]   #i
arr2 = [2,3,4,4,5,6] #j
print(union(arr1,arr2))