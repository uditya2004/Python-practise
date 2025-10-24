class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = [0]*26

        for element in s1:
            hash[ord(element) - ord('a')] +=1
        

        for element in s2:
            hash_index = hash[ord(element) - ord('a')]
            if hash[hash_index] >= 1:
                hash[hash_index] -=1
        
        for element in hash:
            if element != 0:
                return False
        
        return True

obj = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(obj.checkInclusion(s1,s2))