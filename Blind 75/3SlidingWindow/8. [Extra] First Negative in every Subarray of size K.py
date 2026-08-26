from collections import deque

"""
Question:
https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
"""

# FIXED SIZE SLIDING WINDOW
# TC: O(n) -> each index enters/leaves the window and the deque at most once
# SC: O(k) (auxiliary)
class Solution:
    def firstNegInt(self, arr: list[int], k: int)->list[int]:
        n = len(arr)

        result = []
        currNegative = deque()   # SC: O(K)

        i = 0
        j = i

        # TC: O(N)
        while j < n:
            # 1. CALCULATION
            if arr[j] < 0: # negative
                currNegative.append(arr[j])   # TC: O(1)

            # 2. If window overgrew, SHRINK from left => outgrows only by 1 unit
            if j-i+1 > k: 
                if arr[i] < 0:   # If arr[i] is negative, then that element will be the leftmost in deque
                    currNegative.popleft()   # TC: O(1), this is why deque is used instead of list. In list removing first element is O(N)
                i += 1

            # 3. Record the valid result
            if j-i+1 == k:
                if currNegative:  
                    result.append(currNegative[0])
                else:
                    # As per question, if no negative element in window then report 0   
                    result.append(0)

            # 4. Move
            j += 1

        return result

obj = Solution()
arr= [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(obj.firstNegInt(arr, k))