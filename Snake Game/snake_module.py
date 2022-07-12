from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        self.snake.append(new_segment)

    def increase_size(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_position = self.snake[segment_number - 1].pos()
            self.snake[segment_number].setpos(new_position)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)