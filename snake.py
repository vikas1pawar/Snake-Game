from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.move_speed = 0.15

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segments(self.snake_segments[-1].position())

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()

    def increase_speed(self):
        self.move_speed *= 0.9

    def reset_speed(self):
        self.move_speed = 0.15


    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

