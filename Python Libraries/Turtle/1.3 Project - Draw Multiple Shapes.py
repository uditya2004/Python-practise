from turtle import Turtle, Screen

tim = Turtle()

def shapes(n, color):
    for p in range(n):
        tim.color(color)
        tim.forward(100)
        tim.right(360/n)



colors = ["deep sky blue", "blue", "green", "orange", "grey", "black", "gold", "deep pink", ]

for i in range(3,11):
    shapes(i, colors[i-3])




Screen = Screen()
Screen.exitonclick()