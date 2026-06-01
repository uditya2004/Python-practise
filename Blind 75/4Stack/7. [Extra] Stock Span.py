# Problem Link:- https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

"""
- From the current element, we keep moving to the left as long as we are getting smaller or equal elements to the current element.
    - We stop when we get a greater element than the current element

- Hence we are looking to Nearest greater to the right.
"""

# Monotonic Stack:- Nearest Greater to the Left Pattern

#TC: O(N)
#SC: O(N)
class Solution:
    def calculateSpan(self, arr):
        result = []
        stack = []   # store indexes
        n = len(arr)
        
        # Traverse from left to right
        for i in range(0, n):

            if not stack: # empty
                result.append(1)
            
            else: # not empty

                # pop till we get a greater element or the stack get's empty
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                
                # emptied the stack while popping
                # means no element to the left is greater than current element.
                # so result for this will be:- number of element in left + 1  = i + 1
                if not stack: 
                    result.append(i+1)
                
                else: # element there in the stack, so the stack top contains the element's index greater than current
                    result.append(i-stack[-1])
                    
            stack.append(i)
        
        return result

obj = Solution()
arr = [10, 4, 5, 90, 120, 80]
print(obj.calculateSpan(arr))