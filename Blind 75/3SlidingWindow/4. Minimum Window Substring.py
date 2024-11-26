"""
- Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

- The testcases will be generated such that the answer is unique.
- s and t consist of uppercase and lowercase English letters.
"""
# Two Pointers - Brute Force
# TC: O(N^2)
#SC: O(M), m is the length of t

def minWindow(s, t) :
    resLen = float("inf")           # as we need minimum len, thus initialized with "inf"
    resStart = -1

    for i in range(0, len(s)):

        count = 0         # no. of character of "t" found in current window

        hash = {} #SC: O(M)
        for k in t:        # Pre-inserting all character of t in hashmap "hash"
            hash[k] = 1 + hash.get(k, 0)

        
        for j in range(i, len(s)):

            # As we iterate through pointer j , we always decrement frequency of element in hash
            # if the element is not in hash, we initialize it to 0 and then decrement to make it's freq -ve
            if hash.get(s[j], 0) > 0:   # checking if s[j] was a pre-inserted element (if it's >0 it means it was pre-inserted), if it is preinserted we got one element of t in s, so increment "count"
                count +=1

            hash[s[j]] =  hash.get(s[j], 0) - 1   # We decrement the frequency as we move the pointer j, for every element in s

            if count == len(t):
                resLen = min(resLen, j-i+1)
                resStart = i
                break
    
    if resStart == -1:
        return ""
    else:
        return s[resStart: resStart + resLen]


s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
print(minWindow(s, t))

#==================================
# Sliding window - Best Solution
# TC: O(N)
#SC: O()

def minWindow(s, t) :

    hash = {}
    for k in t:             # Preinserting the characters in t
        hash[k] = 1 + hash.get(k, 0)
    
    resLen = float("inf")    # length of the possible substring , we want it to be minimum
    resStart = -1            # starting index of the possible substring
    count = 0                # no. of char of t found in s in the current window

    l = 0
    r = 0
    while r < len(s):
        # Process the right pointer
        if s[r] in hash:
            if hash[s[r]] > 0:
                count += 1
            hash[s[r]] -= 1

        # Shrink the window from the left if it's valid
        while count == len(t):
            if r - l + 1 < resLen:
                resLen = r - l + 1
                resStart = l

            if s[l] in hash:  # Only adjust if s[l] is in t
                hash[s[l]] += 1
                if hash[s[l]] > 0:
                    count -= 1
            l += 1

        r += 1

    # Return the result
    if resStart == -1:
        return ""
    else:
        return s[resStart: resStart + resLen]


# Example Usage
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
print(minWindow(s, t))


#==============================
# Sliding window - Best solution
# TC: O(N)

# def minWindow(s, t) :

#     if t == "":      # Edge case
#         return ""

#     hash = {}
#     window = {}

#     for i in t:
#         hash[i] = 1 + hash.get(i, 0)     # storing the frequency of all elements in t
     
    
#     have = 0                    # no. of characters of t we currently have in s
#     need = len(hash)          # Why we need unique? we need these many characters in our possible substring

#     res = [-1,-1]               # result stores the start and end index of possible answer (substring)
#     resLen = float("inf")       # length of possible answer substring, as we need length to be minimum so we initialize it with inf
#     l = 0                       # Left pointer, initialize at the start of string
    
#     for r in range(len(s)):     # right pointer 
#         c = s[r]
#         window[c] = 1 + window.get(c, 0)             # storing the frequency of char where pointer is at.

#         if c in hash and window[c] == hash[c]:   # we don't care about the char which are not in hash
#             have +=1
        
#         while have == need:
#             #update our result
#             if (r-l+1) < resLen:
#                 res = [l, r]       
#                 resLen = (r-l+1)
            
#             #pop from the left of our window
#             window[s[l]] -=1                                     # decrementing the frequency as we move the "l" pointer
#             if s[l] in hash and window[s[l]] < hash[s[l]]:   # if the removed elemnent from back was a part of "t" , then we decrement the "have", as now we will be in need of that 1 removed character
#                 have -=1

#             l +=1     # moving the left pointer forward
    
#     l,r = res

#     if resLen != float("inf"):
#         return s[l:r+1]
#     else:
#         return ""

# s = "aaaaaaaaaaaabbbbbcdd"
# t = "abcdd"
# print(minWindow(s, t))

