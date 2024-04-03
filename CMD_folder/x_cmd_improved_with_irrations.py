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

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

# Create the turtle for drawing the border
def Border():
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

def random_color_code():
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    return random.choice(colors)

# Initialize x
x = 0
r = 0
# Main loop to run 100 iterations at a time
while True:  # Change this number to the number of times you want to repeat the loop
    Border()
    r += 5 # how many times the turtle does random movement
    x = 1   # print the cmd message
    bob.hideturtle()
    for _ in range(r):
        bob.speed(0)
        move_randomly(bob, x_bound, y_bound)
        set_heatmap_color(bob)
        color1 = random_color_code()
        print(f"    {color1}Amount of times = \033[0m{x}\033[0m")  # Print with random colors
        x += 1  # Increment x within the loop


    # Reset the turtle's position and clear the screen after 100 iterations
    bob.penup()
    bob.goto(0, 0)
    bob.pendown()
    wn.resetscreen()  # Clear the screen and reset turtle to initial state

# Keeps the window open until it's closed manually
wn.mainloop()
