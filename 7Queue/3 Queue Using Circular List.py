"""
→ In normal list implementation, appending at the end is O(1) Operation, but pop(0) is O(N) operation as we will have to shift all the elements 1 step forward after removing the element from the start.
   To solve this we use Circular List Implementation (making both operations O(1)).

→ In circular List implementation is cache friendly as well as it's based on array implementation

Notes:-
→ In circular List, We cap the size of array (specify the fixed size beforehand).
→ In circular List, we utilize the empty spaces efficiently , no space is wasted in a fixed size array.

→ In circular List, we use 3 formula's to get the value of front and rear:- 
        → Incrementing front by 1 = (front + 1) % cap
        → Incrementing rear by 1 = (rear + 1) % cap
        → rear = (self.front + self.size - 1) % self.cap

   """

class MyQueue:
	def __init__(self, c):
		self.cap = c         # Set the capacity of the queue
		self.l = [None] * c  # The list is of fixed size, equal to the capacity c of the queue, and is initially filled with None to indicate that the positions in the list are empty. So, if c is 4, the expression [None] * c will result in [None, None, None, None].
      
		self.size = 0        # Initialize the size of the queue = 0
		self.front = 0       # Initialize the front Index = 0


	def GetFront(self):
		if self.front == None:
			print("Emtpy Queue")
			return None
		else:
			return self.l[self.front]  # Every element is stored in a list, and index of front element is stored in self.front
	

	def GetRear(self):
		if self.size == 0:
			print("Empty Queue")
		
		else:
			rear = (self.front + self.size - 1) % self.cap   #Finding the rear Index using formula, as we don't maintain rear now like we do for front.
			return self.l[rear]
	

	def Enque(self, data ):
		if self.size == self.cap:    #If the list is already full we don't add any extra element
			print("List capacity Full")
			return None
		
		else:
			rear = (self.front + self.size - 1) % self.cap
			rear = (rear + 1) % self.cap

			self.l[rear] = data
			self.size +=1
	

	def Deque(self):
		if self.size == 0:
			print("Empty Queue")
			return None
		
		else:
			prev = self.l[self.front]
			self.front = (self.front + 1) % self.cap
			
			self.size -=1
			return prev


	def isEmpty(self):
		return (self.size == 0)


q = MyQueue(5)    #We initialize a queue with storing capacity = 5

q.Enque(10)
q.Enque(20)
q.Enque(30)

print(q.Deque())

print(q.size)

print(q.GetFront())
print(q.GetRear())
print(q.isEmpty())