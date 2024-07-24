#Ques: Search element 30 and return it's position in linkedList. If not present return -1.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def show(self):
        current = self
        while current != None:
            print(current.data, end= "-> ")
            current = current.next
        print("None")


    def search(self,data):
        current = self       #Starting with the object passed i.e head
        count= 0
        while current != None:     #Traversing through the complete list
            count +=1

            if current.data == data:
                return count
            
            current = current.next
        
        return -1


#Creating a linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head.show()

#=================
#Searching
print(head.search(30))