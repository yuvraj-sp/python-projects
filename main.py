import turtle as t
from paddle import Paddle   
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Arcade Game")
screen.tracer(0)

scoreboard = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# ✅ Track which keys are pressed
keys_pressed = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}

def key_down(key):
    keys_pressed[key] = True

def key_up(key):
    keys_pressed[key] = False

screen.listen()

screen.onkeypress(lambda: key_down("Up"), "Up")
screen.onkeyrelease(lambda: key_up("Up"), "Up")
screen.onkeypress(lambda: key_down("Down"), "Down")
screen.onkeyrelease(lambda: key_up("Down"), "Down")
screen.onkeypress(lambda: key_down("w"), "w")
screen.onkeyrelease(lambda: key_up("w"), "w")
screen.onkeypress(lambda: key_down("s"), "s")
screen.onkeyrelease(lambda: key_up("s"), "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    
    # ✅ Move paddles every frame if key pressed
    if keys_pressed["Up"]:
        r_paddle.go_up()
    if keys_pressed["Down"]:
        r_paddle.go_down()
    if keys_pressed["w"]:
        l_paddle.go_up()
    if keys_pressed["s"]:
        l_paddle.go_down()
    
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Ball out of boundary
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= 11:
        game_is_on = False
        screen.textinput(title="Game Over!", prompt=f"Left Player Wins with {scoreboard.l_score} points!")
    elif scoreboard.r_score >= 11:
        game_is_on = False
        screen.textinput(title="Game Over!", prompt=f"Right Player Wins with {scoreboard.r_score} points!")

screen.exitonclick()

# import turtle as t
# from paddle import Paddle   
# from ball import Ball
# from scoreboard import ScoreBoard

# import time

# screen=t.Screen()
# screen.setup(width=800,height=600)
# screen.bgcolor("black")
# screen.title("Pong : The Arcade Game")
# screen.tracer(0)


# scoreboard=ScoreBoard()
# r_paddel=Paddle((350,0))
# l_paddel=Paddle((-350,0))
# ball=Ball()

# screen.listen()

# # onkeypress for continous press of key to move

# screen.onkey(r_paddel.go_up,"Up")
# screen.onkey(r_paddel.go_down,"Down")
# screen.onkey(l_paddel.go_up,"w")
# screen.onkey(l_paddel.go_down,"s")

# game_is_on=True

# while game_is_on:
#     time.sleep(ball.ball_speed)
#     screen.update()
#     ball.move()


#     # collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         # needs to bouceoff
#         ball.bounce_y()

#     # collision with paddel
#     if (ball.distance(r_paddel) < 50  and ball.xcor() > 320) or (ball.distance(l_paddel) <50 and ball.xcor() < -320):

#         ball.bounce_x()


#     # Ball goes out of boundary

#     # detect r side player misses
#     if ball.xcor() > 380 :
#         ball.reset_position()
#         scoreboard.l_point()
        
#     # detect l side player misses
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()




# screen.exitonclick()
