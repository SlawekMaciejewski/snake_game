from turtle import Turtle, Screen
from food import Food
from snake import Snake
import time

if __name__ == '__main__':
    screen = Screen()
    screen.title("SNAKE GAME")
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.05)  # The screen delay is displayed after 0.05s and then refresh the screen.
        snake.move()

    screen.exitonclick()
