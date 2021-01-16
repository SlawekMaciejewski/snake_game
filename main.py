from turtle import Turtle, Screen
import time

if __name__ == '__main__':
    screen = Screen()
    screen.title("SNAKE GAME")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    segments = []
    x = 0
    for segment in range(3):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(x=x, y=0)
        x += -20
        segments.append(new_segment)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.05)
        # The last segment takes the second to last segment, the second to last segment takes the next segment etc.
        # The first segment always moves forward 20.
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            # time.sleep(1)
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)

    screen.exitonclick()
