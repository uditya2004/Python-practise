#Two Pointers:- Brute Force
#TC: O(N^2)
#SC: O(26) = O(1)
def characterReplacement(s, k):
    
    res = 0
    for i in range(0,len(s)):
        hash = {}        # {element: freq} . In worst case it can store all unique alphabet i.e 26 . SC(26)
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
"""
- Use a sliding window with left pointer i and right pointer j
- Keep a hash map to count character frequencies in the current window
- Track max_freq = max frequency of any character seen so far (only update upwards, never shrink it)

(Note -> (j - i + 1) - max_freq = Number of replacements needed) 

- Validity condition: (j - i + 1) - max_freq <= k → window is valid
- Invalid condition: (j - i + 1) - max_freq > k → shrink from left
    - Decrease hash[s[i]] by 1
    - Increment i

- After ensuring validity, update res = max(res, j - i + 1)
"""
#Best Solution Sliding window
# TC: O(N)
# SC: O(26) = O(1)
def characterReplacement(s, k):
    res = 0
    hash = {}    # In the worst case, it can store all unique characters (English letters i.e 26) in the string

    i = 0        # Left Pointer
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