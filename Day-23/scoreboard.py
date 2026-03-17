from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.goto(-280,280)
        self.color("black")
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level :{self.level}",font=FONT)
