"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

#==================================================
"""
ALGORITHM:
- traverse through the string
    - if found the open bracket , put it in the stack
    - if found the closing bracket, check the top of the stack for the corresponding opening bracket of it:-
        - if top has corresponding opening bracket
            - pop it from the top of the stack
        - if top doesn't have corresponding closing bracket
            - return false.

- After full traversal, check the stack:
    - if empty:
        - return true
    - if not empty, means there is a opening bracket whose corresponding closing bracket is not present in the string
        - return false
"""
# Best Solution
# TC: O(N)
# SC: O(N)
def isValid(s: str) -> bool:
    stack = []

    if len(s) == 1:
        return False
    
    bracket_map = {
        ")": "(", 
        "]": "[", 
        "}": "{"
    }

    openingBrackets = "({["
    closingBrackets = ")}]"

    for i in range(0,len(s)):

        if s[i] in openingBrackets:     # encountered open bracket. push it into the stack
            stack.append(s[i])
        
        elif s[i] in closingBrackets:   # encountered closed bracket, compare
            
            if not stack:               # (Stack is empty) :- We encountered a closing bracket before any opening bracket 
                return False            # returning false , as it's not following the correct order
             
            if bracket_map[s[i]] == stack[-1]:      # Check if the corresponding opening bracket , matches the last open bracket in stack.
                stack.pop() 
            elif stack[-1] != bracket_map[i]:         #MisMatch
                return False
    
    """ 
    In Python:
        - An empty list ([]) is considered False.
        - A list containing any elements is considered True.
    """ 
    
    # Check if the stack is empty of not after traversing the entire string
    if not stack:     # Stack do not have any element left
        return True 
    else:             
        return False  # Stack has a element left, it means we didn't got the corresponding closing bracket for that element. So not balanced

        

s = "()[]{}"
print(isValid(s))


# ===================
# Shorter to write
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {")": "(", "}": "{", "]": "["}

        for i in s:
            
            # if it is a closing bracket , check it with the top of the stack if it's the corresponding opening bracket
            if i in maps:
                if not stack or maps[i] != stack.pop():   # if the stack is empty when we got the closing bracket OR top element is not the corresponding opening bracket, then return false
                    return False
            else:                                    # if not in maps , means it's opening bracket, so push it to stack
                stack.append(i)
           
        return len(stack) == 0


obj = Solution()
s = "()"
print(obj.isValid(s))
