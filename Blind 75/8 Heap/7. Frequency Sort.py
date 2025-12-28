import heapq
from collections import defaultdict

# Question:- sort by frequency descending, and if frequencies tie, larger element first
class Solution:
    def freqSort(self, nums: list[int]) -> list[int]:
        
        # {element: freq}
        hash = defaultdict(int)
        for i in nums:
            hash[i] +=1

        # maxHeap with pair (freq, element) => maxFreq element at top
        maxHeap = []
        for element, freq in hash.items():
            heapq.heappush(maxHeap, (-freq, -element))
        
        # building result list 
        result = []
        for i in range(len(maxHeap)):
            freq, element = heapq.heappop(maxHeap)
            
            while freq !=0:
                result.append(-element)   # -element to make -ve element +ve
                freq +=1    # we add we freq is -ve, we add to come to 0
        
        return result


obj = Solution()
nums = [1,1,1,3,2,2,4]
print(obj.freqSort(nums))   # Expected output:- [1,1,1,2,2,4,3]