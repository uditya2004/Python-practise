class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Method 1:- Better Solution (Using HashMap)
    """
    APPROACH:
    1. create a hashmap to map the old node to the coressponding copy node.
    2. In the 1st traversal through the linked list , only create a copy node of each node with the data , don't set any pointers
    2. In the 2nd traversal through the linked list, create the pointers between the copy nodes.
    """
    # TC: O(2N) = O(N)
    # SC: O(N)
    def copyRandomList(self, head):
        
        # SC: O(N)
        oldToCopy = {None : None}  # hashmap to map the old node to the corresponding copy node (initialized to "None: None" to handle the edge case that old "None" maps to "None" in copied linked list.)
        
        # 1st Pass:- create a node (only having data, no pointers) and map the to old nodes using Hashmap
        # TC: O(N)
        curr = head
        while curr != None:
            copy = Node(curr.val)   #creating the copy node
            oldToCopy[curr] = copy
            curr = curr.next
        
        # 2nd Pass:- establish the "next" and "random" pointers between the Copy Nodes
        # TC: O(N)
        curr = head
        while curr != None:
            copy = oldToCopy[curr]     # oldToCopy[curr] will return the copy node associated with it in the hashmap
            copy.next = oldToCopy[curr.next]      # setting the next pointer of the copy node to the copy node associated with the curr.next
            copy.random = oldToCopy[curr.random]  # setting the random pointer of the copy node to the copy node associated with the curr.random
            curr = curr.next                      # move the curr pointer ahead
        
        return oldToCopy[head]
    


    # Method 2:- Best Solution
    # TC: O(3N) = O(N)
    # SC: O(1)
    def copyRandomList(self, head):
        
        # Create a copy node and insert in between the nodes of the original linked list.
        # TC: O(N)
        curr = head
        while curr != None:
            copy = Node(curr.val)   # created a copy node
            copy.next = curr.next   # setting copy node's next
            curr.next = copy        # updating curr node's next
            curr = curr.next.next   # moving to the next element of the original list (which is the 1 node ahead of curr as we inserted copy node in between them)
        
        # connecting the random pointer of the copy nodes.
        # TC: O(N)
        curr = head
        while curr != None:
            copy = curr.next                # original node's next node is a copied node of itself
            if curr.random != None:
                copy.random = curr.random.next  # setting the random pointer of the copied node to the curr.random node's copied node , which is it's next one , hence curr.random.next
            else:
                copy.random = curr.random       # edge case : where curr.random is "None", so directly point copy.random to "None"
            
            curr = curr.next.next           # moving the pointer to the next original node.
        
        # connect Next pointer of the copy node (this step will separate copied Linked list from the original linked list).
        # TC: O(N)
        curr = head
        dummy = Node(-1)                 # creating a dummy node
        res = dummy                      # pointer pointing to the dummy node.
        while curr != None:
            res.next = curr.next         # setting the next pointer of copied node to point next copies node
            curr.next = curr.next.next   # setting the next pointer of original node to point to original next node
            
            res = res.next               # moving the "res" pointer to the next copied node
            curr = curr.next             # moving the "curr" pointer to the next original node


        return dummy.next