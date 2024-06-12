# def rotate(lst):
#     first= lst[0]
#     for i in range(1,len(lst)):
#         lst[i-1]=lst[i]
    
#     lst[len(lst)-1]=first

# l=[1,2,3,4]
# rotate(l)
# print(l)
#=======================

def rev(lst, start,end):
    while start<end:
        lst[start],lst[end]= lst[end], lst[start]
        start +=1
        end -= 1


def rotate(lst,d):
    l=len(lst)
    rev(lst,0,d-1)

    rev(lst,d,l-1)

    rev(lst,0,l-1)


l=[1,2,3,4]
d=2
rotate(l,2)
print(l)


