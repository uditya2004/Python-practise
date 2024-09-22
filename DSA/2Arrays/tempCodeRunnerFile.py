def Rearrange(arr,N):
    # Create separate lists for positive and negative numbers.
    result = [0]*N
    
    pos_Ind = 0
    neg_Ind = 1

    for i in range(0,N):
        if arr[i] > 0:
            result[pos_Ind] = arr[i]
            pos_Ind +=2
        
        elif arr[i] < 0:
            result[neg_Ind] = arr[i]
            pos_Ind +=2
    
    return result


arr = [1,2,-3,-1,-2,3]
N = 6

print(Rearrange(arr,N))