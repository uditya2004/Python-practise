def Search(arr,el):
    for i in range(0,len(arr)):
        if arr[i]==el:
            return i
        
    return -1

lst=[1,2,3,4]
key=5
Result = Search(lst,key)
print(Result)

# if Result == -1:
#     print("Element not found")

# else:
#     print("Element Found at index: ", Result)