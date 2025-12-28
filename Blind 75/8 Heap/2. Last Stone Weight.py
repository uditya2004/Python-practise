"""
- We use Max Heap as:
    - I need to repeatedly extract the maximum element
    - After processing, I might need to insert a new element back
    - Heaps give me O(log n) for insert and extract operations

Note:- Python's heapq is a min heap. So I'll negate all values when pushing, and negate again when popping to get the actual value.
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxHeap = []

        # insert all the elements to heap
        for i in stones:
            heapq.heappush(maxHeap, -i)

        # repeatedly pop 2 max elements and smash them
        while len(maxHeap) >= 2:   # there should be atleast 2 elements before we start popup 2 element
            
            # first > second , as at the top is "first" and below it was "second" => maxHeap, max element at the top
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            if first != second:
                heapq.heappush(maxHeap, -(first - second))
        
        # if maxHeap contain element , then return maxHeap[0], else return 0
        if maxHeap:
            return -maxHeap[0]   
        else:
            return 0
            



obj = Solution()
stones = [2,7,4,1,8,1]
print(obj.lastStoneWeight(stones))