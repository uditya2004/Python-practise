#METHOD 1 - USING Sets 
# def checkdub(list1):
#     b=list(set(list1))
#     return b
    

# l=[1,1,2,2,3,3,4,4]

# print(checkdub(l))

#================
#METHOD 2 - USING 2 POINTERS
# def checkdub(list1):
#     i=0
#     for j in range(1,len(list1)):
#         if list1[i] != list1[j]:
#             i +=1             # Move the pointer i only when jth element is different than ith element
#             list1[i]=list1[j]
        
#     del list1[i+1:]
                   
    
    

# l=[1,1,2,2,3,3,4,4]
# checkdub(l)
# print(l)
