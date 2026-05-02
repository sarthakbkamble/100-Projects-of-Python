from turtle import Turtle, Screen
import paddle,time
from ball import Ball
import scoreboard 

# 1. Screen Setup
# Initialize the game canvas dimensions, black background, title, and turn off automatic tracer updates
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(height=600,width=800)
my_screen.title("Pong")

# Turn off the tracer animation to manually update frames with .update()
my_screen.tracer(0)
score_display = scoreboard.Scoreboard()
my_ball = Ball()

# 2. Paddles Initialization
# Instantiate the right and left paddles at their starting coordinate offsets
r_paddle = paddle.Paddle((350,0))
l_paddle = paddle.Paddle((-350,0))

# 3. Key Bindings
# Bind specific keyboard keys to move the left (W/S) and right (Arrow Up/Down) paddles
my_screen.listen()
my_screen.onkeypress(key="Up",fun=r_paddle.move_up) 
my_screen.onkeypress(key="Down",fun=r_paddle.move_down) 
my_screen.onkeypress(key="w",fun=l_paddle.move_up) 
my_screen.onkeypress(key="s",fun=l_paddle.move_down) 

# 4. Main Game Loop
game_on = True
while game_on:
    # Set the game speed dynamically based on the ball's moving speed multiplier
    time.sleep(my_ball.moving_speed)
    
    my_ball.move()

    # Detect collision with top and bottom walls
    if my_ball.ycor()>280 or my_ball.ycor()<-280:
        my_ball.bounce_y()
        
    # Detect collision with both right and left paddles
    if my_ball.distance(r_paddle)<50 and my_ball.xcor()>320 or my_ball.distance(l_paddle)<50 and my_ball.xcor()<-320:
        my_ball.bounce_x()
        
    # Handle right-side out-of-bounds (Left Player scores a point)
    if my_ball.xcor()>380 :
        my_ball.reset_position()
        score_display .l_point()
        
    # Handle left-side out-of-bounds (Right Player scores a point)
    if my_ball.xcor()<-380:
        my_ball.reset_position()
        score_display.r_point()
        
    # Manually update the canvas state to prevent screen stuttering
    my_screen.update()


# 5. Screen Exit Listener
my_screen.exitonclick()