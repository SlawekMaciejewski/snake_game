from turtle import Screen
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

        # Detect collision with food
        # The snake has 20x20 pixels, the food has 10x10 pixels. A Half snake is 10 and a half food is 5.
        # snake.head is the first segment of the snake
        if snake.head.distance(food) <= 15:
            food.refresh()
            new_segment = Snake()
            # x = snake.tail.xcor()
            # y = snake.tail.ycor()
            # new_segment.head.goto(x-20, y-20)
            snake.segments.append(new_segment.head)
            print(len(snake.segments))

    screen.exitonclick()
