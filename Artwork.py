import turtle
import time
import random




wn = turtle.Screen()
wn.bgcolor("black")


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

alex = turtle.Turtle()  #create turtle
alex.color(random_color())  #set turtle pen color

alex.goto(0,0)  #move turtle to the (x y of 0)
# Function to move turtle forward
def move_forward():
    
    alex.pendown()
    alex.speed(0)

    x = 0 #seet the pos for alex on the x plane
    y = 0 #set the pos for alex on the y plane
    alex.setheading(90)
    alex.color(random_color())

    for loop in range(1):
        alex.color(random_color())
        x + 50
        y - 50
        alex.goto(x,y)



        for back_forth in range(180):
            alex.right(0.5)
            alex.backward(120)

            alex.forward(400)
            alex.right(93.7)

wn.listen()
wn.onkeypress(move_forward, "a")




























turtle.exitonclick()