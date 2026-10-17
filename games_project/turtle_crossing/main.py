import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("road.gif")
screen.tracer(0)


tim=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(tim.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(tim) <20 :
            game_is_on = False
            scoreboard.game_over()

    if tim.ycor() > 300 :
        tim.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()
