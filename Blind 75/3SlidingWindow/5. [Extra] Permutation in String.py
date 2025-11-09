# Method 1:- Using Fixed window size sliding window technique

# TC: O(N + M)
    # N:- Length of s1
    # M:- Length of s2
 
# SC: O(26 + 26) = O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # Creating signature of s1 string
        # Every Permutation of s1 will have same signature (count1 array).
        count1 = [0]*26
        for element in s1:
            count1[ord(element) - ord('a')] +=1
        
        i = 0
        j = i
        count2 = [0]*26

        while j < len(s2):
            count2[ord(s2[j]) - ord('a')] +=1
            
            # On adding s2[j], if the window size exceed n, we decrease size by moving i forward
            if j-i+1 > n:
                count2[ord(s2[i]) - ord('a')] -=1
                i +=1
            
            # Once the window now valid, we check:- if the "signature of s1" == "signature of substring in s2" , then we found a permutation
            if count1 == count2:
                return True
            
            j +=1

        return False



obj = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(obj.checkInclusion(s1, s2))