array = [67, 44, 82, 17, 20]
n = len(array)

for i in range(0, n):   # We choose every element in an array one by one.
    j = i
    
    while (j > 0) and (array[j-1] > array[j]):       #we go till j=1 as we have to compare j to j-1 . If we go till j=0 we will get runtime error.
        array[j], array[j-1] = array[j-1], array[j]  #swap
        j = j-1

print(array)