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
# Method 2:- Sliding window with set
"""
TC:- O(2N)  = O(N)
    - The right pointer moves from 0 to n-1, visiting each character exactly once.
    - The left pointer also moves from 0 to at most n-1

SC:- O(N) => If all characters are unique, the set holds n characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = set()

        maxLength = 0
        n = len(s)

        left = 0
        right = 0
        while left <= right and left <  n and right < n:
            if s[right] in occur:
                # move the left pointer till we remove duplicate element from the window
                while s[right] in occur:
                    occur.remove(s[left])
                    left +=1

            if s[right] not in occur:
                occur.add(s[right])    # Adding the s[right] element to set
                maxLength = max(maxLength, (right - left) + 1)   # Updating the maxlength
                right +=1   # moving right forwards
        
        return maxLength


obj = Solution()
s = "pwwkew"
print(obj.lengthOfLongestSubstring(s))


#=========================
#Method 3:- Using 2 pointers Sliding window :- Best Solution
"""
- We can optimize method 2 by educing the number of operations:
    - Method 2 may move left one step at a time when a duplicate is found. 
    - But We can jump directly to the position after the duplicate using a hashmap instead of a set.
"""
#TC: O(N)
#SC: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        maxlength = 0
        n = len(s)

        left = 0 
        right = 0
        while left <= right and left < n and right < n:
            
            # If the character is already present in the dictionary and is between left and right , then current element (s[right]) is a duplicate
            if s[right] in hash and hash[s[right]] >= left:
                # we move the left pointer ahead of the duplicate element index
                left = hash[s[right]] + 1

            # Update the last seen index of current character (overwrite)
            hash[s[right]] = right

            # Update max length
            maxlength = max(maxlength, (right - left) + 1)

            # move right pointer forward
            right +=1
        
        return maxlength



obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))