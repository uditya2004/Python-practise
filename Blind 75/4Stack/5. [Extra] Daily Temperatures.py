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
- Make a result list:- Initialize every element as zero (default value for all)
- Make a empty stack list for keeping track of previous smaller elements.

- Traverse through the temperature array:-
    - If the stack if empty, push the current element to the stack, move to the next element.
    
    - Compare the current element with the top of the stack,

        - if the StackTopElement < current element
            - pop the Top
            - Update Top's corresponding value in result list to (currentNumIndex - StackTopElementIndex)
            - continue the same process with the new Top, until the stack is empty
        
        - if the StackTopElement > current element
            - push current element in the stack
"""
# Best Solution:- Monotonic Decreasing Stack (Best Solution)

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # Every element initialize it with 0
    result = [0] * len(temperatures)

    stack = []       # each element is a tuple : (temp, index)

    for currIndx, currNum in enumerate(temperatures):
        
        # If the stack is not empty and current element > stack top element, update the value in result list corresponding to the stack Top element
        while stack and currNum > stack[-1][0]: 
            
            stackTop, stackTopIndx= stack.pop()    # popped element is a tuple (temp, index) , where stackTop = temp and stackTopIndx = indx

            result[stackTopIndx] = currIndx - stackTopIndx   # Updating the value in result list corresponding to stackTop element index
        
        # if the stack is empty or the num < stackTop Element, then push current element to the stack
        else:
            stack.append((currNum, currIndx))   
    
    return result

temperatures = [30,60,90]
print(dailyTemperatures(temperatures))