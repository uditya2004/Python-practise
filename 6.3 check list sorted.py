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
      
    for i in range(1,len(list)):  # start with 1, so in 1st iteration index 1 is compared with index 0. If we start with 0, then index 0 will be compared with -1
        if list[i]<list[i-1]:
            return False
        prev = i
    
    return True

l=[1,2,4,5]
if checksort(l):
    print("Yes")

else:
    print("No")