"""
CONCEPT:
- We use single array only (no chaing formation)
- Condition for open addressing:-
        1. No. of slots in hash table >= No. of key to be inserted

Advantage:-
- Cache Friendly (contiguous location storage)

Ways to do open addressing:-
    1. Linear Probing  -> Linearly Search for next empty Slot
    2. Quadratic Probing
    3. Double Hashing
"""
#========================================================
#========================================================

#LINEAR PROBING 

"""
Searching Algo:
1. Find the hash_value using the hash_function
2. We go to that index and we compare:
        - If we find it , return True
        - Else we linearly search and do not stop on encountering "deleted" slot:-
                - We stop when:-
                        - We found the element
                        - encountered a empty box
                        - research the starting position again.(Traverse through the whole table)
"""

"""
DELETE Algo:
1. Search for the element
2. Remove the element and place "deleted" string in place of the element in the box.
                Problem with simply deleting the element -> Search operation will stop after encountering empty box.     
"""

#========================================================

"""
PROBLEM OF CLUSTER FORMATION:-

1. For Linear Probing :- We have issue of Primary Cluster
2. For Quadratic Probing :- We have issue of Secondary Cluster
"""

#========================================================
#========================================================
"""
Quadratic Probing
Disadvantage with Quadratic Probing:-
- It might happen it is not able to find empty slot even if there are empty slot present.

"""

#========================================================
"""
Mathematical formulas:-

1. Linear Probing    -> hash(key,i) = (h(key) + i) % m
2. Quadratic Probing -> hash(key,i) = (h(key) + i^2) % m
3. Double Hashing    -> hash(key,i) = (h1(key) + i*h2(key)) % m

"""