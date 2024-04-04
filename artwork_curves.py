import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

artwork = turtle.Turtle()
artwork.color("white")
artwork.pendown()

# Make turtle random colors
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

artwork.speed(0)

# Variables for spiral parameters
length = 10
angle = 90
increment = 2
clockwise = True  # Start with clockwise rotation

# Draw spiral
for Sprial in range(200):
    artwork.forward(length)
    if clockwise:
        artwork.left(angle)
    else:
        artwork.right(angle)
    length += increment
    artwork.color(random_color())  # Set random color for each segment of the spiral
    print(artwork.position())

turtle.done()