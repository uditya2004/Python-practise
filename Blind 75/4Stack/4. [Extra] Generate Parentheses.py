"""
As Choices and Decisions are required for filling each box with open or close parenthesis , So it's a recursion question.
"""
#===================================
"""
CONCEPT
Base Case:- When openBrackets == Closed Brackets == n, we found a valid combination

Constraints:-
At each step, we either:
1. add one more openBracket if:
    - no. of openBrackets < n

2. add one more closeBracket if:-
    - no. of closeBrackets < openBracket
"""
#====================================
"""
Decision Tree for recursion

n = 3
                   ""
                   /  
                 "("  
               /      \
           "(("       "()"
          /    \      /
      "((("   "(()"  "()("
      /   \      \       \
  "((())" "((()))" "()()("
     |         |       |  
  "((()))"  "(()())" "()()()"
 
"""

# Recursive Backtracking Approach

def generateParenthesis(n: int) -> list[str]:
    stack = []                     # Used for making one valid comination like ["(", ")", "(", ")", "(", ")"]
    result = []                    # contains  all possible combinations

    def backtracking(openN, closeN):

         # If we used all parentheses, add valid string to results
        if openN == closeN == n:
            result.append("".join(stack))    # join all the elements in "stack" to make a single string, then append this string to "result"
            return                           # we reached the end of the tree, so Stop exploring this branch    
        
        
        # We start with adding "(", we can't add ")" as first element in stack, as it will give invalid combination
        # If we can still add '(', add it and recurse
        if openN < n:                        # Makes:- Child Node 1
            stack.append("(")
            
            backtracking(openN + 1, closeN)  # calling function again to make further child node if possbible, considering this "Child Node 1" as parent now.
            
            stack.pop()                      # When we reach the end node, we append it to the result then we backtrack i.e go to the previous state then search for other paths. To achieve the previous state we pop the currently added element. It's like depth first search.


        # If we can add ')', add it and recurse
        if closeN < openN:                   # Makes:- Child Node 2
            stack.append(")")
            
            backtracking(openN, closeN + 1)  # calling function again to make further child node if possbible, considering this "Child Node 2" as parent now.
            
            stack.pop()

    backtracking(0,0)                        # as initially we are setting openN = 0, closeN = 0
    return result

n = 3
print(generateParenthesis(n))

