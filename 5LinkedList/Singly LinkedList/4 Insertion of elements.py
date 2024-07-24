class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def show(self):
        current = self             #Starting with the object passed i.e head
        while current != None:          
            print(current.data, end= "-> ")
            current = current.next
        print("None")
    

    def InsertAtBeginning(self,data):     #TC: O(1) , SC: O(1)
        new_node = Node(data)      #created a node
        new_node.next = self       #set next pointer of the new node to head
        return new_node            #returning the new_node will be stored in head. Thus the head pointer will be updated


    def InsertAtEnd(self,data):      #TC: O(n) , SC: O(1) (If we maintain a "Tail" (just like head) then TC will become O(1))
        if head == None:      #If the LinkedList is empty   (Here "self" and "head" are same, but we write "head" to improve readability.)
            return Node(data)
        
        current = head
        while current.next != None:  
            current = current.next
        
        new_node = Node(data)
        current.next = new_node
        return head                #Indicating no change in head, and preventing from making function void
    
    def InsertAtPosition(self,position, data):
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

    def InsertAfterNode(self, position, data):
        new_node = Node(data)
        current = self

        for i in range(0, position-1):
            current = current.next

        new_node.next = current.next
        current.next = new_node


    def InsertBeforeNode(self, position, data):
        new_node = Node(data)
        current = self

        for i in range(0, position-2):
            current = current.next

        new_node.next = current.next
        current.next = new_node


#Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original: ",end = " ")
head.show()

#--------------------------
#Insert at the beginning
# head = head.InsertAtBeginning(40)    #We store the returned value in head
# head.show()

#--------------------------
#Insert at the End
# head = head.InsertAtEnd(40)
# head.show()

#--------------------------
#Insert At 3rd position
head = head.InsertAtPosition(5, 70)
head.show()

#--------------------------
#Insert after 3rd position
# head.InsertAfterNode(3, 70)
# head.show()

#--------------------------
#Insert before 3rd position
# head.InsertBeforeNode(3, 70)
# head.show()