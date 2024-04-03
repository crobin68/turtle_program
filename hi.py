import turtle
from turtle import *
import time
import random

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set her pen width
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("green")              # set his color

a = turtle.Turtle()              # create a
alex.color("hotpink")            # set his color


tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


def more_square():
    alex.right(23.78)
    alex.forward(70)

alex.color(random_color())
alex.speed(0)
alex.begin_fill()





alex.pensize(1)
def squareness():
    alex.begin_fill()
    alex.fillcolor(random_color())
    for square in range(5):
        alex.forward(30)                 # make alex draw a square
        alex.color(random_color())
        alex.left(90)
    alex.end_fill()
    more_square()
    squareness()
squareness()






wn.listen()









wn.exitonclick()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

for SPEED in range(200):
        
        a.pencolor(random_color())
        a.speed(10000)
        a.color(random_color())
        a.pensize(10)
        a.left(-39.45)
        a.forward(-100)


        alex.pencolor(random_color())
        alex.speed(10000)
        alex.color(random_color())
        alex.pensize(10)
        alex.left(39.45)
        alex.forward(100)

wn.exitonclick()


#for Turtle_spin_1000_times in range(1000):
#    alex.pencolor(random_color())  # Corrected: Added parentheses to call random_color() function
#    alex.speed(10000)
#    alex.color(random_color())
#    alex.pensize(10)
#    alex.left(39.45)
#    alex.forward(100)

#for Turtle_spin_1000_times in range(1000):
#    a.pencolor(random_color())  # Corrected: Added parentheses to call random_color() function
#    a.speed(10000)
#    a.color(random_color())
#    a.pensize(10)
#    a.left(-39.45)
#    a.forward(-100)





