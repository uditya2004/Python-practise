"""
Methods to handle collision:-
1. Chaining -> We create extra space here (e.g., linked lists) 
2. Open addressing -> We don't create extra space here , rather we find the next free slot in the array
        i. Linear Probing
        ii. Quadratic Probing
        iii. Double Hashing
"""

# CHAINING

class MyHash:
    def __init__(self, n):
        self.bucket_size = n
        self.hash_table = [[] for _ in range(self.bucket_size)]          #Output: [[], [], [], [], [], [], []]
    
    def insert(self, value):
        hash_value = value %  self.bucket_size
        self.hash_table[hash_value].append(value)
    
    def search(self, key):
        hash_value = key %  self.bucket_size
        return key in self.hash_table[hash_value]

    def remove(self, key):
        hash_value = key %  self.bucket_size
        if key in self.hash_table[hash_value]:
            self.hash_table[hash_value].remove(key)
        else:
            print(f"Key {key} is not present")


"""

BUCKET = 7
So, HASH_FUNCTION = x % BUCKET = x % 7

"""
h = MyHash(7)

h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.hash_table)

print("Searching 56:- ", h.search(56))       #Output:- True

h.remove(56)
print(h.hash_table)

print("Searching 56:- ", h.search(56))       #Output:- False

h.remove(57)