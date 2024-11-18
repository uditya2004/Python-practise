"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
"""
#Using dictionary + sorting
#TC: O(N* NLogN)
#SC: O(N*K)          (The space complexity for sorting a string of length k is O(k). Since this is done for each of the n strings, the total auxiliary space for sorting is O(n * k).)
 
from collections import defaultdict

def groupAnagrams(strs):

    res = defaultdict(list)           # if we access a key that doesn’t exist in dictionary, it automatically creates that key and initializes it with an empty list ([]).
    
    for s in strs:
        sortedS = ''.join(sorted(s))  #TC: O(NLogN), SC: O(K)  ## making the string , a sorted string
        res[sortedS].append(s)        # We made the sorted string as the key, and appended every string whose sorted order matched with the key, to the list value associated with that key.
    
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))


#============
#Using dictionary + array hashmap  - Best solution
#TC: O(N*K),  where N is the number of words in list and k is the character in the word
#SC: O(N + N*26) = O(N)

from collections import defaultdict

def groupAnagrams(strs):

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26                   # it's like storing a code for a word, all anagrams will have same code
        for char in word:                  # iterating a single word for every c
            count[ord(char) - ord('a')] += 1

        res[tuple(count)].append(word)     # code is the key and all the words with same code are appended to the list associated with that key. (Here we made the key as "tuple datatype" as dictionary key shoulbe be of immutable type

    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))



