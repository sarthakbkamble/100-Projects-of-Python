import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.listen()
my_player = Player()
screen.onkeypress(key="Up",fun=my_player.move)


game_is_on = True
while game_is_on:
    if my_player.ycor()>280:
        my_player.reset_position()
        scoreboard.update_level()


    time.sleep(0.1)
    screen.update()

screen.exitonclick