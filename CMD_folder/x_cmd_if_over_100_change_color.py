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
bob.speed(0)  # Set turtle speed to fastest
#border_pen = turtle.Turtle()   ****Already defined in line 36 and 37****
#border_pen.color("white")      ****Already defined in line 36 and 37****





# Define the boundary box
x_bound = 250
y_bound = 250

# Draw the boundary box
border_pen = turtle.Turtle()
border_pen.color("white")
border_pen.penup()
border_pen.goto(-x_bound, y_bound)
border_pen.pendown()
for _ in range(4):
    border_pen.forward(2 * x_bound)
    border_pen.right(90)
border_pen.hideturtle()

# Set the initial position of the turtle
bob.penup()
bob.goto(0, 0)
bob.pendown()


                        #### THINGS TO CALL ####


# make bob random colors
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

#making the background a rainbow
def background_color_change():
    wn.bgcolor(random_color())

# make the cmd colors
def random_color_code():
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    return random.choice(colors)



# Main loop for random movement within the boundary box
r = 0 
x = 0
loop_count = 0
p = 0
while True:
    p += 1
    r += 5
    x = 1
    bob.hideturtle()
    bob.pensize(p)
    
    for _ in range(r):
        
        
        if x >= 1000:
            bob.color("Red")
        
        
        move_randomly(bob, x_bound, y_bound)
        

        color1 = random_color_code()
        print(f"    {color1}Amount of times = \033[0m{x}\033[0m")  # Print with random colors
        x += 1  # Increment x within the loop

    loop_count += 1

    print(f"\033[91m you have compleated {loop_count}")

    bob.penup()
    bob.goto(0, 0)
    bob.pendown()
    bob.clear()

    

# Keep the window open until it's closed manually
wn.mainloop()
