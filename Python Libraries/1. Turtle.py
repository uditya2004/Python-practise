from turtle import Turtle, Screen            #from "turtle" module , we import "Turtle" CLASS

my_turtle = Turtle()             #creating an object of Turtle class

#changing appearance of our turtle
my_turtle.shape("turtle")
my_turtle.color("black", "blue")       #my_turtle.color({outline}, {body filled color})

#Movements
my_turtle.forward(100)
my_turtle.backward(100)

my_turtle.right(45)










screen = Screen()                #creating an object of "Screen" class
screen.exitonclick()             # This will prevent the window to automatically close