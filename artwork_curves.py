import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

artwork = turtle.Turtle()
artwork.color("white")
artwork.pendown()


# make turtle random colors
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)





change = 100000

artwork.speed(0)
for __ in range(20):
    artwork.color(random_color())
    for _ in range(70):
        
        artwork.forward(10)
        artwork.right(5)
        















turtle.exitonclick()