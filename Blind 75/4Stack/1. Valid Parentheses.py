"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""
# Best Solution
# TC: O(N)
# SC: O(N)
def isValid(s: str) -> bool:
    stack = []
    res = False

    if len(s) == 1:
        return False
    
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for i in range(0,len(s)):

        if s[i] in ["(", "[", "{"]:     # encountered open bracket. push it into the stack
            stack.append(s[i])
        
        elif s[i] in [")", "]", "}"]:   # encountered closed bracket, compare
            
            if not stack:               # (Stack is empty) :- We encountered a closing bracket before any opening bracket 
                return False            # returning false , as it's not following the correct order
             
            if bracket_map[s[i]] == stack[-1]:      # Check if the corresponding opening bracket , matches the last open bracket in stack.
                stack.pop() 
            else:                                   # Mismatch
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



