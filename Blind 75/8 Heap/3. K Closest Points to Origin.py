import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []

        for x,y in points:
            distance = (x**2) + (y**2)
            heapq.heappush(maxHeap, (-distance, [x,y]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [point for distance, point in maxHeap]




obj = Solution()
points = [[1,3],[-2,2]]
k = 1
print(obj.kClosest(points, k))