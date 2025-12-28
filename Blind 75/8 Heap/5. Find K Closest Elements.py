import heapq

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        
        # Store in Heap a pair (key, arr[i]) => here key is => abs(arr[i] - x)
        # We use max heap of size k => as in max heap at top contains higher ab(arr[i] - x) which will be removed, elements left in the heap will have minimum difference , thus closest to x
        maxHeap = []

        for i in arr:
            heapq.heappush(maxHeap, (-abs(i - x), -i))   # as heaq implements minHeap only, we push (-diffence, -element) to simluate maxHeap. "-element" for tiebreak condition where difference is same, then we need to keep larger value on top so we can pop it.

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return sorted([-num for key, num in maxHeap])


obj = Solution()
arr = [1,2,3,4,5] 
k = 4
x = 3
print(obj.findClosestElements(arr, k, x))
