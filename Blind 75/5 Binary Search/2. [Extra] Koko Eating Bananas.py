"""
1. Value of k can be in range 1 to max(piles: list[int])
2. We apply binary search on values of K:
    - For each K we see if total hours needed to eat all the bananas execeeds "h" or not
        - If it exceeds, then we need more banana eating speed , so move the left pointer next to mid
        - If it do not execeed, this can be possible answer , so take min(result, k)
"""
# TC: O(n x logm)    (we are processing n piles in each turn.   As we are applying binary search for the values of k, so logm, where m are the possible values of k)
# SC: O(1)

import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    left  = 1
    right = max(piles)

    result = max(piles)

    while left <= right:
        totalTime = 0   # for each value of k, we calculate the total time
        k = (left + right) // 2

        # for a value of K, calculating the total time to finish all the piles
        for element in piles: 
            totalTime += math.ceil(element / k)
        
        # if the total time taken is less or equal to threshold (h), it is a possible answer , but we will further try to decrease speed (k) in search of minimum
        if totalTime <= h:
            result = min( result, k)
            right = k - 1
        
        # if the total time taken is more than threshold (h), the speed is slow, we have to increase speed(k)
        else:
            left = k + 1
    
    return result

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))