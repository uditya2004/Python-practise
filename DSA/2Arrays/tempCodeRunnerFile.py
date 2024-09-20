def findnum(arr, n):
    #Applying Moore's Algo
    majority_element = arr[0]
    count = 1
    
    for num in arr[1:]:
        if count == 0:
            majority_element = num
        
        if num == majority_element:
            count += 1
        else:
            count -= 1
    
    #Verifying if the element is really a majority or not
    count2 = 0
    for j in arr:
        if j == majority_element:
            count2 +=1
    
    if count2 > n//2:
        return majority_element
    else:
        return None
        

arr = [2,2,1,1,1,2,2]
N= 7
print(findnum(arr, N))      # Output:- 2