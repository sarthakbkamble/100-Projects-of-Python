from turtle import Turtle,Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager():
    def __init__(self):
        # Initialize an empty list to track active car objects and set the starting speed
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        """Creates car"""
        # Introduce a 1-in-6 probability factor to space out car generation cycles
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car= Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # Place the newly generated car at a randomized height along the right edge of the screen
            random_y=random.randint(-230,230)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """used for car moving"""
        # Move every car westward across the screen based on the current level's speed multiplier
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """increases car speed"""
        # Add the fixed movement increment value to speed up gameplay for the next level
        self.car_speed+=MOVE_INCREMENT