#EXAMPLE - BASIC
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name=restaurant_name
#         self.food_style=cuisine_type
    
#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.name} \nFood style: {self.food_style}")
    
#     def open_restaurant(self):
#         print("Restaurant is OPEN")

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.Flavours= ["chocolate", "vanilla", "strawberry"]

#     def display(self):
#         print(f"Here are all the flaours {self.Flavours}")

# x=IceCreamStand("Vadilal" , "icecream")
# x.display()


#-------------------------
#Example - BASIC
# class Person: #PARENT CLASS
#     def __init__(self, fname, lname):  
#         self.first_name=fname
#         self.last_name=lname
    
#     def printname(self):
#         print(f"A person of name {self.first_name} {self.last_name}")


# class Student(Person):  #CHILD CLASS (every student is a person. Extra feature -> the person having graduation year is a student.)
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname) # after using super(), child class can use all the properties and method of parent class
#         self.GradYear=year
    
#     def welcome(self):
#         print(f"Welcome {self.first_name} {self.last_name} to the {self.GradYear} batch")

# x=Person("uditya", "kumar")
# x.printname()

# y=Student("adi","pandey",1997)
# y.welcome()

# z=Student("Yuvi", "Yadav" , 2024)
# z.welcome()

#-------------------------------

#Example - BREAKING CLASSES INTO SEPARATE CLASSES
# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class Battery:
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
    
#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} miles on a full charge.")
    
#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()     <- we break battery portion in another class


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# my_tesla.battery.get_range()
# print("I'm upgrading the battery to 100 now.....")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()

#---------------------
#Example - BREAKING CLASSES INTO SEPARATE CLASSES
# class User:
#     def __init__(self, first_name, last_name, device, browser):
#         self.fname=first_name
#         self.lname=last_name
#         self.device=device
#         self.browser=browser

#     def describe_user(self):
#         print(f"user {self.fname} {self.lname} uses {self.device} and browser is {self.browser}")
    
#     def  greet_user(self):
#         print(f"Have a happy browsing {self.fname} {self.lname}")

# class Privileges:
#     def __init__(self):
#         self.privileges = ["can add post", "can delete post", "can ban user", "react on a post"]

#     def show_privileges(self):
#         print(f"Here are all the privileges to a user: {self.privileges}")

# class Admin(User):
#     def __init__(self, first_name, last_name, device, browser):
#         super().__init__(first_name, last_name, device, browser)
#         self.privileges = Privileges()  # Dviding one class into multiple separate classes

    

# x=Admin("udi","kumar","Apple","safari")
# x.privileges.show_privileges()
# print(x.fname)

#--------------------------
# #EXAMPLE -> MULTI -LEVEL INHERITANCE
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(car):   # "ToyotaCar" inherits all properties of "car"
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):  ## "Fortuner" inherites all the properties of both "ToyotaCar" and "car"
#     def __init__(self, brand,type):
#         super().__init__(brand)
#         self.type = type

# x= Fortuner("toyota", "diesel")
# x.start()
# print(x.brand)

#-----------
#Example -> child class inherting properties from multiple parent

# class A:
#     varA ="Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):   # C inherites properties of both parent A and B
#     varC = "Welcome to class C"

# x= C()

# print(x.varC)
# print(x.varB)
# print(x.varA)