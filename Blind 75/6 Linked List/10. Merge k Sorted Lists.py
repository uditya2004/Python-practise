from typing import Optional
import heapq
from helper import *

# "N" is total nodes and "k" is number of lists
# TC: O(KLogK + N*LogK) = O(NLogK)
# SC: O(K), as the heap size always remains K -> we are just removing one element and adding one element in each iteration
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # empty list
            return None
        
        """
        - Initializing Heap with heads:- 
            - push the head of each linked list to minHeap
        """
        minHeap = []
        for index, head in enumerate(lists):   # TC: O(KLogK)

            if head:   # push head only if head is not None
                heapq.heappush(minHeap, (head.val, index, head))


        """
        - pop the minimum (heappop)
            - add the next node of the popped node
            - Add the popped node in front of dummy node
        - keep running the loop until the min heap is empty
        """
        dummy = ListNode()
        curr = dummy
        while minHeap:  # TC: O(N*LogK)
            headVal, index, node = heapq.heappop(minHeap)

            # adding next of popped node to heap
            nextNode = node.next
            if nextNode:    # push next node only when nextNode is not None
                heapq.heappush(minHeap, (nextNode.val, index, nextNode))

            # adding popped element in front of dummy node
            curr.next = node

            # move current pointer forward
            curr = curr.next
        

        return dummy.next




obj = Solution()
lists = [
    build_list([1,4,5]),
    build_list([1,3,4]),
    build_list([2,6])
]

print_list(obj.mergeKLists(lists))



