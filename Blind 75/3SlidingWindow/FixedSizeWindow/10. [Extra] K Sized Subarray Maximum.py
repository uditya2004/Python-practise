"""
Given an array arr[] of positive integers and an integer k. Find the maximum value for each contiguous subarray of size k.

https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
"""
from collections import deque

# Fixed Size Sliding Window
# TC:- O(N)
# SC:- O(K), deque holds at most K elements
class Solution:
    def maxOfSubarrays(self, arr, k)->list[int]:
        q = deque()    # contains max element candidates in decreasing order, so if we q.popleft, then q[0] gives us next max element

        result = []

        n = len(arr)
        i = 0
        j = 0
        while j < n:
            # 1. calculation
            # In queue, as long as arr[-1] < ar[j] keep poping, as those element will no longer be useful
            # This will arrange queue in decreasing order:- largest on the left end and smallest on the right end
            while q and q[-1] < arr[j]:
                q.pop()
            q.append(arr[j])

			# 2. shrink
            if j-i+1 > k:
                # arr[i] , if present, will always be found at the queue starting
                if arr[i] == q[0]:
                    q.popleft()
                i += 1

			# 3. Record
            if j-i+1 == k:
                result.append(q[0])

			# 4. Move
            j +=1
        return result



obj = Solution()
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(obj.maxOfSubarrays(arr, k))