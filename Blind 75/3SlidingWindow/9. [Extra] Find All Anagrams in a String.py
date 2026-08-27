"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

# Count Occurences of Anagrams
# TC:- O(N)      -> each index enters/leaves the window once; dict comparison is O(26) = O(1)
# SC:- O(1)      -> dict1 + dict2 hold at most 26 distinct chars (O(N) if the result list is counted)
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        dict1 = {}
        for char in p:
            dict1[char] = dict1.get(char, 0) + 1

        # FIXED SIZE Sliding Window
        result = []   # count of anagram
        dict2 = {}
        n = len(s)
        k = len(p)
        i = 0
        j = i
        while j < n:
            # 1. calculation
            # add the frequency to dict2
            dict2[s[j]] = dict2.get(s[j], 0) + 1

            # 2. Shrink
            if j-i+1 > k:
                dict2[s[i]] = dict2.get(s[i], 0) - 1   # remove the element frequency 

                if dict2[s[i]] == 0:   # if frequency reaches 0, remove the element from dict, so it can eventually matches dict1
                    del dict2[s[i]]
                i += 1

            # 3. Record
            if j-i+1 == k:
                if dict2 == dict1:
                    result.append(i)   # appending the start index of the found anagram

            # 4. Move
            j += 1

        return result


obj = Solution()
s = "cbaebabacd"
p = "abc"
print(obj.findAnagrams(s, p))