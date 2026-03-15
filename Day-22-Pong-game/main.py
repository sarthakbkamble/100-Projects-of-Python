from turtle import Turtle, Screen
import paddle,time
from ball import Ball
import scoreboard 

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(height=600,width=800)
my_screen.title("Pong")

my_screen.tracer(0)
score_display = scoreboard.Scoreboard()
my_ball = Ball()


r_paddle = paddle.Paddle((350,0))
l_paddle = paddle.Paddle((-350,0))

my_screen.listen()
my_screen.onkeypress(key="Up",fun=r_paddle.move_up) 
my_screen.onkeypress(key="Down",fun=r_paddle.move_down) 
my_screen.onkeypress(key="w",fun=l_paddle.move_up) 
my_screen.onkeypress(key="s",fun=l_paddle.move_down) 

game_on = True
while game_on:
    time.sleep(0.1)
    
    my_ball.move()

    if my_ball.ycor()>280 or my_ball.ycor()<-280:
        my_ball.bounce_y()
    if my_ball.distance(r_paddle)<50 and my_ball.xcor()>320 or my_ball.distance(l_paddle)<50 and my_ball.xcor()<-320:
        my_ball.bounce_x()
    if my_ball.xcor()>380 :
        my_ball.reset_position()
        score_display .l_point()
    if my_ball.xcor()<-380:
        my_ball.reset_position()
        score_display.r_point()
    my_screen.update()


my_screen.exitonclick()