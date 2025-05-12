class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    """
    APPROACH
    - traverse through the linked list and put each node object in a set(). Set will store the memory location of the node (so two node with same node.data but different memory location will be considered unique nodes). This help solution to work with nodes with duplicate data.
    - before puttin the node object to set(), check :-
        - if it already exists means -> current node memory address is already present in the set means we are cycled back to the same node . So the cycle exists
    """
    #Method 1
    # TC: O(N)
    # SC: O(N)
    # def hasCycle(self, head) -> bool:
    #     visited = set()        # memory locations of node is stored in this set . Eg of each element:- <__main__.ListNode object at 0x0000021257F49E00>
    #     curr = head

    #     while curr != None:
    #         if curr in visited:
    #             return True
    #         else:
    #             visited.add(curr)   # we stored the Node object in the set instead of node's data , as there can be nodes with same data.
    #             curr = curr.next
        
    #     return False

    #===============================

    """
    APPROACH
    - take two pointer "slow" and "fast". Both pointers moves together
        - "slow" move 1 step at a time
        - "fast" move 2 steps at a time.
    - Check:
        - if the fast or fast.next reaches "None" , means we reached the end of the linked list means no loop present in the linked list.
        - if the fast and slow pointers meet, then we must have cycled back and there exist a loop in the linked list.
    """
    # Method 2: Floyd's Tortoise & Hare Algo  (Two pointer approach)
    # TC: O(N)
    # SC: O(1)
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:  # if both the pointers meet , then there is a loop
                return True
            
        return False
        
    




head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

obj = Solution()
print(obj.hasCycle(head))