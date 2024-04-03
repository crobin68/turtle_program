import turtle
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

#Function to do a powerup of turtle
def powerup():
    for powerup in range(2):
        bob.forward(20)
        bob.right(45)



#Function to change color of turtle
def color_change():
    bob.color(random_color())

# Function to move turtle forward
def move_forward():
    bob.forward(10)

# Function to move turtle backward
def move_backward():
    bob.backward(10)

# Function to turn turtle left
def turn_left():
    bob.left(10)

# Function to turn turtle right
def turn_right():
    bob.right(10)
    bob.color(random_color())

# Set up the screen
wn = turtle.Screen()
wn.setup(width=1000, height=800)
wn.bgcolor("black")

# Create the turtle
bob = turtle.Turtle()
bob.color("pink")
bob.pensize(2)
bob.speed(0)

# Set up event handlers for arrow keys
wn.listen()
wn.onkeypress(move_forward, "Up")
wn.onkeypress(move_backward, "Down")
wn.onkeypress(turn_left, "Left")
wn.onkeypress(turn_right, "Right")
wn.onkeypress(powerup, "a")
# Keeps the window open until it's clicked
wn.mainloop()
