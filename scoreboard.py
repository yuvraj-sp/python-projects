from turtle import Turtle
FONT=("courier", 20, "normal")
ALIGNMENT="center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.goto(0,270)
        self.color("white")
        self.penup() 
        self.hideturtle()
        self.score_update()
        


    def score_update(self):
        self.clear()
        self.write(f"Score :{self.score} HighScore :{self.highscore}",align=ALIGNMENT,font=FONT )
    

    def increase_score (self):
        self.score+=1
        self.clear()
        self.score_update()
        

    def reset(self):
        if self.score > self.highscore :
            self.highscore=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)
        