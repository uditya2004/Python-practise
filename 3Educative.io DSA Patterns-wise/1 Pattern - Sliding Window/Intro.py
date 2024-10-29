"""

Ques:- Given an array, find the average of all contiguous subarrays of size 'K' in it.

"""

# Approach 1 - Brute Force
def average(K, lst):
    result = []
    for i in range(0, len(lst)):
        
        summation = 0
        max_ind = i+K

        if (max_ind-1) <= (len(lst) - 1):

            for j in range(i, max_ind):
                summation += lst[j]

            result.append(summation/K)
    
    return result



result = average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K:", result)

#===============================
# Approach 2 - Sliding window