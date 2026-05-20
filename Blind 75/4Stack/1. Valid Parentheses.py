"""
- Traverse through the elements of s:
    - If it's a opening bracket:
        - Push it in stack.
    - If it's a closing bracket:
        - If the stack is not empty:
            - Check if stack_top == opening bracket corresponding to current closing bracket. If it is , pop the stack top and move to next element else false
        - If stack empty
            - return False, as it's wrong order

- Finally after completing the traversal:-
    - If stack is empty -> we got correct orders -> return True
    - If stack not empty -> we got wrong orders -> returns False
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        dict1 = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        stack = []
        for i in s:

            if i not in dict1: # opening bracket -> push in the stack
                stack.append(i)

            else:  # closing bracket
                if stack and stack[-1] == dict1[i]:   
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                


obj = Solution()
s = "(("
print(obj.isValid(s))