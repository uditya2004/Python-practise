#Method 1 - Time complexity O(N) and space complexity O(N)
# def cons(lst):
#     temp=[]
#     count=0
#     for i in range(0,len(lst)):
#         if lst[i]==1:
#             if i==(len(lst)-1):
#                 count +=1
#                 temp.append(count)
#             count +=1
            
#         elif lst[i]==0:
#             temp.append(count)
#             count = 0
        
    
#     return max(temp)


# prices = [1, 1, 0, 1, 1, 1]
# print(cons(prices))

#================================
#Method 2 - Time complexity O(N) and space complexity O(1)
def cons(lst):
    max_count=0
    count=0
    for i in range(0,len(lst)):
        if lst[i]==1:   #when 1 is encountered , increase count by 1
            count +=1

            
        elif lst[i]==0:   #whenever zero is encountered , make max_count of 1 = count and reintialise count to 0 
            max_count = count
            count = 0
    
    return max(max_count, count)   # if we reach last index and last element was 1, then "max_count = count" will not happen but count will get increased . That's why we take the greatest of both count and max_count. 


prices = [1, 1, 0, 1, 1, 1]
print(cons(prices))