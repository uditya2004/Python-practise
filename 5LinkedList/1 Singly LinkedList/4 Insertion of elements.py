class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def show(head):
    current = head             #Starting with the object passed i.e head
    while current != None:          
        print(current.data, end= "-> ")
        current = current.next
    print("None")
    

def InsertAtBeginning(head,data):     #TC: O(1) , SC: O(1)
    new_node = Node(data)      #created a node
    new_node.next = head       #set next pointer of the new node to head
    return new_node            #returning the new_node will be stored in head. Thus the head pointer will be updated


def InsertAtEnd(head,data):      #TC: O(n) , SC: O(1) (If we maintain a "Tail" (just like head) then TC will become O(1))
    if head == None:      #If the LinkedList is empty   (Here "self" and "head" are same, but we write "head" to improve readability.)
        return Node(data)
    
    current = head
    while current.next != None:  
        current = current.next
    
    new_node = Node(data)
    current.next = new_node
    return head                #Indicating no change in head, and preventing from making function void
    

def InsertAtPosition(head,position, data):
    new_node = Node(data)
    if position ==1:                #When we insert at the head
        new_node.next = head
        return head
    
    current = head                  #Traversing till the position before the required position
    for i in range(0,position-2):  
        current =current.next
    
        if current == None:         #Let's say we want to fill 5th position but 4th is not filled before it (going beyond the length of list), Then we don't do any changes
            return head             #We don't do any changes
    
    new_node.next = current.next
    current.next = new_node
    return head                     #Just to prevent the function to return null value


def InsertAfterNode(head, position, data):
    new_node = Node(data)
    current = head

    for i in range(0, position-1):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


def InsertBeforeNode(head, position, data):
    new_node = Node(data)
    current = head

    for i in range(0, position-2):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


#Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original: ",end = " ")
show(head)

#--------------------------
#Insert at the beginning
print("\nInsert at the beginning")
head = InsertAtBeginning(head, 40)    #We store the returned value in head
show(head)

#--------------------------
#Insert at the End
print("\nInsert at the End")
head = InsertAtEnd(head,40)
show(head)

#--------------------------
#Insert At 3rd position
print("\nInsert At 3rd position")
head = InsertAtPosition(head, 5, 70)
show(head)

#--------------------------
#Insert after 3rd position
# head = InsertAfterNode(head, 3, 70)
# show(head)

#--------------------------
#Insert before 3rd position
# head = InsertBeforeNode(head, 3, 70)
# show(head)