# NOTE: Heapq library implements min heap
"""
- Time complexities of function:
    - heapq.heapify => TC: O(N)
    - heapq.heappop => TC: O(logN)
    - heapq.heappush => TC: O(logK), where K is heap size
"""
# Kth Largest => So we use Min heap of size k
import heapq
class KthLargest:

    # TC:- O(n) + O((n - k) log n)  = O(n log n)
    def __init__(self, k: int, nums: list[int]):
        self.minHeap = nums    # right now self.minheap is just a array, so we have to convert it into heap
        heapq.heapify(self.minHeap) # converting the array to heap   TC: O(N)

        self.k = k    # size of heap

        #After initializing a heap => to maintain the size k, we pop if the initial len(minHeap) > k
        """
        - Time complexity:
            - Number of pops = n - k
            - Each heappop takes O(log n) initially
        - So TC: (n - k) * log n
        """
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # poping the minimum value

    # TC: O(logK)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # if originally the len(minHeap) < k, the while loop in __init__ will not run, so after adding a ONE new value, we check if size > k by ONE element, if so we POP one value
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # poping the minimum value
        
        """
        - The heap does NOT store all numbers. It stores only the k largest numbers seen so far.
        - Because it's a min-heap, the smallest among those k largest numbers is at index 0
        """
        return self.minHeap[0]   
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))