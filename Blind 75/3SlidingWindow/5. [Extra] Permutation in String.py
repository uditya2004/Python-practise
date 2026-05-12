"""
- Observations:
    - Any permutation of s1 will have same length as s1
    - All the permuation will have same hash array signature
- So we have to check all the possible windows of size fixed as length of s1
- Hence a problem of fixed sized sliding window.
"""

# Method:- Using Fixed window size sliding window technique

#TC: O(2n + m) =  O(m) , where n = len(s1), m = len(s2)
# SC: O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len(s1) > len(s2) then permutations of s1 can't exist in s2
        if len(s1) > len(s2):
            return False
            
        hash1 = [0] * 26   # contains signature of s1
        hash2 = [0]*26     # contains current window signature

        # make signature of s1 in hash array
        for i in range(len(s1)):
            hash1[ord(s1[i]) - ord('a')] +=1

        # building the initial window -> by moving j till len(s1) and building hash2
        i = 0 
        j = 0
        for x in range(len(s1)):
            hash2[ord(s2[j]) - ord('a')] +=1
            j+=1
        
        # checking initial window
        if hash1 == hash2:
            # permutation found
            return True
        
        while j < len(s2):

            # making current window
            hash2[ord(s2[j]) - ord('a')] +=1  # adding element at j
            hash2[ord(s2[i]) - ord('a')] -=1  # removing element at i
            
            # checking current window
            if hash1 == hash2:
                # permutation found
                return True
            
            # preparing next window by moving pointers
            i +=1
            j +=1
            
        return False


obj = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(obj.checkInclusion(s1, s2))