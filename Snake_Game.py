from turtle import Screen
import time
from Snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Douda Game Yamat Nokia')
screen.tracer(0)


screen.listen()
screen.onkey(snake.down,'s')
screen.onkey(snake.up,'z')
screen.onkey(snake.right,'d')
screen.onkey(snake.left,'q')

is_moving = True
scoreboard.scoreb(scoreboard.score)
while is_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    if snake.head.distance(food) < 15 :
        scoreboard.score += 1
        scoreboard.scoreb(scoreboard.score)
        food.refrech()
        snake.extend()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_moving = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_moving = False
            scoreboard.game_over()

screen.exitonclick()