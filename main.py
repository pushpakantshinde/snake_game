from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)


is_game_on = True
snake = Snake()
food_item = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food_item) < 20:
        food_item.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        snake.clear_snake()             # Clear the snake
        score.game_reset()
        snake.snake_reset()


    # Detect collision with tail
    #--------------------------------------------------------
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 20:
    #         score.game_over()
    #--------------------------------------------------------

    # OR


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # distance 10 is decided based on trial & error
            snake.clear_snake()           # Clear the snake
            score.game_reset()
            snake.snake_reset()


my_screen.exitonclick()
