#Ques 1:- Sum of N natural number

#Method 1:-  Recursion:- PARAMETERIZED WAY 
# TC:- O(N) (For one number it takes O(1) and it does for all N numbers . SO O(N)
# SC:- O(N) (Stack Space

def summation(n, result):
    if n == 0:
        print(result)
        return
    else:
        summation(n-1, result + n)


n= int(input("Enter a Times:-"))
summation(n, 0)


#-------------------------------------------
#Method 2:- Recursion:- FUNCTIONAL WAY -> Used when we want function to return value and not just print it
def summation_using_recursion(n):
    if n == 0:
        return 0
    else:
        return n + summation_using_recursion(n-1)


n= int(input("Enter value of N:- "))  
print(summation_using_recursion(n))




#=======================================================
#Question:- Factorial of N

#Method 1:- Recursion:- Parameterized way
# TC:- O(N) (For one number it takes O(1) and it does for all N numbers . SO O(N)
# SC:- O(N) (Stack Space)      

def factorial(n, fact):
    if n ==0:
        print(fact)
        return
    
    else:
        factorial(n-1, fact * n)


n = int(input("Enter a number:- "))  #4
factorial(n,1)

#---------------------------------------------
#Method 2:- Recursion:- Functional Way

def factorial(n):
    if n== 0:
        return 1
    
    else:
        return n * factorial(n-1)

n = int(input("Enter a number:- "))  #4
print(factorial(n))