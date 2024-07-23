def leftrotate(list):
    a=list[0]
    for i in range(1,len(list)):
        list[i-1] = list[i]
    
    list[len(list)-1]=a
    return list


l=[1,2,3,4,5]
print(leftrotate(l))