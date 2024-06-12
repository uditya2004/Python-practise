#LEFT ROTATE 1 TIMES

#Method 1 - Use built-in functions
# def leftrotate(list):
#     a=list.pop(0)
#     list.append(a)
#     return list

#Method 2 - Use Logic
# def leftrotate(list):
#     a=list[0]
#     for i in range(1,len(list)):
#         list[i-1] = list[i]
    
#     list[len(list)-1]=a
#     return list


# l=[1,2,3,4,5]
# print(leftrotate(l))

#========================================
# LEFT ROTATE D TIMES

#METHOD 1 - Our Logic (More time complexity)
# def leftrotate(list,d):
#     a=list[0]
#     for i in range(d):
#         a=list[0]
#         for i in range(1,len(list)):
#             list[i-1] = list[i]
    
#         list[len(list)-1]=a
#     return list


# l=[1,2,3,4,5]
# D=3
# print(leftrotate(l,D))

#-------------
#METHOD 2 - Our Logic - Using reverse() - (O(n) and O(1)auxilary space)
def rev(list1,start,end):
    while start<end:
        list1[start],list1[end]= list1[end], list1[start]
        start +=1
        end -=1

def leftrotate(list,d):
    l=len(list)
    rev(list,0,d-1)     # As all the changes are done through reference "list" and "list1" directly on "lt", we used only 1 variable (i.e It).

    rev(list,d, l-1)

    rev(list,0,l-1)
    return list

lt=[1,2,3,4,5]
D=2
print(leftrotate(lt,D))

#-------------

#METHOD 3 - Using list slicing
# def leftrotate(list,d):
#     newlist = list[d:] + list[:d]
#     return newlist


# l=[1,2,3,4,5]
# D=2
# print(leftrotate(l,D))

#-------------
#METHOD 4 - Using deque method

# from collections import deque
# l=[1,2,3,4,5]
# D=2
# dq = deque(l)
# dq.rotate(-D)  # -D to left rotate and D to right rotate

# newlist = list(dq)
# print(newlist)

#-------------
#METHOD 5 - Using pop and append method
# def leftrotate(list,d):
#     for i in range(d):
#         list.append(list.pop(0))
#     return list


# l=[1,2,3,4,5]
# D=2
# print(leftrotate(l,D))