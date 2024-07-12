#3 Types of decoraters - static, property , class
"""
Decorators are a powerful way to modify the behavior of functions or methods without directly changing their code.

1. The @staticmethod decorator is used to define a method within a class that doesn't need access to the instance of that class (i.e., self) or the class itself (i.e., cls).
        a) static method function can't access  can't access or modify the instance variable or class variable because they don't receive self or cls as their first parameter.

2. classmethod  - Class methods are particularly handy when you need to interact with class-level variables. They can access, modify, or use these variables directly.
"""
#Example -> STATIC METHOD

# class Student:
#     name="rahul"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     @staticmethod # this makes "def hello" static method , so now we don't have to write parameter "self" in def. Without this it will give error.
#     def hello():  #it doesn't have access to individual instance attributes like self.marks
#         print ( "Hello")
    
#     def get_avg (self) :
#         sum =0
#         for val in self.marks:
#             sum += val
#         print (f"hi {self.name} your avg score is: {sum/3}")
#         Student.hello()


# sl = Student ("tony stark" ,[99, 98, 97])
# sl. get_avg()
# sl. hello()

#----------------------------------
#EXAMPLE -> CLASS METHOD = Changing the variable in the class (i.e "name" here)
# class Person:
#     name= "anonymous"

#     #METHOD 1
#     # def changeName(self, name) :  # this method not recommended due to reading confusion issues
#     #     self.__class__.name = name
    
#     #METHOD 2
#     # def changeName(self,name):  #it's recommended not to use this method , reason below
#     #     Person.name= name

#     #METHOD 3
#     # @classmethod
#     # def changeName(cls, name) : # passing cls rather than "self" here
#     #     cls.name = name

# pl = Person()
# pl. changeName("rahul kumar")
# print (pl. name)
# print (Person. name)

"""
Why not use METHOD 1
1. Using self.__class__.name = name might obscure the fact that you are directly modifying a class attribute. Someone reading your code (including yourself in the future!) might need an extra moment to realize you're not dealing with a typical instance attribute.
   The @classmethod decorator immediately signals that the method operates at the class level. It improves the readability of your code and makes your intentions more obvious.

------------------------------------------------------------
Why not use METHOD 2
1. This becomes problematic if you were to subclass Person — the method would always modify the name attribute of the Person class, not the subclass.

Example

class Person:
    name = "anonymous"

    def changeName(self, name):  # Hardcoded 'Person'
        Person.name = name

class Student(Person):  
    pass 

person1 = Person()
student1 = Student()

person1.changeName("Alice") 
print(Person.name)  # Output: Alice
print(student1.name)  # Output: Alice 

student1.changeName("Bob")  
print(Person.name)  # Output: Bob  <-- PROBLEM!   (when student1.changeName("Bob") is called, it also modifies the name of the Person class, even though the call was made on a Student instance. This is because the method is hardwired to change Person.name.)
print(student1.name)  # Output: Bob 

-----
CORRECT SOLUTION

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

class Student(Person):
    pass

person1 = Person()
student1 = Student()

person1.changeName("Alice")
print(Person.name)  # Output: Alice
print(student1.name)  # Output: Alice 

student1.changeName("Bob") 
print(Person.name)  # Output: Alice 
print(student1.name)  # Output: Bob  <-- Correct behavior!

"""
#---------------------------
#Example -> PROPERTY METHOD = it changes a property automatically if values changes

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
    
#     # #Method 1
#     # def percentage(self):
#     #     print(str((self.phy + self.chem + self.math) / 3) + "%")
    
#     # #Method 2
#     # @property
#     # def percentage(self):
#     #     return  str((self.phy + self.chem + self.math) / 3) + "%"
    

# stul = Student (98, 97, 99)


# #Method 1
# stul.percentage()

# stul.phy = 86
# stul.percentage()

#=======
# #Method 2
# print (stul.percentage)

# stul.phy = 86
# print (stul. percentage)

"""
Method 1:  notice how you call stul.percentage(). This syntax makes it look like you're calling a function that performs an action rather than accessing a value (the percentage).

Method 2:  With the @property decorator, you access stul.percentage as if it were a regular attribute. No parentheses () needed! This makes your code more readable and intuitive.
           The logic inside the method remains hidden, providing a clean abstraction. 
"""