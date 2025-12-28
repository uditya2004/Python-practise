from collections import defaultdict
import heapq


# TC: O(N) + O(MLog K) + O(K) = O(N + MlogK)
# SC: O(M + K) = O(M)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # hashmap to store frequency associated with element
        hashmap = defaultdict(int)   # SC: O(M), m unique element

        # TC: O(N)
        for i in nums:
            hashmap[i] +=1   
        
        """
        - Use heap to find the top k frequent by pushing pair (frequency, element).
        - keep fix size k
        - Use min Heap => so that min freq element comes to top and we can remove then
        """

        # TC: O(MLog K)
        minHeap = []      # SC: O(K)
        for element, freq in hashmap.items():           #TC: O(M) ,  where M is no. of unique elements in nums
            heapq.heappush(minHeap, (freq, element))    # TC: O(log K), where k is heap capacity

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [element for freq, element in minHeap]   # TC: O(K)

obj = Solution()
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(obj.topKFrequent(nums, k))