
def reverse(arr, low, high):
    
    while low<high:
        arr[low], arr[high] = arr[high], arr[low]
        low +=1
        high -=1
    
    return arr

arr = [1,3,2]
print(reverse(arr, 0, len(arr)-1))