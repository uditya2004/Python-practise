def fib(n):
    if n<=1:
        return n
    else:
        last = fib(n-1)
        sec_last = fib(n-2)
        return  last + sec_last 


n = int(input("Enter the number: "))
print(fib(n))

# 0 1 1 2 3 5