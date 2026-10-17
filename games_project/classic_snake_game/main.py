import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=t.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

play=True
while play:
    is_game_on=True

    while is_game_on:
        screen.update()
        time.sleep(0.1) 
        snake.move() 

        # detect collision
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280 :
            scoreboard.reset()
            snake.reset()
            is_game_on =False
            

        # detect collision with tail.
        for segment in snake.segments[1:]:
            
            if snake.segments[0].distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                is_game_on = False

    response = screen.textinput(title=f"Score:{scoreboard.score} Play Again?", prompt="Type 'yes' or 'no':")
    screen.listen()
    if response and response.lower() == "yes":
        play = True
    else:
        play = False

screen.exitonclick()
