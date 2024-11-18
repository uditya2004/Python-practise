#Sort and compare s and t

# def isAnagram(s, t):
#     new_s = "".join(sorted(s))
#     new_t = "".join(sorted(t))

#     return new_s == new_t

# s = "rat"
# t = "car"
# print(isAnagram(s, t))

#Store frequency in dict
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    print(count_t)
    print(count_s)
    # return count_s == count_t



s = "rat"
t = "car"
print(isAnagram(s, t))