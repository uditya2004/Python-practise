#Method 1: Using Temporary Array
# TC: O(N)
# SC: O(N)  {Using temp array "temp"}

def check_pal(str):
    temp = ""
    for i in range(len(str)-1, -1, -1):
        temp = temp + str[i]

    if temp == str:
        print("True")
    else:
        print("False")


str1 = "ABCDCBA"
check_pal(str1)

#============================
#Method 2: Using 2 Pointer (Run a for loop till half the length of the string in order to check the first and last character of the string.)
# TC: O(N/2) = O(N)
# SC: O(1)  

def check_pal(str, low , high):
    mid = (low + high) // 2

    while low<mid or high>mid:
        if str[low] != str[high]:
            return False
        else:
            low = low + 1
            high =high - 1
    
    return True        


str1 = "ABCDCBA"
print(check_pal(str1, 0, len(str1) - 1))

#===========================================
# Method 3: Recursion:- Functional Recursion - Using 2 Pointer variable
 # TC:- O(N/2)
 # SC:- O(N/2)   {N/2 function call will be waiting}

def check_pal(str, low , high):
    if low>=high:                 #BASE CASE
        return True
    else:
        if str[low] != str[high]:
            return False
        
        return check_pal(str, low + 1 , high - 1)


str1 = "ABCDCBA"
print(check_pal(str1, 0, len(str1) - 1))

#------------------------------------------
# Method 3: Recursion:- Functional Recursion - Using 1 Pointer variable

def check_pal(n, str, low):
    if low>=n//2:                  #BASE CASE
        return True
    else:
        if str[low] != str[n-low-1]:
            return False
        
        return check_pal(n, str, low + 1)


str1 = "ABCDCBA"
print(check_pal(len(str1), str1, 0))

#===============================================
"""
Ques:- 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def isPalindrome(s):
    
    
    left = 0
    right = len(s)-1

    while left<right:
        if not s[left].isalnum():
            left +=1

        elif not s[right].isalnum(): 
            right -= 1

        elif s[left].lower() != s[right].lower():
            return False
            
        else:
            left +=1
            right -=1
    
    return True

    

s = "race a car"
print(isPalindrome(s))