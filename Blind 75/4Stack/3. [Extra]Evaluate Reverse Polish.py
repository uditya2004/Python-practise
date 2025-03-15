"""
APPROACH
- Create a stack
- Traverse through the string
    - If found an operand put it in the stack.
    - If found an operator, pop last 2 entered operand, perform operation and push the result back into the stack.

- Once the traversal is done, last element in the stack is the final result of the complete expression.
"""
# TC: O(N)
# SC: O(N)
def evalRPN(tokens: list) -> int:
    stack = []
    operators = "+-*/"
    #Traverse through the string
    for i in tokens:

        #If found an operand , push it in the stack
        if i not in operators:
            stack.append(i)
        
        #If found an operator, pop previous 2 elements and push the result of operation
        else:
            SecOperand = int(stack.pop())
            FirstOperand = int(stack.pop())
            result = 0
            if i == "+":
                result = FirstOperand + SecOperand
            elif i == "-":
                result = FirstOperand - SecOperand
            elif i == "*":
                result = FirstOperand * SecOperand
            elif i == "/":
                result = int(FirstOperand / SecOperand)  # Used "int" as we have to round towards zero
            
            stack.append(result)
    
    return int(stack.pop())


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))

