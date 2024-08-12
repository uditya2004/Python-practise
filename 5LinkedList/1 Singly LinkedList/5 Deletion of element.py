class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def show(self):
        current = self       #Starting with the object passed i.e head
        while current != None:
            print(current.data, end= "-> ")
            current = current.next
        print("None")

    def DeleteFromBeginning(self):          #TC: O(1), SC: O(1)
        if head == None:   
            return None
        else:                   #We just have to move the head. Deallocating memory is taken care by Python
            return head.next
    
    def DeleteFromEnd(self):
        if head == None:   #Empty Linked List
            return None
        
        if head.next == None:  #List with single element
            return None
        
        current = head
        while current.next.next !=None:
            current = current.next
        
        current.next = None
        return head
    
    def DeleteFromPosition(self, position):
        current = head
        for i in range(0,position-2):
            current = current.next
        
        current.next = current.next.next
        return head
    
    def DeleteBeforePosition(self, position):
        if head == None or position <= 0:
            return None
        
        current = head
        for i in range(0,position-3):
            current = current.next
        
        current.next = current.next.next
        return head
    
    def DeleteAfterPosition(self, position):
        if head == None or position <= 0:
            return None
        
        else:
            current = head
            for i in range(0,position-1):
                current = current.next
            
            if current.next != None and current.next.next != None:
                current.next = current.next.next
            else:
                current.next = None
            return head




#Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)


print("Original: ",end = " ")
head.show()

#--------------------------
#Deletion from the beginning
print("\nDelete from the beginning")
head = head.DeleteFromBeginning()
head.show()

#--------------------------
#Deletion from the End
print("\nDelete from the End")
head = head.DeleteFromEnd()
head.show()

#--------------------------
#Deletion from the Postion
print("\nDelete from the Postion")
head = head.DeleteFromPosition(2)
head.show()

#--------------------------
#Deletion before position
print("\nDelete before positon")
head = head.DeleteBeforePosition(3)
head.show()

#--------------------------
#Deletion After position
print("\nDelete after position")
head = head.DeleteAfterPosition(2)
head.show()