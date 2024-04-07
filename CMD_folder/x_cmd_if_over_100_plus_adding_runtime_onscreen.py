import turtle
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.setup(width=700, height=700)
wn.bgcolor("black")


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


                        #### THINGS TO CALL ####


# make bob random colors
def random_color():
    return tuple(random.random() for _ in range(3))

#making the background a rainbow
def background_color_change():
    wn.bgcolor(random_color())
for BGcolor in range(3):
    background_color_change()
# make the cmd colors
def random_color_code():
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    return random.choice(colors)





# Create the turtle
bob = turtle.Turtle()
bob.color("white")                          # Set turtle color to white
bob.hideturtle()                            # hide turtle
loop_count_text = turtle.Turtle()           # turtle is printing {loop_count} in "Dark Red"
loop_count_perm_text = turtle.Turtle()      # turtle is printing "Run times" in yellow
progress_bar = turtle.Turtle()
box_for_progress = turtle.Turtle()

#set speed for turtles
loop_count_text.speed(0)
loop_count_perm_text.speed(0)
bob.speed(0)



# Define the boundary box
x_bound = 250
y_bound = 250
# Draw the boundary box
def border_box():
    border_pen = turtle.Turtle()
    border_pen.color("white")
    border_pen.penup()
    border_pen.goto(-x_bound, y_bound)
    border_pen.pendown()
    border_pen.speed(0)
    for _ in range(4):
        border_pen.forward(2 * x_bound)
        border_pen.right(90)
    border_pen.hideturtle()

# make progress bar box
def move_progress_bar():
    box_for_progress.speed(0)
    box_for_progress.hideturtle()
    box_for_progress.color("white")
    box_for_progress.penup()
    box_for_progress.right(180)
    box_for_progress.forward(250)
    box_for_progress.right(90)
    box_for_progress.forward(255) # height of box for progress bar
    box_for_progress.pendown()
    for box in range(2):
        box_for_progress.forward(20)
        box_for_progress.right(90)
        box_for_progress.forward(500)
        box_for_progress.right(90)


#set pos for {loop_count} turtle 
def pos_for_loop_count():
    loop_count_text.color("Dark Red")
    loop_count_text.hideturtle()
    loop_count_text.right(180)
    loop_count_text.forward(250)
    loop_count_text.right(90)
    loop_count_text.forward(270) # the height of the text
    loop_count_text.right(90)
    loop_count_text.forward(250)
    loop_count_text.clear() #clear lines 

# Set position for progress bar
def set_pos_progress_bar_text():
    loop_count_perm_text.color("yellow")
    loop_count_perm_text.hideturtle()
    loop_count_perm_text.right(180)
    loop_count_perm_text.forward(250)
    loop_count_perm_text.right(90)
    loop_count_perm_text.forward(270)  # the height of the text
    loop_count_perm_text.clear()  # clear lines before printing text
    loop_count_perm_text.write("Run times = ", font=("Arial", 24, "normal"))
    loop_count_perm_text.right(90)




# Progress bar for loop_count
def set_pos_progress_bar_slider():
    progress_bar.shape("square")
    progress_bar.penup()
    progress_bar.color("light green")
    progress_bar.hideturtle()
    progress_bar.right(180)
    progress_bar.forward(240)
    progress_bar.right(90)
    progress_bar.forward(265)  # height of the progress bar
    progress_bar.right(90)
    progress_bar.pensize(10)
    progress_bar.pendown()




# ==-==-==-==-==-==-==-==-==-==-==-==-==
#           Call everything 
border_box()                    #   this makes the border
set_pos_progress_bar_slider()   #   this set the pos of the progress slider
set_pos_progress_bar_text()     #   this set the perm text "Run times="
pos_for_loop_count()            #   this set the pos for loop count 
move_progress_bar()             #   this  set the pos of green progress bar

# ==-==-==-==-==-==-==-==-==-==-==-==-==





# variables that need to be set before the {for loop}
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
r = 0 
x = 0
loop_count = 1
for MainCode in range(10):
    wn.bgcolor(random_color())
    r += 5
    x = 1   # how many times the code runs
    bob.hideturtle()
    loop_count_text.write(f"{loop_count}", font=("Arial", 24, "normal"))

    for _ in range(r):
        
        if x >= 1000:
            bob.color("Red")
        
        move_randomly(bob, x_bound, y_bound)

        color1 = random_color_code()
        print(f"    {color1}Amount of times = \033[0m{x}\033[0m")  # Print with random colors
        x += 1  # Increment x within the loop

    loop_count += 1
    progress_bar.forward(48)
    print(f"\033[91m you have compleated {loop_count - 1}")

    bob.penup()
    bob.goto(0, 0)
    bob.pendown()
    bob.clear()
    loop_count_text.clear()
 
#loop_count_text.showturtle()
loop_count_text.speed(0)
loop_count_text.left(145)
loop_count_text.forward(18)
loop_count_text.left(45)
loop_count_text.forward(10)
loop_count_text.color("Green")
loop_count_text.write(f"Random movement Compleated", font=("Arial", 15, "normal"))
# Keep the window open until it's closed manually
wn.mainloop()
