"""
- Observations:
    - Any permutation of s1 will have same length as s1
    - All the permuation will have same hash array signature
- So we have to check all the possible windows of size fixed as length of s1
- Hence a problem of fixed sized sliding window.
"""

# Method:- Using Fixed window size sliding window technique

# TC: O(n + m)
# SC: O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        # building signature of s1
        hash1 = [0]*26
        for ch in s1:
            hash1[ord(ch) - ord('a')] +=1
        

        hash2 = [0]*26
        i = 0 
        for j, item in enumerate(s2):
            # Add current element at j to window
            hash2[ord(item) - ord('a')] +=1

            # If window size exceeds len(s1), shrink from left
            if j-i+1 > len(s1):
                hash2[ord(s2[i]) - ord('a')] -=1
                i +=1
            
            # Check if window size equals len(s1) and signatures match
            if j-i+1 == len(s1) and hash1 == hash2:
                # valid window
                return True
        
        return False


obj = Solution()
s1 = "ab" 
s2 = "eidbaooo"
print(obj.checkInclusion(s1, s2))