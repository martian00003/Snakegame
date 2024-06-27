from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


N = 600
D = 10
speed = 3
sleep_time = 0.000001

up = "Up"
down = "Down"
left = "Left"
right = "Right"

black = "black"
sqr = "square"


screen = Screen()
screen.setup(width = N+100, height = N+100)
screen.bgcolor(black)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up ,up)
screen.onkey(snake.down ,down)
screen.onkey(snake.left ,left)
screen.onkey(snake.right ,right)


runn = True

while runn:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        score.increase()
        snake.extend()
        snake.incr_speed()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        runn = False
        score.gameover()

    for i in snake.segment[1:]:
        if snake.head.distance(i) < 3:
            runn = False
            score.gameover()


screen.exitonclick()
