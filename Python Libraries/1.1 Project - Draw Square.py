from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("Blue")

for i in range(0,4):
    timmy.forward(100)
    timmy.right(90)


Screen = Screen()
Screen.exitonclick()