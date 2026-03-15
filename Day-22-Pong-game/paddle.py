from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coord):
        super().__init__()
        self.goto(x=coord[0],y=coord[1])
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        

    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
    
