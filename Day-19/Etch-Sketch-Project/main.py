import turtle 
pointer = turtle.Turtle() 
my_screen = turtle.Screen() 

# Functions for turtle movements and rotation mechanics
def move_forward():
    # Move the turtle pen forward by 10 units
    pointer.forward(10)

def move_backward():
    # Move the turtle pen backward by 10 units
    pointer.backward(10)

def point_clockwise():
    # Rotate the turtle's heading 5 degrees to the right
    pointer.right(5)

def point_counter_clockwise():
    # Rotate the turtle's heading 5 degrees to the left
    pointer.left(5)

# Function to clear the screen and reset the position
def reset():
    # Clear the canvas drawings and return the turtle to home center position
    pointer.reset()

# Initialize key event listening and map the movement functions to the WASD/C keys
turtle.listen()
# Key bindings configuration
turtle.onkeypress(move_forward,"w")
turtle.onkeypress(move_backward,"s")
turtle.onkeypress(point_clockwise,"d")
turtle.onkeypress(point_counter_clockwise,"a")
turtle.onkeypress(reset,"c")

# Set up screen close interaction
my_screen.exitonclick()