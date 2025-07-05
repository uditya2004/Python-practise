class Node:
    def __init__(self, key, val):
        # Data
        self.key = key    
        self.val = val

        #Pointers
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}   # hashmap

        """
        left node -> it's next node indicates = least recently used
        right node -> it's prev node indicated => most recently used
        """
        self.left, self.right = Node(0,0), Node(0,0)                # created a dummy Node -> left and right

        # setting pointers of left and right Nodes
        self.left.next, self.right.prev = self.right, self.left     # new nodes will be added in between these 2 dummy nodes
        
    # function to delete the node from the linked list
    def delete(self, Node):
        # storing the node's next and prev nodes
        prevNode = Node.prev
        nextNode = Node.next
        
        # updating the next and prev pointers
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # function to insert the given Node between the right node and the right Node's prev Node (becomes the last 2nd Node)
    def insert(self, Node):
        prevNode, nextNode = self.right.prev, self.right

        prevNode.next = nextNode.prev = Node

        # setting the prev and next pointer of the given node
        Node.prev = prevNode
        Node.next = nextNode


    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])    # deleting the node from the linked list
            self.insert(self.cache[key])    # insert the node just before the right node, as on accessing this node , it becomes most recently used node
            return self.cache[key].val          # return the value of the node
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])     # if te node is already present we delete the previous node , so as to update the value of the node.
        
        self.cache[key] = Node(key, value)    # creating and assigning a node to the key
        self.insert(self.cache[key])          # adding the Node inside the linked list between the "left" and "right" Node.

        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.delete(LRU)         # de-Linking the LRU node from the Linked List
            del self.cache[LRU.key]  # deleting the key of LRU from the hashmap (cache), which also removes it's associated value along with it