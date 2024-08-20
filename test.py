def Merge(arr, low, middle, high):
    temp = []
    left = low
    right = middle + 1

    while left <= middle and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        
        else:
            temp.append(arr[right])
            right +=1
    
    while left <= middle:
        temp.append(arr[left])
        left +=1
    
    while right <= high:
        temp.append(arr[right])
        right +=1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]
    
    return arr

def MergeSort(arr, low, high):
    if low >= high:
        return
    
    middle  = (low + high) // 2

    MergeSort(arr, low, middle)
    MergeSort(arr, middle + 1, high)
    Merge(arr, low, middle, high)

    return arr


arr=[3,2,4,1,3]

print(MergeSort(arr, 0, len(arr)-1))