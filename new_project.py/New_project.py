import turtle 
import time

wn = turtle.Screen()
wn.bgcolor("black")

border_pen = turtle.Turtle()
# Define the boundary box
x_bound = 350
y_bound = 350
# Draw the boundary box
def border_box():
    border_pen.color("white")
    border_pen.penup()
    border_pen.goto(-x_bound, y_bound)
    border_pen.pendown()
    border_pen.speed(0)
    for _ in range(4):
        border_pen.forward(2 * x_bound)
        border_pen.right(90)
    border_pen.hideturtle()

border_box()
border_pen.showturtle()

# Make turtle random colors
def color():
    r = 0
    g = 0
    b = 255
    return (r, g, b)

alex = turtle.Turtle()
alex.pencolor("white")

alex.pendown()
alex.forward(350)

blue = turtle.Turtle()
blue.pencolor("blue")  # Unpack the tuple returned by color() function

blue.pendown()
blue.right(90)
blue.forward(20)
blue.left(90)
blue.forward(150)
blue.left(90)
blue.forward(300)
time.sleep(2)

# Define a function to check if turtle is over a certain color
def check_color(wn, alex):
    # Get the color of the screen at the turtle's position
    color = wn.getpixel((round(alex.xcor()), round(alex.ycor())))

    # Check if the color matches the color we are interested in
    if color == ("blue"):  # Blue color
        print("Turtle is over blue color!")
    elif color == ("red"):  # Red color
        print("Turtle is over red color!")

# Move the turtle to a position where you want to check the color
for _ in range(100):
    alex.backward(1)
    check_color()


alex.penup()
alex.goto(0, 0)
alex.pendown()

# Call the check_color function
check_color()

wn.exitonclick()

