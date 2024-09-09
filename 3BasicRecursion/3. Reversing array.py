# parameterize way            
# TC: O(N) 
# SC: O(N)  -> O(N) {result varaible} + O(N) {Function call stack}
def reverse(n, arr, result):
    if n<0:
        print(result)
        return
    
    else:
        result.append(arr[n-1])
        reverse(n-1, arr, result)


array = [10,20,30,40]
result = []

reverse(len(array), array, result)



# Functional way
# TC : O(N/2) = O(N)
# SC: O(N/2) = O(N)  {Function call stack}
def reverse(arr, p1, p2):
    if p1>=p2:
        return arr
    
    else:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        return reverse(arr, p1+1, p2-1)


array = [10,20,30,40]

print(reverse(array, 0, len(array)-1))