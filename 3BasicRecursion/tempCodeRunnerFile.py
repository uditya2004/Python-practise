def reverse(n, arr, left):
    if left >= n- left - 1:
        return arr
    
    else:
        arr[left], arr[n-left-1] = arr[n-left-1], arr[left]
        return reverse(arr, left+1, n-left-1-1)


array = [10,20,30,40]

print(reverse(len(array), array, 0))