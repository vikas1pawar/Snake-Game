from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    if snake.snake_segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        snake.increase_speed()
        scoreboard.increase_score()

    if snake.snake_segments[0].xcor() > 290 or snake.snake_segments[0].xcor() < -290 or snake.snake_segments[0].ycor() > 290 or snake.snake_segments[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()
        snake.reset_speed()

    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            snake.reset_speed()


screen.exitonclick()
