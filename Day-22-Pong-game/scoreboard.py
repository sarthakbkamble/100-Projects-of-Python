from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # Inherit from Turtle and configure general styling parameters for score-rendering
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # Track independent game scores for both the left and right players
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

 


    def update_scoreboard(self):
        # Clear previous frame drawings to avoid overlaps and render the fresh scores
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 30, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 30, "bold"))
        
        # Draw a custom dashed line straight down the middle of the screen
        self.setheading(270)
        self.goto(0,300)
        self.pensize(5)
        while self.ycor()!=-300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def l_point(self):
        # Increment the score for the left player and refresh the visual board
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increment the score for the right player and refresh the visual board
        self.r_score += 1
        self.update_scoreboard()