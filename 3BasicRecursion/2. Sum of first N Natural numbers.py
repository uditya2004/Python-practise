#Method 1:-
def summation(n, result):
    if n == 0:
        print(result)
        return
    else:
        result +=n
        summation(n-1, result)


n= int(input("Enter a Times:-"))
summation(n, 0)


#=============================================
#Method 2:-
def summation_using_recursion(n):
    if n == 0:
        return 0
    else:
        return n + summation_using_recursion(n-1)


n= int(input("Enter value of N:- "))  
print(summation_using_recursion(n))