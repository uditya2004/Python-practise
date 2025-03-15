"""
Make all the methods in O(1) TC
"""

# Brute Force
# TC: O(N) for getmin() operation
class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):     # TC: O(1)
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
 
    def pop(self):            #TC: O(1)
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):             #O(1)
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):           # TC: O(N)
        """
        :rtype: int
        """
        return min(self.stack)
        

#===========================

# Better solution
# Time complexity: O(1) for all operations.
# Space complexity: O(n)
"""
APPROACH
- make a list "stack"
- make a list "min" to track the minimum element in the stack. (last element of this stack or recently added element in this stack will represent the current minimum of the Main stack)

- while push or pop make sure to update the list "min" accordingly.

- PUSH
    - push in "stack"
    - check the pushed value if it's smaller that last element of "min" list:-
        - If smaller, then push it in "min"

- POP
    - Pop from "stack", 
    - check if the popped element = min[-1] (means if the popped elemnent is the current min)
        - If found equal, then pop from "min" as well 
"""
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []   # SC: O(N)      , Used to keep track of minimum at any point
        

    def push(self, val):     # TC: O(1)
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If the minimum is empty , simply add the new val. If not empty, we want the newest added element to always be minimum
        if not self.min or  self.min[-1] >= val:   # This ensures that the min stack always contains the sequence of minimum elements as new values are added.
            self.min.append(val)
        
 
    def pop(self):            #TC: O(1)
        """
        :rtype: None
        """
    
        if not self.stack:   # If stack is empty do nothing
            return 
        else:
            m = self.stack.pop()
            # If the popped value matches the top of the min stack (self.min[-1]), it is also removed from min. This ensures that the min stack remains in sync with the main stack.
            if self.min[-1] == m:
                self.min.pop()
        

    def top(self):             #O(1)
        """
        :rtype: int
        """
        if not self.stack:     # Empty
            return
        else:
            return self.stack[-1]
        

    def getMin(self):           # TC: O(1)
        """
        :rtype: int
        """
        return self.min[-1]
    
#===========================

# Best solution:- use a "difference encoding" strategy for storing values in the stack
"""
We store:-
    - in stack -> pushedElement - currentMin
    - in "min" -> pushedElement
"""
# Time complexity: O(1) for all operations.
# Space complexity: O(1)

class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []


    def push(self, x: int) -> None:

        if not self.stack:           # if the stack is empty:- 
            self.stack.append(0)     # 1. append "0" to the "stack"
            self.min = x             # 2. set the min = "variable to be pushed"

        else:                                  # If the stack not empty:- 
            self.stack.append(x - self.min)    # 1. We store difference of element to be pushed and minimum to the "stack"
            if x < self.min:                   # 2. Update the minimum variable
                self.min = x


    def pop(self) -> None:
        if not self.stack:      # If poped from empty stack do nothing
            return
        
        poppedElement = self.stack.pop()
        
        # -ve elements will be stored in the stack only in case when element is smaller than min.
        # Case - 1:- Popped element is +ve:- no change to self.min.
        # Case - 2:- Popped element is -ve:- update self.min
        if poppedElement < 0:    
            self.min = self.min - poppedElement   # this is the case when the poped element is the current min element, so to go to prev min we do  "self.min - pop" where pop is -ve num -> self.min+pop


    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:                   # if the top is +ve, then to find the top element we do "top + self.min"
            return top + self.min
        else:
            return self.min            # if the top is -ve , then the "min" is the "top"


    def getMin(self) -> int:
        return self.min               # The self.min variable always holds the current minimum.