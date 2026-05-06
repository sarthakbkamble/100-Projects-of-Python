# Importing Modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialization and basic screen setup
# Instantiate the screen, disable automatic tracer animations, and set up dimensions
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.listen()
my_player = Player()
carmanager = CarManager()

# For player movement
# Bind the "Up" arrow key to trigger the turtle player's forward movement
screen.onkeypress(key="Up",fun=my_player.move)


game_is_on = True

# Main game loop
while game_is_on:
    # Set the game step delay rate and manually update the visual screen elements
    time.sleep(0.1)
    screen.update()

    # Create cars randomly and advance them horizontally across the canvas
    carmanager.create_car()
    carmanager.move_cars()
    
    # Detecting collision with car
    # Check if the player has collided with any of the moving obstacles in the fleet
    for car in carmanager.all_cars:
        if car.distance(my_player)<20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting successful crossing 
    # Check if the player successfully reached the top edge of the screen
    if my_player.is_at_finish_line():
        scoreboard.update_level()
        my_player.reset_position()
        carmanager.increase_speed()

# Keep the window open until the user clicks to exit
screen.exitonclick()