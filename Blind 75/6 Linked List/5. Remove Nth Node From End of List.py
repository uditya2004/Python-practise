from typing import Optional
from helper import build_list, ListNode, print_list

class Solution:

    # Method 1:- Better solution (Require 2 pass)
    # def removeNthFromEnd(self, head, n: int):

    #     if head == None or head.next == None: 
    #         return None

    #     #findinng the length of the linked list.  TC: O(N)
    #     length = 0
    #     curr = head
    #     while curr != None:
    #         length +=1
    #         curr = curr.next
        
    #     # deleting the node.   TC: O(M)
    #     target = (length - n) + 1   #4

    #     if target == 1:   # case of delete from beginning
    #         return head.next

    #     curr1 = head
    #     for i in range(0, target-2):  
    #         curr1 = curr1.next
        
    #     curr1.next = curr1.next.next

    #     return head
        
    #Method 2:- Best Solution (Single Pass)
    """
        - Take a dummy node
        - Take two pointer p1 and p2 , pointed at dummy node
        - Move p2 pointer n time forward to give a headstart
        - Then move both pointers together till p2 reaches the last element, then p1 would be behind the required element to delete
        - delete element by setting p1.next = p1.next.next
        - Return Dummy.next (as that is the head of the list)

        Note:- 
            - We use dummy node to deal with the edge case => Deleting the head element
            - which can't be done as we would return head only (if we didn't use dummy node)

    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(0, head)
        p1 = dummy
        p2 = dummy

        # Move one pointer n time forward
        for i in range(0,n):
            p2 = p2.next
        
        # Moving oth pointers simultaneosly until p2 reaches last element
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next

        # Performing deletion
        p1.next = p1.next.next

        return dummy.next

obj = Solution()

head = build_list([1,2,3,4,5])
n = 2

result = obj.removeNthFromEnd(head, n)

print("Answer List:")
print_list(result)