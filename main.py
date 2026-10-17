import turtle as t
import random

is_race_on =False
screen=t.Screen()
screen.title("Turtle Race")
screen.setup(width=800,height=600)
screen.bgpic("image.png")

colors=["red","pink","blue","orange","green","black"]
y_posi=[175,100,30,-40,-115,-185]
all_turtle=[]
leaderboard = {}

def create_turtle():
    for index in range(0,6):
        new_turtle=t.Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(-350,y=y_posi[index])
        all_turtle.append(new_turtle)

def reset_turtle():
    for turtle in all_turtle:
        turtle.goto(-350,turtle.ycor())
    
def race():
    is_race_on = True

    while is_race_on :
        for turtle in all_turtle:
            if turtle.xcor() > 310:
                is_race_on=False
                winning_color=turtle.pencolor()

                if winning_color == user_bet:
                    print(f"You have Won ! The {winning_color} turtle is the winner .")
                    return True
                else:
                    print(f"You have Lost ! The {winning_color} turtle is the winner .")
                    return False
                break

            random_distance = random.randint(0,10)
            turtle.forward(random_distance)

def update_leaderboard(player_name,won):
    if player_name not in leaderboard:
        leaderboard[player_name] = {"wins":0,"loss":0}
    if won :
        leaderboard[player_name]["wins"] +=1
    else:
        leaderboard[player_name]["loss"] +=1
    
def show_leaderboard():
    print("\n========== LEADERBOARD ==========")
    for player, stats in sorted(leaderboard.items(), key=lambda x: x[1]["wins"], reverse=True):
        print(f"{player}: {stats['wins']} wins, {stats['loss']} loss")
    print("================================\n")

create_turtle()

player_name = screen.textinput(title="Welcome!",prompt="Enter your name:")

play_again=True

while play_again:
    reset_turtle()
    user_bet = screen.textinput(title="Make your Bet!",prompt="Enter the color? Which turtle will win : ")
    if not user_bet:
        break

    won = race()

    update_leaderboard(player_name,won)

    response = screen.textinput(title="Play Again?", prompt="Type 'yes' or 'no':")
    
    if response and response.lower() == "yes":
        play_again = True
    else:
        play_again = False
show_leaderboard()
screen.exitonclick()
