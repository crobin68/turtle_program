import turtle
import random

# Function to move the turtle randomly
def move_randomly(turtle, x_bound, y_bound):
    angle = random.uniform(0, 360)  # Generate a random angle
    turtle.setheading(angle)  # Set the turtle's heading to the random angle
    turtle.forward(10)  # Move the turtle forward by a fixed amount

    # Check if turtle is out of bounds
    if abs(turtle.xcor()) > x_bound or abs(turtle.ycor()) > y_bound:
        turtle.penup()  # Pick up pen before (0,0)
        turtle.goto(0, 0)  # Reset turtle position to (0, 0)
        turtle.pendown()  # Pen down when at (0,0)

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")

# Create the turtle
bob = turtle.Turtle()
bob.color("white")  # Set turtle color to white
bob.speed(1)  # Set turtle speed to fastest

# Define the boundary box
x_bound = 250
y_bound = 250

# Set the initial position of the turtle
bob.penup()
bob.goto(0, 0)
bob.pendown()

# Write "Happy Birthday"
bob.penup()
bob.goto(-100, 0)
bob.pendown()
bob.write("Happy Birthday", font=("Arial", 24, "normal"))
bob.penup()
bob.right(90)
bob.forward(50)
bob.pendown()
bob.write("Calvin", font=("Arial", 24, "normal"))

# Hide the turtle
bob.showturtle()

# Keep the window open until it's closed manually
wn.mainloop()
