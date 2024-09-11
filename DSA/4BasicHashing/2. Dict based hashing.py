# Method 2: Using a Dictionary (Hash Map-Based Hashing)

"""
- When you have very large numbers as element of array (like 10^9), using a direct-mapping approach to create an array of size 10^9 +1 is not feasible because it requires too much memory. Instead of creating a huge array, we can use a dictionary (hash map) in Python , where dictionary size = no. of unique elements in an array.

STEPS FOR HASHING
Here's how you can use hashing:

Step - 1: Pre-storing: We first create a dictionary to store how many times each number appears in the array.
Step - 2: Fetching: For each query, we just fetch the frequency from the dictionary.
"""

def build_hash(arr):

    hash_table = {}        #Empty Dictionary
    for num in arr:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1
    return hash_table

def fetch_frequency(hash_table, query):
    return hash_table.get(query, 0)                 # .get() is use to find the value associated with the key. Syntax: dictionary.get(key, default_value)

# Sample array and queries
arr = [1, 2, 1, 3, 2]
queries = [1, 3, 4, 2, 10]

# Build the hash table (pre-storing frequencies)
hash_table = build_hash(arr)


# # Fetch the frequency for each query
for q in queries:
    print(f"{q} occurs {fetch_frequency(hash_table, q)} times.")



#========================================
#CHARACTER HASHING
"""
Ques 2: you are given the string "abcdabefc" and need to answer how many times certain characters appear.
"""

def build_hash(s):
    dict1 = {}

    for character in s:
        if character in dict1:
            dict1[character] +=1
        else:
            dict1[character] =1
    
    return dict1

def fetching(hash_table, query):
    return hash_table.get(query, 0)


# Sample string and queries
s = "abcdabefc"
char_queries = ['a', 'g', 'h', 'b', 'c']

hash_table = build_hash(s)

for query in char_queries:
    print(f"{query} occurs {fetching(hash_table, query)} times")




# Creating an array of size N+1
N = 5
frequency = [0] * (N + 1)  # An array with 6 slots: [0, 0, 0, 0, 0, 0]

# If we have an array like this: [2, 3, 5, 3, 2, 5, 0]
arr = [2, 3, 5, 3, 2, 5, 0]

# Count the frequency of each number in the array
for num in arr:
    frequency[num] += 1
    print(frequency,"\n \n")

# Now, let's see the frequency array
print(frequency)
