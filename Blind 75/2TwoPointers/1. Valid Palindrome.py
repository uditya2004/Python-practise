"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
#Using Two Pointers
#TC: O(N)
#SC: O(1)
def isPalindrome(s):

    if len(s) == 0:
        return True
    
    low = 0
    high = len(s)-1
    while low<high:

        if not s[low].isalnum():
            low +=1

        elif not s[high].isalnum():
            high -=1

        elif s[low].lower() != s[high].lower():
            return False
        else:
            low +=1
            high -=1
    return True




s = ""
print(isPalindrome(s))


#==============================
# Method 2:- Inner loop
#TC: O(N)
#SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # empty string is a palindrom
        if len(s) == 0:
            return True
        
        left = 0
        right = len(s)-1

        while left < right:

            # move left till it reaches alphanumeric
            while left < right and not s[left].isalnum():
                left +=1

            # move right till it reaches alphanumeric
            while left < right and not s[right].isalnum():
                right -=1

            # now that both on alphanumeric, compare
            if s[left].lower() != s[right].lower():
                return False
            else:
                left +=1
                right -=1
        
        return True
            

obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))