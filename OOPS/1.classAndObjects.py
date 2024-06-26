"""
Naming conventions:
1. object = instance (eg : x,y,z in code below)
2. Attribute = Instance variable  (self.name)
3. method -> open_restaurent , __init__ , describe_ restaurent
4. __init__ = special method called "constructor"
5.  Class variable -> (wheel)

6. Shared State = for "x", "y", "z" , the class variable "wheels" is a shared state
"""

#EXAMPLE 1 -> BASIC(CLASS WITH PROPERTIES AND MULTIPLE METHODS)

# class Restaurant:
#     wheel = 0  # just to explain naming

#     def __init__(self, restaurant_name, cuisine_type):
#         self.name=restaurant_name
#         self.food_style=cuisine_type
    
#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.name} \nFood style: {self.food_style}")
    
#     def open_restaurant(self):
#         print("Restaurant is OPEN")

# #Creating an Instance:
# x= Restaurant("Swada", "Indian")
# y= Restaurant("Dhaba", "south")
# z= Restaurant("Mayuri", "East")

# # Modifying the class variable
# Restaurant.wheels = 6

# #Calling the Method:
# x.describe_restaurant()
# y.describe_restaurant()
# z.describe_restaurant()
# x.open_restaurant()

#-------------------------------------------------
#EXAMPLE -> BASIC(CLASS WITH PROPERTIES AND MULTIPLE METHODS)
# #EXAMPLE

# class car:
#     def __init__(self, make, car_model, year):
#         self.make=make
#         self.model=car_model
#         self.year=year
#         self.odometer_reading=0
    
#     def update_odometer(self, new_reading):
#         if new_reading>=self.odometer_reading:
#             self.odometer_reading = new_reading
#             print(f"New reading is {self.odometer_reading}")
        
#         else:
#             print(f"Odometer current reading is {self.odometer_reading}. You can't  roll back.")
    
#     def increment_odometer(self, new_read):
#         self.odometer_reading += new_read
#         print(f"New reading is {self.odometer_reading}")



# x= car("Audi", "A4", 2005)
# print(x.model)
# x.update_odometer(24)

# x.increment_odometer(13)

#-----------------------------------

#Example 2 -> BASIC(CLASS WITH PROPERTIES AND MULTIPLE METHODS)

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

# x= User("rahul", "pandey", "MI", "chrome")
# print(x.lname)  
# x.describe_user()
# x.greet_user()


# x= User("Uditya", "pandey", "Asus", "Brave")
# x.describe_user()
# x.greet_user()

# x= User("Aditya", "pandey", "Apple", "Safari")
# x.describe_user()
# x.greet_user()

#-------------------------------------

