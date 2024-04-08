import turtle
import random 



# Create a turtle screen
wn = turtle.Screen()
wn.setup(width=800, height=800)
wn.bgcolor("black")


alex = turtle.Turtle()
alex.pencolor("Pink")
alex.showturtle()
alex.write(f"hello", font=("Arial", 24, "normal"))


wn.exitonclick()




