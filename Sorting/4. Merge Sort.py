def merge(arr,low,mid,high):
    temp=[]
    left=low
    right= mid + 1

    while left<=mid and right<=high:   # while we have elements remaining on both left and right half
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        
        else:
            temp.append(arr[right])
            right +=1
    
    while left<=mid:        #if right half is exhausted and left one, elements remains . Then we straightaway add all the elements of the left half
        temp.append(arr[left])
        left +=1
    
    while right<=high:      #if left half is exhausted and right one, elements remains
        temp.append(arr[right])
        right +=1
    

    #placing all the elements from temp array to arr
    for i in range(low,high+1):
        arr[i] = temp[i-low]

    return arr


def mergeSort(arr,low,high):
    if low>=high:
        return
    middle= (low+high) // 2     #we have to divide the array into 2 parts , so we find the middle index

    mergeSort(arr, low, middle)         #We tell the function to return the sorted left half of the array
    mergeSort(arr, middle+1, high)      #We tell the function to return the sorted right half of the array
    merge(arr,low,middle,high)         # We merge both the halfs

    return arr

lst=[3,2,4,1,3]

print(mergeSort(lst,0,len(lst)-1))


#--------------------------------------
