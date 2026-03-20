from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-280,245)
        self.color("black")
        self.update_level()

    def update_level(self):
        """Updates the game level"""
        self.clear()
        self.level+=1
        self.write(arg=f"Level :{self.level}",font=FONT)

    def game_over(self):
        """Shows game over message"""
        self.goto(0,0)
        self.write(arg="GAME OVER!",align="center",font=FONT)
