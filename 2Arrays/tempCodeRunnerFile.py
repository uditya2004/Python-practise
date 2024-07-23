def checkdub(lst):
    i=0
    length=0
    for j in range(1,len(lst)):
        if lst[i] != lst[j]:
            lst[i+1] = lst[j]
            i +=1
            length +=1

    return length



l=[0,1,1,1,2,2,3,3,4]

print("Original List: ", l)

print(l)