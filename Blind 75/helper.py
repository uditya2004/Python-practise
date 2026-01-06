# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr: list) -> ListNode:
    dummy = ListNode()
    
    curr = dummy
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next
    
    return dummy.next


def print_list(head: ListNode) -> list:
    result = []
    curr = head
    while curr != None:
        result.append(curr.val)
        curr = curr.next
    
    return result

