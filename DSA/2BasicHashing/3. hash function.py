"""
Hash Function:-
- Hash table size is dependent upon how many key you want to insert in hash table
        - eg:- if you want to store 100 phn no. , then size of hash table will be around 100 (can be 100, 200,400 etc.)

- To find which phn no. will go to which slot of hash table we use "HASH FUNCTION"
        - "HASH FUNCTION" is a function that takes elements (large numbers, strings, float etc) as input and give small values as output which can be used as index in the hash table.
                Eg- If hash table size is 200, hash function take a phn no. of 10 digit and generate a value in range 0 to 199. 
        
        - Eg of Hash function -> h(large_value) = large_value % m
                    - Generally the value of m is chosen as a prime number close to hash table size because we will have less factors and have better distribution of large keys . We take prime number not close to 2's or 10's power.
                    - Bad value of m is -> any power of 2 or power of 10
"""