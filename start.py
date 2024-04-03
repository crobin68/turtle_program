import turtle
from turtle import *
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)



wn = turtle.Screen()                            # Set up the window and its attributes
wn.setup(width=1000, height=800)                 # Set window size to 600x400          
wn.bgcolor("Black")


bob = turtle.Turtle()
bob.color("Black")
bob.pensize(2)
bob.penup()
#bob.setx(500)
#bob.sety(400)
bob.speed(0)
bob.pendown()





p = 0
x = 0
for loop in range(200):
    for a in range(10):
        x += 2                  # Increase x by a small amount to create the spiral effect
        bob.forward(1 + x)
        bob.right(85)
        bob.color(random_color())
    print(p)
    bob.right(180)
    q = 15
    for b in range(q):
        x += -2                 # Increase x by a small amount to create the spiral effect
        bob.forward(1 - x)
        bob.left(-85)
        bob.color(random_color())

            
    















#Bob.forward(80)                 # Let tess draw an equilateral triangle
#Bob.left(120)
#Bob.forward(80)
#Bob.left(120)
#Bob.forward(80)
#Bob.left(120) 
#Bob.forward(100)
##Bob.forward(80)                 # Let tess draw an equilateral triangle
#Bob.left(120)
#Bob.forward(80)
#Bob.left(120)
#Bob.forward(80)
#Bob.left(120) 
#Bob.forward(100)
wn.exitonclick()


