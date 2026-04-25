from turtle import Turtle, Screen
import random

# Initialize game state and setup screen proportions 
race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Set up the starting vertical track positions for each racer
y_positions = [-100, -60, -20, 20, 60, 100]

# Instantiate 6 distinct turtle objects with different colors and line them up at the starting line
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # Using the list to ensure they are spaced evenly
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Begin the race sequence once the user places a bet
if user_bet:
    race_is_on = True

# Execute the race simulation: move turtles forward randomly and monitor for a finish line crossing
while race_is_on:
    for turtle in all_turtles:
        # Check if the turtle has reached the finish line (250 - half turtle width)
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break # Exit the for loop once we have a winner

        # Advance each turtle by a randomized step distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the execution window when clicked
screen.exitonclick()