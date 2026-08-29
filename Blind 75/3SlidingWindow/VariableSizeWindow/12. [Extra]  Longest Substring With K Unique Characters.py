"""
https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 
"""
#Variable Size Sliding Window
# TC: O(n)  -> j moves n times; 
#              i moves at most n times total — not n per iteration (amortized), 
#              dict ops are O(1)

# SC: O(k)  -> map holds at most k+1 distinct chars; bounded by 26 (lowercase) => O(1)
class Solution:
    def longestKSubstr(self, s, k):
        result = -1  # length of max possible substring
        seenChar = {}   # {value: frequency}

        n = len(s)
        i = 0
        j = 0
        while j < n:
            # 1. Calculation
            # add the frequency of the element to the "seenChar"
            seenChar[s[j]] = seenChar.get(s[j], 0) + 1

            # 2. Shrink
            while len(seenChar) > k:
                # decrease the frequency of s[i] element and move i
                seenChar[s[i]] -=1

                if seenChar[s[i]] == 0:
                    del seenChar[s[i]]

                i +=1
                        
            # 3. Record
            if len(seenChar) == k:
                result = max(result, j-i+1)

            # 4. Move
            j += 1

        return result


obj = Solution()
s = "aabacbebebe"
k = 3
print(obj.longestKSubstr(s, k))