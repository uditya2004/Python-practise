def move(lst):
    for i in lst:
        if i==0:
            lst.remove(i)
            lst.append(0)
    return lst

l=[1,0,0,2,3,0,6]
print(move(l))