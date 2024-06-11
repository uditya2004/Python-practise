#Method 1- With built-in function (sort function does more work)
# def checksort(list):
#     newlist= sorted(list)
#     if newlist == list:
#         return True
#     else:
#         return False

#Method 2 - Without built-in function (Prefered)
def checksort(list):
    if len(list) <=1:
        return True
    
    prev=list[0]
    for i in list[1:]:            
        if i< prev:
            return False
        
        prev = i
    
    return True

l=[1,2,4,3]
if checksort(l):
    print("Yes")

else:
    print("No")