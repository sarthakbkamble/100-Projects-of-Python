from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}",align="center",font= ("Arial", 14, "bold") )
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER.",align="center",font= ("Arial", 25, "bold") )

    def increase_score(self):
        self.clear()    
        self.score+=1
        self.write(arg=f"Score: {self.score}",align="center",font= ("Arial", 14, "bold") )
       

