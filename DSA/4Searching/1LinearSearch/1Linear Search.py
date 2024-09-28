def Search(lst, key):
    for i in range(0,len(lst)):
        if lst[i] == key:
            return i
        
    return -1
    
lst = [1,2,3,4]
key = 4
result  = Search(lst, key)
print 

if result != -1:
    print("Element found at index: ", result)
else:
    print("Not Found")