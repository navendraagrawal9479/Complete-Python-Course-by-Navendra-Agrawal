from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake_module import Snake

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_size()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()>280:
        scoreboard.game_over()
        is_game_on = False

    for segment in snake.snake:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 15:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()