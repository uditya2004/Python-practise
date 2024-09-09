def reverse(arr, p1, p2):
    if p1>=p2:
        return arr
    
    else:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        return reverse(arr, p1+1, p2-1)


array = [10,20,30,40]

print(reverse(array, 0, len(array)-1))