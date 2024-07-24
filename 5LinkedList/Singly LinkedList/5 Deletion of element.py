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




#Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original: ",end = " ")
head.show()

#--------------------------
#Deletion from the beginning
head = head.DeleteFromBeginning()
head.show()