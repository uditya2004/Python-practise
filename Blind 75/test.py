class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        length = 0

        i = 0
        j = i

        while i < len(s) and j < len(s):

            if s[j] in dict1:
                if dict1[s[j]] >= i:
                    i = dict1[s[j]] + 1
            
            # By above "if condition" we made the invalid window valid again, so we can continue with below steps as usual
            length = max(length, j-i+1)
            dict1[s[j]] = j
            j +=1
        
        return length      


obj = Solution()
s = "pwwkew"
print(obj.lengthOfLongestSubstring(s))