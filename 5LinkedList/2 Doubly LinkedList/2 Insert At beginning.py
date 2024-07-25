class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
def show(head):
    current = head
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")
    

def InsertAtBeg(head,data):
    new_node = Node(data)
    
    if head != None:        # If head is initally None , then we don't access it's prev
        head.prev = new_node

    new_node.next = head
    return new_node
    
    
head = None   #Assuming empty linked list
head = InsertAtBeg(head, 10)
# head = InsertAtBeg(head, 20)
show(head)
