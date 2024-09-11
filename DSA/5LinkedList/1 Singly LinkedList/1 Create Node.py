class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Method:- 1
#Creating node
node1= Node(10)
node2= Node(20)
node3= Node(30)

head = node1

#Establishing the link between Nodes
node1.next = node2
node2.next = node3
node3.next = None

#======================
#Method 2: Alternative Shorter way
# head= Node(10)
# head.next= Node(20)
# head.next.next= Node(30)