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




#============================
# vars for fordward and right
forward_first = 100
right = 136
forward_second = 200
forward_third = 100
#============================


alex.speed(0)
alex.goto(0,0)
alex.hideturtle()
alex.fillcolor("red")
def fill_alex():
    alex.begin_fill()
    for runs in range(44):
        alex.forward(forward_first)
        alex.right(right)
        alex.forward(forward_second)
        if runs == 43:
            print("ran this")
            alex.forward(forward_third)
    alex.end_fill()

alex.penup()
fill_alex()

alex.penup()
alex.setheading(90)
alex.goto(0,0)
alex.forward(300)
alex.penup()

#============================
# vars for fordward and right
forward_first = 50
right = 136
forward_second = 100
forward_third = 50
#============================

fill_alex()

alex.penup()
alex.setheading(0)
alex.goto(0,0)
alex.forward(300)
alex.left(90)
alex.forward(100)
alex.penup()

#============================
# vars for fordward and right
forward_first = 25
right = 136
forward_second = 50
forward_third = 25
#============================

fill_alex()
















wn.exitonclick()