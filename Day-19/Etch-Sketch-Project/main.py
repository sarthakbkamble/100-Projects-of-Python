import turtle 
pointer = turtle.Turtle() 
my_screen = turtle.Screen() 

#functions for movments
def move_forward():
    pointer.forward(10)
def move_backward():
    pointer.backward(10)
def point_clockwise():
    pointer.right(5)
def point_counter_clockwise():
    pointer.left(5)

#function to clear the screen and reset the position
def reset():
    pointer.reset()

turtle.listen()
#key bindings
turtle.onkeypress(move_forward,"w")
turtle.onkeypress(move_backward,"s")
turtle.onkeypress(point_clockwise,"d")
turtle.onkeypress(point_counter_clockwise,"a")
turtle.onkeypress(reset,"c")


my_screen.exitonclick()