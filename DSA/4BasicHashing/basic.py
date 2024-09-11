"""
Hashing useful for below task because of O(1) TC :
    1. Search
    2. Insert
    3. Delete

Not Useful for:
    1. Finding closest value  -> We use AVL or Red black Tree
    2. Keeping Sorted Data    -> We use AVL or Red black Tree
    3. Prefix Searching       -> We use Trie Data Structure
"""
array = [1,3,2,1,3]

query_count = 5
for i in range(0,query_count):
    num = int(input("Enter a number:- "))
    hashfunc(array, n)