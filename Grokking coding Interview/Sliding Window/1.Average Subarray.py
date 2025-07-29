# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

"""
-> Set i = 0 and move j from the start (i.e., j = 0)

-> Till window size < k:
    Just keep adding elements to the window sum

-> Once window size == k:
    - Add upcoming element to the sum
    - Subtract the outgoing element from the sum (i.e., arr[i])
    - Slide the window by moving i += 1
"""

# TC: O(N)
# SC: O(1)
def findAvg(lst, k)-> list:
    result = []
    sum = 0
    i = 0

    for j in range(0, len(lst)):
        sum += lst[j]

        if j >= k-1:
            result.append(sum/5)
            sum -= lst[i]
            i +=1
    return result


l = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(findAvg(l,k))