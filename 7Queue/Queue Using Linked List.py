class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Myqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def Enque(self, data):
        new_node = Node(data)

        if self.rear == None:           # If the element is added in an empty Queue , it should be made front and rear both
            self.front = new_node       # we update the front only when the Queue is empty 
        
        else:        
            self.rear.next = new_node   # Linking the new_node with the rear

        self.rear = new_node            # Shifting rear to new_node
        self.size +=1
    

    def Deque(self):
        if self.front == None:
            print("Underflow")
            return None
        
        else:
            prev = self.front.data            # Storing the data, before moving the front pointer
            self.front = self.front.next      # We move the front, without having to deallocate memory as in python automatic garbage collections happens

            if self.front == None:            # For tackling the case when we have only 1 element which is removed and front is now None
                self.rear == None

            self.size -=1

            return prev


    def GetFront(self):
        if self.front == None:  
            print("Empty Queue")
            return None
        
        else:
            return self.front.data
    

    def GetRear(self):
        if self.front == None:
            print("Empty Queue")
            return None
        
        else:
            return self.rear.data
    

    def isEmpty(self):
        return (self.size == 0)



"""
10      20     30
^               ^
front           Rear

"""
q= Myqueue()

q.Enque(10)
q.Enque(20)
q.Enque(30)

print("Deque Operation: ",q.Deque())

print(q.size)

print(q.GetFront())

print(q.GetRear())

print(q.isEmpty())
