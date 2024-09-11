"""
CONCEPT
Note:
- We create an array of size = max element present in that array.
- we store element's frequency at their own index (eg: frequency of element "2" will be stored at index 2). This allows constant time access to data because you don't need to search for the element; you know exactly where it is stored.

"""

#===============================

"""
Ques 1:- Given an array of integers: [1, 2, 1, 3, 2] and we are given some queries: [1, 3, 4, 2, 10]. For each query, we need to find out how many times the number appears in the array. 

- Building the hash table takes O(N) time, where N is the size of the array.
- Fetching the frequency for each query takes O(1).
- For Q queries, the total time complexity is O(N + Q)
"""

# Method 1: Using a List (Array-Based Hashing) or direct mapping


arr = [1, 3, 2, 5, 3]
max_value = max(arr)
hash_table = [0] * (max_value + 1)  # Create array of size (max_value + 1)

for num in arr:
    hash_table[num] += 1  # Store frequency at the number's index

print(hash_table)  # Output: [0, 1, 1, 2, 0, 1]