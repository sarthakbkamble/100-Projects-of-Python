from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        # Inherit from Turtle and configure drawing settings for displaying level status
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        # Position the level text at the top-left corner of the window
        self.goto(-280,245)
        self.color("black")
        self.update_level()

    def update_level(self):
        """Updates the game level"""
        # Clear the old level text, increment the stage counter, and write the new level
        self.clear()
        self.level+=1
        self.write(arg=f"Level :{self.level}",font=FONT)

    def game_over(self):
        """Shows game over message"""
        # Relocate to the center of the screen and render the final game over banner
        self.goto(0,0)
        self.write(arg="GAME OVER!",align="center",font=FONT)