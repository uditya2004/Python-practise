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
                stack.append(i)
            
            else: # not empty

                # pop till we get a greater element
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                
                # we got a greater element
                if not stack: # emptied the stack while popping, means not element greater
                    result.append(i+1)
                
                else: # element there in the stack, so the stack top contains the element's index greater than current
                    result.append(i-stack[-1])
                    
                stack.append(i)
        
        return result

obj = Solution()
arr = [10, 4, 5, 90, 120, 80]
print(obj.calculateSpan(arr))