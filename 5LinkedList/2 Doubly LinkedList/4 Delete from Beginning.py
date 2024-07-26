class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def show(head):
    current = head
    while current  != None :
        print(current.data, end= "-> ")
        current = current.next
    print("None")

def deleteFromBeg(head):
    if head == None:
        return None
    
    elif head.next ==None:
        return None
    
    else:
        head = head.next
        head.prev = None
        return head

#Creating Nodes
head = Node(10)
# node1 = Node(20)

#Linking Nodes
# head.next = node1
# node1.prev= head
show(head)

#------------------
#Delete From Beginning of List
head = deleteFromBeg(head)
show(head)
