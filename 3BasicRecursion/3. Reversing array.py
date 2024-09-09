# Method 1:- Recursion:- parameterize way            
# TC: O(N) 
# SC: O(N)  -> O(N) {result varaible} + O(N) {Function call stack}
# def reverse(n, arr, result):
#     if n<0:                     #BASE CASE
#         print(result)
#         return
    
#     else:
#         result.append(arr[n-1])
#         reverse(n-1, arr, result)


# array = [10,20,30,40]
# result = []

# reverse(len(array), array, result)

#=========================================

# Method 2:- Recursion:- Functional way - Using 2 Pointer through 2 variable
# TC : O(N/2) = O(N)
# SC: O(N/2) = O(N)  {Function call stack}

# def reverse(arr, left, n-left-1):
#     if left>=n-left-1:            #BASE CASE
#         return arr
    
#     else:
#         arr[left], arr[n-left-1] = arr[n-left-1], arr[left]
#         return reverse(arr, left+1, n-left-1-1)


# array = [10,20,30,40]

# print(reverse(array, 0, len(array)-1))

#=========================================

# Method 3:- Recursion:- Functional way - Using 2 Pointer through 1 variable  (take right pointer = n-left-1)
# TC : O(N/2) = O(N)
# SC: O(N/2) = O(N)  {Function call stack}

def reverse(n, arr, left):
    if left >= n//2 :            #BASE CASE
        return arr
    
    else:
        arr[left], arr[n-left-1] = arr[n-left-1], arr[left]
        return reverse(n, arr, left+1)


array = [10,20,30,40]

print(reverse(len(array), array, 0))