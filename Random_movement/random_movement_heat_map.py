import turtle
import random

# Function to check if the turtle is out of bounds
def out_of_bounds(turtle, x_bound, y_bound):
    x, y = turtle.position()
    return abs(x) > x_bound or abs(y) > y_bound

# Function to move the turtle randomly
def move_randomly(turtle, x_bound, y_bound):
    angle = random.uniform(0, 360)  # Generate a random angle
    turtle.setheading(angle)  # Set the turtle's heading to the random angle
    turtle.forward(10)  # Move the turtle forward by a fixed amount

    # Check if turtle is out of bounds
    if out_of_bounds(turtle, x_bound, y_bound):
        turtle.penup()
        turtle.goto(0, 0)  # Reset turtle position to (0, 0)
        turtle.pendown()

# Function to calculate the distance from the origin
def distance_from_origin(turtle):
    x, y = turtle.position()
    return ((x ** 2) + (y ** 2)) ** 0.5

# Function to set turtle color based on distance from origin
def set_heatmap_color(turtle):
    distance = distance_from_origin(turtle)
    if distance > 200:
        turtle.color("red")
    elif distance > 100:
        turtle.color("yellow")
    else:
        turtle.color("blue")

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

# Create the turtle
bob = turtle.Turtle()
bob.hideturtle()

# Define the boundary box
x_bound = 250
y_bound = 250

# Set the initial position of the turtle
bob.speed(0)
bob.penup()
bob.goto(0, 0)
bob.pendown()

# Move the turtle randomly within the boundary box
while True:
    move_randomly(bob, x_bound, y_bound)
    set_heatmap_color(bob)

# Keeps the window open until it's closed manually
wn.mainloop()
