def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):    # i -> n-1 to 1

        for j in range(0, i):      # j -> 0 to i-1 , as we are comparing element with the adjacent next element. If we go till "i" we will exceed list index.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr = [1,6,2,4,9]
print("Original List: ", arr)
print("Sorted List: ", BubbleSort(arr))