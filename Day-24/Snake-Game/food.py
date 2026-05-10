from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        # Inherit from the Turtle class and configure its visual appearance
        super().__init__()
        self.shape("circle")
        self.penup()
        # Scale down the default turtle size (20x20 pixels) to a 10x10 pixel circle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Generate random coordinates within the game boundaries and relocate the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)