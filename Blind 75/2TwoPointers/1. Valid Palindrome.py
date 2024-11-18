"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
#Using Two Pointers
#TC: O(N/2) = O(N)
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