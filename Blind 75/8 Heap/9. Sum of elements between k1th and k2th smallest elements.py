# Question Link:- https://www.geeksforgeeks.org/problems/sum-of-elements-between-k1th-and-k2th-smallest-elements3133/1

"""
APPROACH:-

Lets Assume K2 > K1
- Sort using maxHeap of size => max(K1, K2). So we get K2 smallest number where the number aat the top will be K2
- Pop K2 
- run a loop of => abs(K2-K1) - 1 times:
    - in each iteration pop element and Add it to SUM variable

- Return SUM variable
"""

#TC: O(NLogK2 + LogK2 + MLogK2) => O(NlogK2) , where N >> M
# SC: O(K2)
import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        maxHeap = []    # SC: O(K2)

        # TC: O(NLogK2)
        for i in A:    # TC: O(N)
            heapq.heappush(maxHeap, -i)  # TC: O(LogK2)

            if len(maxHeap) > max(K1, K2):
                heapq.heappop(maxHeap)
        
        #Popping K2th element
        heapq.heappop(maxHeap)  # TC: O(Logk2)

        # pop abs(K2-K1) - 1 times and add it to SUM
        sum = 0
        for i in range(0, abs(K2 - K1) - 1):   # TC: O(M), m is number of elements between K1 and K2
            element = -heapq.heappop(maxHeap)  # TC: O(LogK2)
            sum += element
        
        return sum


obj = Solution()
A = [20, 8, 22, 4, 12, 10, 14]     # [4, 8, 10, 12, 14, 20, 22]
K1 = 3                             #         |           |
K2 = 6
N  = 7
print(obj.sumBetweenTwoKth(A, N, K1, K2))