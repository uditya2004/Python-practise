# Ques:- Given an integer N. Print the Fibonacci series up to the Nth term.
# def series(n, a, b, c):
#     if n == 0:
#         return
#     else:
#         print(c, end = " ")
#         a = b
#         b = c 
#         c = a+b
#         series(n-1, a, b, c)

# n = int(input("Enter number: "))
# a = 0
# b = 1
# c = a+b
# print(a, end=" ")
# print(b, end=" ")
# series(n-2, a, b, c)

#0 1 1 2 3 5 8 13

"""
Multiple Recursion:- 
- In case of Multiple recursion, as program execute line by line , so one recursion gets called and come back , then the second recursion is called.

"""
#-------------------------------
# Ques:- Given an integer N. Print the Nth term of fibonacci series.

# Method :- Using Multiple Recursion way  -> Multiple function calls to itself, inside a function

def series(n):
    if n<=1:
        return n
    else:
        last = series(n-1)
        sec_last = series(n-2)

        return last + sec_last

n = int(input("Enter number: "))
print(series(n))