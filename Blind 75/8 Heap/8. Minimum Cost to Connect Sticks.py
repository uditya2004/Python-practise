# Question:- https://neetcode.io/problems/minimum-cost-to-connect-sticks/question

# Goal: Connect all sticks into one with minimum total cost

# Strategy:- By always connecting the two smallest sticks first, you minimize the cost

"""
- Push all the number in sticks array to min Heap
- Pick two min number:
    - result = first + second
    - cost += result
    - Push result to Heap again
"""
import heapq
class Solution:
    def minCostRope(self, sticks: list[int]) -> int:
        minHeap = []
        for i in sticks:
            heapq.heappush(minHeap, i)
        
        cost = 0
        while len(minHeap) >= 2:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            result = first + second
            cost += result

            heapq.heappush(minHeap, result)

        return cost
    
obj = Solution()
sticks = [1,2,3,4,5]
print(obj.minCostRope(sticks))