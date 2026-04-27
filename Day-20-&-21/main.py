from turtle import Screen
import time, snake, scoreboard
from food import Food

# 1. Screen Setup
# Initialize the game canvas dimensions, background color, title, and turn off automatic tracer updates
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# 2. Game Entities Initialization
# Instantiate the snake controller, food generator, and scoreboard tracker
snake = snake.Snake()
food = Food()
my_score = scoreboard.Scoreboard()

# 3. Input Handling
# Set up the event listeners to map keyboard arrow keys to snake direction controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 4. Main Game Loop
game_is_on = True
while game_is_on:
    # Refresh the screen manually and pause briefly to control the animation frames rate
    screen.update()
    time.sleep(0.1)
    snake.move()
    my_score

    # Check for collision with food (reposition food, grow the snake, and increment the score)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        my_score.increase_score()

    # Check for collision with the outer boundary walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        my_score.game_over()
        game_is_on = False

    # Check for collision with any part of the snake's own tail segments (slice excludes the head)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            game_is_on = False
            my_score.game_over()

# 5. Screen Exit Listener
screen.exitonclick()