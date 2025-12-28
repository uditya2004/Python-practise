import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = []

        for val in nums:
            heapq.heappush(minHeap, val)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

obj = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(obj.findKthLargest(nums, k))