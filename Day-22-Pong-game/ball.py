from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        # Inherit from Turtle, set appearance as a white circle, and disable drawing lines
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        # Define step distances for horizontal/vertical movement and the game loop delay timer
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1
    
    def move(self):
        # Calculate and navigate to the next position based on step increments
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        # Reverse the vertical direction (used for top and bottom wall collisions)
        self.y_move *= -1

    def bounce_x(self):
        # Reverse horizontal direction (paddle collisions) and decrease the loop delay to speed up gameplay
        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        # Send the ball back to the center of the court, reset the movement delay, and change serve direction
        self.goto(0, 0)
        self.moving_speed = 0.1
        self.bounce_x()