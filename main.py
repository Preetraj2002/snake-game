from turtle import Screen

from scoreboard import Scoreboard

from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snakofizz")
screen.tracer(0)
snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




is_game_on = True

def off():
    global is_game_on
    is_game_on = False
    exit(1)

screen.onkey(off,"q")

while is_game_on :
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Detecting collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        screen.update()
        scoreboard.increase_score()

    #Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    #Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()














screen.exitonclick()
