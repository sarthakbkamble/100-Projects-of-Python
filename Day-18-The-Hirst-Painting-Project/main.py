import colorgram
import turtle
import random

# 1. Setup the Color Mode (Fixes the "bad color sequence" error)
turtle.colormode(255)

# 2. Extract colors from the image (Using a raw string for the path)
# Note: Ensure image.jpg is in this folder!
# image_path = r"C:\new\100-Projects-of-Python\Day-18-The-Hirst-Painting-Project\image.jpg"
# colors = colorgram.extract(image_path, 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

rgb_colors = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (41, 46, 65)]

# 3. Initialize the Turtle (Fixes the AttributeError/Type Alias issues)
tiny = turtle.Turtle()
tiny.speed("fastest") # Makes it draw much quicker
tiny.penup()          # Stops the turtle from drawing lines between dots
tiny.hideturtle()     # Hides the turtle icon

# 4. Set Starting Position (Bottom Left)
tiny.setheading(225)
tiny.forward(300)
tiny.setheading(0)

# 5. Draw the 10x10 Grid
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # Draw a dot with a random color from our list
    tiny.dot(20, random.choice(rgb_colors))
    
    # Move forward to the next dot position
    tiny.forward(50)

    # After every 10 dots, move up to the next row
    if dot_count % 10 == 0:
        tiny.setheading(90)
        tiny.forward(50)
        tiny.setheading(180)
        tiny.forward(500)
        tiny.setheading(0)

# 6. Keep the window open
screen = turtle.Screen()
screen.exitonclick()