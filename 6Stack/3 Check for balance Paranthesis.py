def isMatching(a,b):
    #If pair matches , return True , else False
    if (a== "[" and b== "]") or (a== "{" and b== "}") or (a== "(" and b== ")"):
        return True
    else:
        return False
    
def isBalanced(str):
    stack = []

    for i in str:
        if i in ( "[","{","(" ):
            stack.append(i)

        else:
            """ In Python:
                    - An empty list ([]) is considered False.
                    - A list containing any elements is considered True.
                """ 
            if not stack:     #For cases that starts with closed brackets " )([])" . In this case closed bracket will be compared with empty stack which will give "index out of range" error.
                return False
                  
            if isMatching(stack[-1], i,) == True:   #checking if the pair is correct or not
                stack.pop()
            else:                           #If pair doesn't match, it is not balanced
                return False

    #After traversing through the complete string and doing push,pop operations , if the stack has some elements left (eg: [[] ) then it's not balanced
    if stack:
        return False
    else:
        return True
                

str = "[]"
print(isBalanced(str))


