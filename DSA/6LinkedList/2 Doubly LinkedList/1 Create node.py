class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Created Nodes
head= Node(10)
node2= Node(20)
node3= Node(30)

#Linking Nodes
head.next = node2
# head.prev = None         #We generally don't mention "None part"

node2.next = node3
node2.prev = head

# node3.next = None 
node3.prev = node2


