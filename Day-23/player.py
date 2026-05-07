from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        # Inherit from Turtle, configure style as a black turtle, and disable drawing paths
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)
    
    def move(self):
        """Moves the player forward."""
        # Advance the turtle player vertically by the set move distance
        self.forward(10)

    def reset_position(self):
        """Player goes to starting position."""
        # Teleport the turtle player back to the southern starting line coordinate
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        """Checks whether the player is at finish line or not."""
        # Compare the turtle's current vertical y-position against the target northern finish line threshold
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False