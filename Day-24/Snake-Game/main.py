from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 1. Screen Setup
# Set up the dimensions, background, title, and turn off automatic tracing for manual animation control
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# 2. Game Entities Initialization
# Instantiate the snake, the food target, and the persistent high-score scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Input Handling
# Set up the keyboard listeners to bind directional arrow keys to the snake's movement controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 4. Main Game Loop
game_is_on = True
while game_is_on:
    # Refresh the display manually and delay the frame briefly to control movement speed
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    # When the head gets close to the food, reposition the food, lengthen the snake, and increase score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    # If the snake hits any outer boundaries, trigger the reset functions instead of stopping the loop
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    # Check the distance of the head to every segment in the body, ignoring the head itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            

# 5. Screen Exit Listener
screen.exitonclick()