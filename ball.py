from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed = 0.05
        self.bounce_cooldown = 0  # ✅ cooldown counter
        

    def move(self):
        if self.bounce_cooldown > 0:  # ✅ decrement cooldown
            self.bounce_cooldown -= 1
        new_x=self.xcor() + self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        '''ball collision with walls'''
        self.y_move *= -1

    def bounce_x(self):
        if self.bounce_cooldown == 0:  # ✅ only bounce if not in cooldown
            self.x_move *= -1
            if self.ball_speed > 0.01:
                self.ball_speed *= 0.9
            self.bounce_cooldown = 5  # ✅ set cooldown for 5 frames

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.05
        self.bounce_x()
