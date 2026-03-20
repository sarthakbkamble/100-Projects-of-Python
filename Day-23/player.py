from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)
    
    def move(self):
        """Moves the player forward."""
        self.forward(10)

    def reset_position(self):
        """Player goes to starting position."""
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        """Checks whether the player is at finish line or not."""
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
     

