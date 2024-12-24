"""In polymorphism, we learn:
1. operator overiding (eg: changing the meaning of arithmetic operators like +)
2. use of dunder functions(functions having "__" in there start and end) - 

Note: Dunder functions are pre defined in python documentation(https://docs.python.org/3/reference/datamodel.html) and have different operations and syntax to operate through them.
"""

#EXAMPLE -> Defining a class to perform addition of complex number , which is not present in python by default.

class Complex:
    def __init__(self, real, img):
        self.real= real
        self.img= img
    
    def display(self):
        print(f"{self.real}i + {self.img}j")
    
    def __add__(self,otherno):
        return Complex(self.real + otherno.real, self.img + otherno.img)

    


num1= Complex(1,2)
num1.display()

num2= Complex(3,4)
num2.display()

num3= num1 + num2
print(f"{num3.real}i + {num3.img}j")

#=================
# Example 2
class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,o):
        return self.a + o.a

obj1 = A(1)
obj2 = A(2)
obj3 = A("Uditya")
obj4 = A("Kumar")

print(obj1 + obj2)    # Actual working:- A.__add__(ob1 , ob2)
print(obj3 + obj3)