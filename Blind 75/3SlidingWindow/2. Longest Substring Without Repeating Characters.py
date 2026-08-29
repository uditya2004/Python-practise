"""
Given a string s, find the length of the longest substring without repeating characters.

A substring is a contiguous non-empty sequence of characters within a string.
"""

# Method 1:- Using 2 pointers and a list :- Brute Force
#TC: O(N^2)
#SC: O(N)

def lengthOfLongestSubstring(s):
    
    length = 0
    for i in range(0, len(s)):
        temp_seq = []       # SC: O(N)

        for j in range(i, len(s)):
            
            if s[j] not in temp_seq:
                temp_seq.append(s[j])
                length = max(length, len(temp_seq)) #Update the length
            else:
                break

    return length



s = "pwwkew"  #Expected output :- 1
print(lengthOfLongestSubstring(s))

#=========================
# Method 2:- Variable Size Sliding Window
# TC: O(2N) = O(N) => j move n times
#                     i moves at most n times in total (amortized O(1) per step)
# SC: O(1)
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0  # length of longest substring

        n = len(s)
        hash = {}   # { value: count }
        i = 0
        j = 0
        while j < n:
            # 1. calculation
            # Add element frequency to hash
            hash[s[j]] = hash.get(s[j], 0) + 1

            # 2. shrink
            # if the element frequency is > 1, that means we have duplicate, so move i until we remove duplicate
            while hash[s[j]] > 1:  
                hash[s[i]] -=1    # reduce s[i] frequency

                if hash[s[i]] == 0:  # while reducing freqency, if frequency becomes 0, then remove the element from hash
                    del hash[s[i]]

                i +=1

            # 3. record
            # when the frequency again becomes 1, means removed duplicate, so window size is candidate answer to record
            if hash[s[j]] == 1:
                result = max(result, j-i+1)

            # 4. move
            j +=1

        return result


obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))

#=========================================
# Method 3:- Best solution => we reduced inner while loop to simply "if condition"
# TC:- O(N)  => j moves n times; i jumps in O(1)
# SC:- O(1)
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0  # length of longest substring

        hash = {}    # { value: index }

        n = len(s)
        i = 0
        j = 0
        while j < n:

            # If the element s[j] is already in hash and is last seen inside the window, then s[j] is a duplicate element, so we move i ahead of last seen index of s[j] i.e i = hash[s[j]] + 1
            """
            - The dict holds the last index of every character ever seen — including ones that already fell outside the window.  That's why we add extra condition "and hash[s[j]] >= i"
            """
            if s[j] in hash and hash[s[j]] >= i:
                i = hash[s[j]] + 1

            # Update the last seen index of current character (overwrite)
            hash[s[j]] = j

            # Update max length
            result = max(result, j-i+1)

            # move
            j +=1

        return result


obj = Solution()
s = "baaabca"
print(obj.lengthOfLongestSubstring(s))