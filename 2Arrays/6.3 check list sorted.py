#Method 1- With built-in function (sort function does more work)
# def checksort(list):
#     newlist= sorted(list)
#     if newlist == list:
#         return True
#     else:
#         return False

#Method 2 - Without built-in function (Prefered)
def checksort(list):
    n=len(list)
    if len(list) <=1:
        return True
      
    for i in range(0,n-1):  #we go till n-2 th index as we are comparing with 1 element forward. If we go till n-1 , then one element forward would go out of range
        if list[i] > list[i+1]:
            return False
    
    return True

l=[1,2,4,5]
if checksort(l):
    print("Yes")

else:
    print("No")