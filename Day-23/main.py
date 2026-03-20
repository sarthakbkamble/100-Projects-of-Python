# Importing Modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialization and basic screen setup
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.listen()
my_player = Player()
carmanager = CarManager()

# For player movement
screen.onkeypress(key="Up",fun=my_player.move)


game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # creates cars and moves them 
    carmanager.create_car()
    carmanager.move_cars()
    
    # Detecting collision with car
    for car in carmanager.all_cars:
        if car.distance(my_player)<20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting successful crossing 
    if my_player.is_at_finish_line():
        scoreboard.update_level()
        my_player.reset_position()
        carmanager.increase_speed()

screen.exitonclick()  
        


