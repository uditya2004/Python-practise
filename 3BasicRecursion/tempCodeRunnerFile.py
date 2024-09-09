# Ques:- Given an integer N. Print the Fibonacci series up to the Nth term.
def series(n, a, b, c):
    if n == 0:
        return
    else:
        print(c, end = " ")
        a = b
        b = c 
        c = a+b
        series(n-1, a, b, c)

n = int(input("Enter number: "))
a = 0
b = 1
c = a+b
print(a, end=" ")
print(b, end=" ")
series(n-2, a, b, c)