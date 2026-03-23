"""
Our needs:-
1. Access any element using it's key in O(1) ==> Only Dictionary can do this

2. Remove the node from in between
3. Remove the node from the end (LRU element removal on hitting full capacity)

We need to do 2 and 3 operation in O(1) time ==> Can only be done using DOUBLY LINKED LIST

========================================================
APPROACH:
- For storing element associated with key, we use Dictionary  ==> {key: ???}  =>> here ??? will be NODE reference, so we can easily access the node.
- For keeping track of usage order of element we use double linked list

- We use two dummy nodes at both the ends of Linked list to keep track of "head" and "tail" => Let's Say "LEFT_END" and "RIGHT_END"

- LEFT_END represents:- Most recently used
- RIGHT_END represents:- Least recently used

- get(key):
    - Remove the node associated with the key from the linked list
    - Add it after "LEFT_END" Node
    - access the elemen using dictionary => returndict[key]

- put(key, value)
    - if key in dictionary:
        - Delete the node

    - Add the new node after the "LEFT_END" Node
    
    - if len(Dictionary) > capacity:
        - Remove element before "RIGHT_END"

"""



class Node:
    def __init__(self, key, val):
        # Data
        self.key = key     # We store "key" in the Node because when we remove Least recently used node from the tail, we need to know which key (associated with the removed node) to remove from the HashMap as well!
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
        # new nodes will be added in between these 2 dummy nodes
        # Doubly Linked List
        self.left.next = self.right
        self.right.prev = self.left
        
    # function to delete the node from the linked list
    def delete(self, Node):
        # storing the node's next and prev nodes
        prevNode = Node.prev
        nextNode = Node.next
        
        # updating the next and prev pointers
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # function to insert the given Node between the right node and the right Node's prev Node (becomes the node before "right" node)
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