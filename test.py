arr = [1, 3, 2, 5, 3]
arr_max = max(arr)

hash_table = [0]* (arr_max+1)

for i in arr:
    hash_table[i] +=1

print(hash_table)