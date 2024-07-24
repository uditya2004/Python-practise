def miss(lst,n):    
    XOR1 = 0   #Xor of all no. 1 to N
    XOR2 = 0   # XOR of list elements

    for i in range(0,n-1):
        XOR1 = XOR1 ^ i+1      #1 to N-1
        XOR2 = XOR2 ^ lst[i]
    
    XOR1 = XOR1 ^ n
    return XOR1 ^ XOR2

     

l=[1,3,4]
n=4
print(miss(l,n))