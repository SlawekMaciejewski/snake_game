from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
        Snake class. It's creating three segments of snake in the home position.
        :self.segments: list of the snake segments
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        """
        It's creating three segments of snake in the home position.
        :return: None
        """
        # creating 3 segments snake
        x = 0
        for segment in range(3):
            self.add_segment((x, 0))
            x += -20

    def add_segment(self, position):
        """
        Add a new segment to the snake
        :return: None
        """
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """
        Clear all of the segments from the snake and create new snake in the starting position.
        :return: None
        """
        # Move the snake segments off the screen.
        for segment in self.segments:
            segment.goto(1000, 1000)
        # Rebuild a new snake.
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        # self.tail = self.segments[-1]

    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):
        """
        The snake always moves forward 20. The last segment becomes the second to last segment, and etc.
        :return: None
        """
        # The last segment takes the second to last segment, the second to last segment takes the next segment etc.
        # The first segment always moves forward 20.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # time.sleep(1)
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
