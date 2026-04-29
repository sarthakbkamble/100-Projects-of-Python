from turtle import Turtle

# Define initial screen coordinates and standard angular headings for direction constraints
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        # Initialize the container for body segments, build the starting snake, and cache the head segment reference
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        # Generate the initial blocks at the starting positions defined in the list
        for position in STARTING_POSITIONS:
            self.add_segement(position)
            
    def add_segement(self, position):
        # Create a new square green segment, lift its pen, and position it on the screen grid
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Append a new segment at the current coordinates of the last segment of the tail
        self.add_segement(self.segments[-1].position())


    def move(self):
        # Propagate movement from the tail forwards by shifting each segment to the position of the one ahead of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Advance the head segment forward to drive the direction of movement
        self.head.forward(20)

    def up(self):
        # Change heading upwards, ensuring the snake cannot turn directly back into its own neck
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change heading downwards, ensuring the snake cannot turn directly back into its own neck
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Change heading to the right, ensuring the snake cannot turn directly back into its own neck
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        # Change heading to the left, ensuring the snake cannot turn directly back into its own neck
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)