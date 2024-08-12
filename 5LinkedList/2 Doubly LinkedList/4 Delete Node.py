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

def DeleteFromEnd(head):
    if head == None:
        return None
    if head.next == None:
        return None
    
    current = head
    while current.next.next != None:
        current = current.next
    
    current.next = None
    return head

#Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)

#Linking Nodes
head.next = node2

node2.prev = head
node2.next = node3

node3.prev = node2
print("Original list:- ")
show(head)

#------------------
#Delete From Beginning of List
print("\nDelete From Beginning")
head = deleteFromBeg(head)
show(head)

#=============
#Delete from end
print("\nDelete From End")
head = DeleteFromEnd(head)
show(head)