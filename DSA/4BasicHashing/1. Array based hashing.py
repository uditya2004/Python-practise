"""
CONCEPT
- We create an array of size = max element present in that array.
- eg: frequency of element "2" will be stored at index 2. This allows constant time access to data because you don't need to search for the element; you know exactly where it is stored.

STEPS
1. Create an hash_table or frequency_array, having size = max element in the array
2. Store the frequency of each element at there respective index
"""

#===============================

"""
Ques 1:- Given an array of integers: [1, 2, 1, 3, 2] and we are given some queries: [1, 3, 4, 2, 10]. For each query, we need to find out how many times the number appears in the array. 

- Building the hash table takes O(N) time, where N is the size of the array.
- Fetching the frequency for each query takes O(1).
- For Q queries, the total time complexity is O(N + Q)
"""

# Method: Array-Based Hashing (Direct Mapping)


# arr = [1, 3, 2, 5, 3]
# max_value = max(arr)

# hash_table = [0] * (max_value + 1)  # Create array of size (max_value + 1)  (i.e [0,0,0,0,0,0])

# for num in arr:
#     hash_table[num] += 1  # Store frequency at the number's index

# print(hash_table)  # Output: [0, 1, 1, 2, 0, 1]


#========================================
#CHARACTER HASHING
"""
Ques 2: you are given the string "abcdabefc" and need to answer how many times certain characters appear.

Concept:-
- We use ASCII values of "a to z" and map "a to index 0" and "z to index 25" . So we make an array of length 26.

"""

def build_hash_table(str1, char_hash_table):
    for i in str1:
        hash_value = ord(i)-ord('a')         #The ord() function returns the ASCII value of a character. 
        char_hash_table[hash_value] +=1
    
    return char_hash_table

def fetching(char_hash_table, key):
    hash_value = ord(key)-ord('a')
    return char_hash_table[hash_value]

# Sample string and queries
char_hash_table = [0] * 26        
str1 = "abcdabefc"
char_queries = ['a', 'g', 'h', 'b', 'c']

char_hash_table = build_hash_table(str1, char_hash_table)

for query in char_queries:
    print(f"{query} occurs {fetching(char_hash_table, query)} times")

