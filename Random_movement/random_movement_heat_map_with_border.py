import turtle
import random
import subprocess

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
        turtle.penup()     # pick up pen before 0,0
        turtle.goto(0, 0)  # Reset turtle position to (0, 0)
        turtle.pendown()   # pen down when at

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

def set_heatmap_color_for_bob2(turtle):
    distance = distance_from_origin(turtle)
    if distance > 200:
        turtle.color("blue")
    elif distance > 100:
        turtle.color("yellow")
    else:
        turtle.color("red")

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

# Create the turtle for drawing the border
border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")

# Draw the border
border_pen.penup()
border_pen.goto(-250, 250)
border_pen.pendown()
for _ in range(4):
    border_pen.forward(500)
    border_pen.right(90)

# Create the turtle for the moving object
bob2 = turtle.Turtle()
bob = turtle.Turtle()
bob.hideturtle()
bob2.hideturtle()

# Define the boundary box
x_bound = 250
y_bound = 250

# Set the initial position of the turtle
bob2.speed(0)
bob2.penup()
bob2.goto(0, 0)
bob2.pendown()

bob.speed(0)
bob.penup()
bob.goto(0, 0)
bob.pendown()

# Write "x" on the screen
bob.write("x", align="center", font=("Arial", 24, "normal"))


# Open a new command prompt window and run a Python script to continuously print "x"
subprocess.Popen(['cmd', '/k', 'python', '-c', 'x = 0\nwhile True:\n    print("You have run this program", x, "times.")\n    print("You have run this program", x, "times."\n    x += 1'])


# Move the turtle randomly within the boundary box
x = 0
while True:
    move_randomly(bob, x_bound, y_bound)
    move_randomly(bob2, x_bound, y_bound)
    set_heatmap_color(bob)
    set_heatmap_color_for_bob2(bob2)
    x = x + 1
    print(x)

# Keeps the window open until it's closed manually
wn.mainloop()
