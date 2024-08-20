class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def show(head):
    curr = head
    while curr != None:
        print(curr.data,end = "-> ")
        curr = curr.next
    print("None")

def InsertAtBeg(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def InsertAtEnd(head , data):
    new_node = Node(data)
    
    if head  == None:
        return new_node
    
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node

        return head


#DRIVER CODE
head = None
# head.next = Node(20)
show(head)

head = InsertAtBeg(head, 1)
show(head)

