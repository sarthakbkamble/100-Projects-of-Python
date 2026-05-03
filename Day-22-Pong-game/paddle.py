from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coord):
        # Inherit from Turtle and place the paddle at its starting coordinates
        super().__init__()
        self.goto(x=coord[0], y=coord[1])
        self.penup()
        # Change the turtle shape to a square and stretch its proportions to look like a paddle
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        

    def move_up(self):
        # Increase the y-coordinate by 20 units to shift the paddle upward
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        # Decrease the y-coordinate by 20 units to shift the paddle downward
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)