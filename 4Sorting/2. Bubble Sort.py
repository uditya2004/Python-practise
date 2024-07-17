lst=[13,46,24,50,20,9]
n=len(lst)

for i in range(n-1,0,-1):   # i -> n-1 to 1
    for j in range(0,i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1], lst[j]

print(lst)