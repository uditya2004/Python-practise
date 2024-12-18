"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
"""
#Using Sorting
#TC: NLogN + MlogM
#SC: O(N + M)

def isAnagram(s, t):
    temp_s = ''.join(sorted(s))    #TC: NlogN
    temp_t = ''.join(sorted(t))    ##TC: MlogM

    if temp_s == temp_t:
        return True
    else:
        return False  


s = "rat"
t = "car"

print(isAnagram(s, t))


#===============
# Using Dictionary - Better Solution
# TC: O(N)
# SC: O(N)
def isAnagram(s, t):
    count_s = {}
    count_t = {}

    #Edge Case
    if len(s) != len(t):
        return False

    #Finding the count of characters in both "s" and "t"
    """
    - .get() method in Python is used with dictionaries to retrieve the value associated with a specified key.
    - If the key is not found in the dictionary, .get() returns a default value
    """
    for i in range(0,len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)          
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    """
    The comparison(count_s == count_t) checks:

    - Keys: Both dictionaries must have the exact same set of keys.
    - Values: For each key, the corresponding values in both dictionaries must be equal.
    If both conditions are met, the dictionaries are considered equal. Otherwise, they are not.
    """
    return count_s == count_t
    


s = "rat"
t = "car"

print(isAnagram(s, t))


#===============
# Using array as hash table - Best Solution
# TC: O(N)
# SC: O(26) = O(1)
def isAnagram(s, t):
    
    #Edge Case
    if len(s) != len(t):
        return False
    
    count = [0]*26   # As ABC has 26 alphabet , we initialize array of size 26

    for i in range(0, len(s)):
        count[ord(s[i]) - ord("a")] +=1     # Increment count for `s`
        count[ord(t[i]) - ord("a")] -=1     # Decrement count for `t`

    #If it's anagram then the array will be [0]*26 again , as we added and subtracted same number of times
    for j in count:
        if j != 0:
            return False
        
    return True
    
s = "a"
t = "ab"

print(isAnagram(s, t))


#==============
# Shortcut - Dont't use
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
