def rev(arr, low , high):
    if low >= high:
        return arr
        
    else:
        arr[low], arr[high] = arr[high], arr[low]
        return rev( arr, low+1, high-1)
        


array = [40,30,20,10]
print(rev(array, 0, len(array)-1))