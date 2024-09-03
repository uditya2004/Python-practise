#Method 1:- Using color - Line drawn will be of same color as of Turtle 
from turtle import Turtle, Screen

tim = Turtle()

# for j in range(4):
#     for i in range (10):
#         tim.color("black")
#         tim.forward(10)

#         tim.color("white")
#         tim.forward(10)
    
#     tim.right(90)





#Method 2: Using Pendown and penup

for j in range(4):
    for i in range (10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    
    tim.right(90)



screen = Screen()
screen.exitonclick()