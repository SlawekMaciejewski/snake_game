from turtle import Turtle, Screen
from snake import Snake
import time

if __name__ == '__main__':
    screen = Screen()
    screen.title("SNAKE GAME")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.05)
        snake.move()

    screen.exitonclick()
