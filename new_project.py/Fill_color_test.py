import turtle


wn = turtle.Screen()
wn.bgcolor("black")


# Creation of turtles
alex = turtle.Turtle()
bob = turtle.Turtle()

# set color for turtles 
alex.pencolor("light green")
bob.pencolor("white")

bob.hideturtle()

alex.speed(0)
alex.goto(0,0)
alex.showturtle()
alex.fillcolor("red")
def fill_alex():
    alex.begin_fill()
    for runs in range(44):
        alex.forward(100)
        alex.right(136)
        alex.forward(200)
        if runs == 43:
            print("ran this")
            alex.forward(100)
    alex.end_fill()


fill_alex()

alex.penup()
alex.setheading(90)
alex.goto(0,0)
alex.forward(300)
alex.pendown()

fill_alex()



















wn.exitonclick()