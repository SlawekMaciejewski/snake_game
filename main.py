from turtle import Turtle, Screen


if __name__ == '__main__':
    screen = Screen()
    screen.title("SNAKE GAME")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

    x = 0
    for segment in range(3):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(x=x, y=0)
        x += -20

    screen.exitonclick()