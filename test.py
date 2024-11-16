# TC: O(N*MlogM)
# SC: O(N)

# from collections import defaultdict

# def groupAnagrams(strs):
#     dict1 = defaultdict(list)

#     for i in strs:
#         sorted_s = "".join(sorted(i))
#         dict1[sorted_s].append(i)
    
#     return list(dict1.values())
    

# strs = ["act","pots","tops","cat","stop","hat"]

# print(groupAnagrams(strs))


# TC: O(N*N)
# SC: O(N)

from collections import defaultdict

def groupAnagrams(strs):
    dict1 = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ ord(char) - ord("a") ] +=1

        dict1[tuple(count)].append(word)
    
    return list(dict1.values())
    

strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))