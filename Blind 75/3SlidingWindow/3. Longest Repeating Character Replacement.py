"""
- You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
- s consists of only uppercase English letters.
- Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""
#Brute Force sliding window
#TC: O(N^2)
#SC: O(26) = O(1)
def characterReplacement(s, k):
    
    res = 0
    for i in range(0,len(s)):
        hash = {}             # In worst case it can store all unique alphabet i.e 26 . SC(26)
        max_freq = 0

        for j in range(i, len(s)):

            # As j moves we keep hash and max_freq updated at every step
            hash[s[j]] = 1 + hash.get(s[j], 0)    
            max_freq = max(max_freq, hash[s[j]])

            if (j-i+1) - max_freq <= k:      # (j-i+1) - max_freq = no. of alphabet we can change, where (j-i+1) is the length of current window
                res = max(res, j-i+1)
            else:
                break                        # for moving the left pointer i.e "i"

    return res

s = "ABAB"
k = 1
print(characterReplacement(s, k))

#=================
#Best Solution Sliding window
# TC: O(N)
# SC: O(26) = O(1)
def characterReplacement(s, k):
    res = 0
    hash = {}    # In the worst case, it can store all unique characters (English letters i.e 26) in the string

    i = 0
    max_freq = 0

    for j in range(0, len(s)):

        # As j moves we keep hash and max_freq updated at every step
        hash[s[j]] = 1 + hash.get(s[j], 0)
        max_freq = max(max_freq, hash[s[j]])

        while (j-i+1) - max_freq > k:     # As long as (j-i+1) - max_freq > k, move the left pointer i.e "i" . 
            hash[s[i]] -=1                # Decreasing the count of that alphabet, as it's no longer in current window , as we moved pointer "i"
            i +=1

        res = max(res, j-i+1)            # Now it will be (j-i+1) - max_freq <= k, it is our desired window , so update the res

    return res


s = "ABAB"
k = 1
print(characterReplacement(s, k))