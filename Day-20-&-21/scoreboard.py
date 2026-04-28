from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # Inherit from Turtle and configure the drawing options for the text layer
        super().__init__()
        self.score = 0
        self.pencolor("white")
        
        # Hide the drawing icon, move to the top of the canvas, and render the starting score
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}",align="center",font= ("Arial", 14, "bold") )
        
    def game_over(self):
        # Relocate to the center of the screen and overlay the final game over notification
        self.goto(0,0)
        self.write(arg="GAME OVER.",align="center",font= ("Arial", 25, "bold") )

    def increase_score(self):
        # Clear the old score text, increment the tracker, and render the updated score status
        self.clear()    
        self.score+=1
        self.write(arg=f"Score: {self.score}",align="center",font= ("Arial", 14, "bold") )