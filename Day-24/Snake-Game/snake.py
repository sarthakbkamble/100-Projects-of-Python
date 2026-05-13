from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Initialize the snake body segment container, generate the body blocks, and track the head reference
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Place the initial segments at the coordinate offsets specified in STARTING_POSITIONS
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Instantiate a white square segment, lift its pen, place it, and append it to our tracking list
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def reset(self):
        # Send existing segments off-screen to prevent dead body parts from cluttering the canvas
        for seg in self.segments:
            seg.goto(1000,1000)
        # Empty the tracking list, construct a new starting snake, and re-cache the new head
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]

    def extend(self):
        # Grow the snake by appending a new segment at the exact position of the current tail end
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Shift each segment forward to occupy the coordinate position of the segment directly in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Propagate the leading step forward in the current heading direction
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Point the head northwards, preventing the snake from instantly reversing into itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Point the head southwards, preventing the snake from instantly reversing into itself
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Point the head westwards, preventing the snake from instantly reversing into itself
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Point the head eastwards, preventing the snake from instantly reversing into itself
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)