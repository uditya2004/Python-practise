def PlacePivot(arr,low,high):
    pivot=arr[low]    # we take 1st element of the array as Pivot
    i=low
    j=high

    while i<j:     #We keep on doing this until i and j cross each other
        while arr[i]<=pivot and i<=high-1:  # We have to stop at the element greater than pivot, so until then we will continue to move
            i +=1
        
        while arr[j]>pivot and j>=low+1:   ## We have to stop at the element lesser than pivot, so until then we will continue to move
            j -=1
        
        if i<j:   #We perform swap only if i and j haven't crossed each other
            arr[i],arr[j] = arr[j], arr[i]
    
    arr[low],arr[j]= arr[j], arr[low]   # placing the pivot at it's correct place

    return j     # j will be the partition index


def quickSort(arr,low,high):
    if low<high:    # we only sort if the array has more than 1 element
        partitionIndex= PlacePivot(arr,low,high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)
    
    return arr

lst=[4,6,2,5,7,9]
print(quickSort(lst,0,len(lst)-1))
