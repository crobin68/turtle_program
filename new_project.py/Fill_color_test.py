import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")


# Creation of turtles
alex = turtle.Turtle()


# set color for turtles 
alex.pencolor("light green")

alex.penup()
alex.goto(-100,100)
alex.pendown()


alex.speed(0)
alex.fillcolor("red")



def squares():
    for square_loop in range(10):
            alex.forward(25)
            alex.right(90)
            alex.forward(25)
            alex.right(90)
            alex.forward(25)
            alex.right(90)
            alex.forward(25)
            alex.right(90)
            alex.forward(25)
            
            


for loops in range(10):
    squares()
    alex.right(90)
    alex.forward(25)
    alex.right(90)
    alex.forward(250)
    alex.left(180)


alex.left(45)
alex.forward(354)







wn.exitonclick()