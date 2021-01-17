from turtle import Turtle


class Snake():
    def __init__(self):
        """
        Snake class. It's creating three segments of snake in the home position.
        :self.segments: list of the snake segments
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        It's creating three segments of snake in the home position.
        :return: None
        """
        x = 0
        # creating 3 segments snake
        for segment in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=x, y=0)
            x += -20
            self.segments.append(new_segment)

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
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
