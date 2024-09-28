def Search(arr,key, low, high):
    if high<low:
        return -1
    else:
        mid = (low+high)//2
        if key == arr[mid]:
            return mid
        
        elif key< arr[mid]:
            return Search(arr,key, low, high-1)
        else:
            return Search(arr,key, low+1, high)


    

lst=[3,2,5,6]
low = 0
high = len(lst)-1
key = 5

print("Index of ", key," is:",Search(lst,key,low,high))