import turtle
import time
import random




# Create a turtle screen
wn = turtle.Screen()
wn.setup(width=800, height=800)
wn.bgcolor("black")

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


x = -5

blue = turtle.Turtle()
blue.pencolor("blue")
blue.pensize(10)
blue.pendown()


blue.speed(0)

x = -2
org_pen_size = 30
blue.pensize(org_pen_size)



#def call_one():
#    for run_one in range(org_pen_size):
#
#        blue.pencolor(random_color())
#        blue.pensize(blue.pensize() + x)    
#        for __ in range(8):
#            blue.forward(100)
#            blue.right(45)
#            if blue.pensize() <= 10:
#                call_one()
#call_one()


loading = turtle.Turtle()
loading.pencolor("blue")
loading.pensize(10)
loading.pendown()

loading.hideturtle()
loading.speed(0)

def one():
    for onee in range(8):
        loading.pensize(50)
        loading.pencolor("red")
        for loading_one in range(1):
            loading.forward(100)
        loading.right(45)

def two():
    for twoo in range(8):
        loading.pencolor("green")
        loading.pensize(100)
        for loading_two in range(1):
            loading.forward(100)
        loading.right(45)



def call_two():
    for run_one in range(20):
        one()
        two()
call_two()

turtle.done()

# Keep the window open
wn.exitonclick()