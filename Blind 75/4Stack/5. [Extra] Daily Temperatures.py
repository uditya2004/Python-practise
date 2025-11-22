"""
- Traverse through the list using indexes
- At every element, initialize the value associated with it = 0 
- check if current element is larger than the previous element:-
    - If it's larger:-

        - if the value associated with previous element is 0:-
            - update it to = (currentIndex - elementIndex)
            - move to next previous element and check smaller than current and associated value 0, if yes then update it
        
        - If associate value is not 0:-
            - move to next previous element and check smaller than current and associated value 0

    - If it's smaller:-
        - move to the next element forward
"""
# Worst solution
# TC: O(N^2)
# SC: O(N)
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # Every element initialize it with 0
    result = [0] * len(temperatures)

    # Traverse through each element by indexex
    for i in range(0, len(temperatures)):

        # If it's the first element then move to the next element
        if i == 0:
            continue

        for j in range(i-1, -1, -1):

            #Check if current element is larger than previous element
            if temperatures[i] > temperatures[j]:
                
                # Check if value associated with the previous element = 0
                if result[j] == 0:

                    # If it is then update (current - previous index)
                    result[j] = i-j
                
            elif temperatures[i] < temperatures[j]:
                break
    
    return result


temperatures = [30,60,90]
print(dailyTemperatures(temperatures))


#===========================================================
"""
APPROACH:- Nearest Greater to Right Pattern
- Traverse from right to left. For each element:- 
    - we pushed all the elements to it's right to a stack
    - pop elements from the stack to compare if it's greater than current element
"""

# Monotonic Stack:- Nearest Greater to the Right Pattern
# TC:- O(N)
# SC:- O(N)
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []   # stores indices
        result = []
        n = len(temperatures)

        for i in range(n-1, -1, -1):    # traverse from right to left

            # if the stack is empty means, no element in the right side, so push 0 to result[] and push current element index to stack (pushing index not the element as we wanted distances in the final result[])
            if not stack:
                result.append(0)
                stack.append(i)
            
            else: # stack not empty
                """
                - keep popping from stack until:- 
                    - the stack has elements
                    - until we get a bigger temperature

                - Note:- temperatures[stack[-1]]  is stack_top
                """
                while stack and temperatures[stack[-1]] <= temperatures[i]:   
                    stack.pop()
                
                # for stack_top > temperature[i]
                if not stack:      # empty, while popping if the stack becomes empty, means no temp on right is bigger, so append 0 to result[] and push current element's index to stack
                    result.append(0)
                    stack.append(i)

                else:   # not empty, if stack has elements then the stack_top is the index of element whose value bigger than current element. So push distance between that element and current elemen to the result and push current element's index to stack
                    result.append(stack[-1] - i)
                    stack.append(i)
        
        return list(reversed(result))   # result[] we made is reverese from what we needed , so we reverse it get the desired output




obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(temperatures))