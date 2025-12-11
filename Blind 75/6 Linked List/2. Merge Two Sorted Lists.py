"""
1. Create a dummy Node = -1 and a pointer "curr" pointing to this node -> in the end we return "dummy.next", so this -1 node is of no use for us.
2. We place 2 pointers at l1 and l2.
3. Out of the 2 pointer get the smaller data node and add it to the dummy linked list, then move these 2 pointers
"""

from typing import Optional
from helper import build_list, ListNode, print_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # list1 and list2 are the heads of the two list
        
        dummy = ListNode()
        curr = dummy

        p1 = list1
        p2 = list2

        while p1 != None and p2 != None:
            
            # smaller will get appended + smaller pointer moves forward
            if p1.val <= p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next

            curr = curr.next
        
        while p1 != None:
            curr.next = ListNode(p1.val)
            curr = curr.next
            p1 = p1.next

        while p2 != None:
            curr.next = ListNode(p2.val)
            curr = curr.next
            p2 = p2.next

        return dummy.next


obj = Solution()

list1 = build_list([1,2,4])
list2 = build_list([1,3,4])

result = obj.mergeTwoLists(list1, list2)

print("Merged List:")
print_list(result)