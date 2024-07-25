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
    

def InsertAtEnd(head,data):
    new_node = Node(data)
    if head == None:
        return new_node
    else:
        current = head
        while current.next != None:
            current = current.next
        
        new_node.prev = current
        current.next = new_node
        return head

    
#Creating node
head = Node(10)   
node2 = Node(20)

#Linking Node
head.next = node2
node2.prev = head

head = InsertAtEnd(head, 60)
head = InsertAtEnd(head, 90)
show(head)
