from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        # Inherit from Turtle to handle rendering and track current game session score
        super().__init__()
        self.score = 0
        # Load the saved high score from the external tracking file on startup
        with open("/new/100-Projects-of-Python\Day-24\Snake-game\data.txt",mode="r") as data:
            self.high_score = int(data.read())
        # Set up text styling properties and position the board at the top of the window
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Erase the previous score display and draw the updated scores status
        self.clear()
        self.write(f"Score: {self.score} Hight Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # If the player beat their previous record, overwrite the high score file with the new record
        if self.score>self.high_score:
            self.high_score=self.score
            with open("/new/100-Projects-of-Python\Day-24\Snake-game\data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        # Reset current score to zero for the next run and refresh the scoreboard text
        self.score = 0

    def increase_score(self):
        # Increment the score counter by one and refresh the visual rendering
        self.score += 1
        self.update_scoreboard()