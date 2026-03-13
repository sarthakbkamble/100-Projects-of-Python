from turtle import Turtle, Screen
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(height=600,width=800)
my_screen.title("Pong")

paddle = Turtle()
paddle.teleport(x=350,y=)
paddle.penup()
paddle.shape("square")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.color("white")


my_screen.listen()
def move_up():
    new_y = paddle.ycor()+10
    paddle.goto(paddle.xcor(),new_y)

def move_down():
    new_y = paddle.ycor()-10
    paddle.goto(paddle.xcor(),new_y)
my_screen.onkeypress(key="Up",fun=move_up) 
my_screen.onkeypress(key="Down",fun=move_down) 





my_screen.exitonclick()