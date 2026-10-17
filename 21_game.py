import random
import logo

def deal_cards():
    """Returns a random card from a deck """
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(deck)
    return card

def calculate_score(deck):
    """ Take the list of cards and return the score calculated from the card """
    if sum(deck)==21 and len(deck)==2:
        return 0 
    
    if 11 in deck and sum(deck)>21:
        deck.remove(11)
        deck.append(1)
        
    return sum(deck)

def compare(u_score,c_score):
    "Compares the score of user and computer and returns result"
    if u_score==c_score:
        return "Draw!"
    elif u_score==0:
        return "Win with Blackjack "
    elif c_score==0:
        return "Lose , Opponent Won with Blackjack"
    elif u_score>21:
        return "\n\nYou went over . You lose"
    elif c_score>21:
        return "\n\nOpponent went over . You win"
    elif u_score>c_score:
        return "\n\nYou won! "
    else:
        return "\n\nYou Lose "
        
def play_game():
    print(logo.art)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1

    is_game_over=False



    for _ in range(2):
        # new_card=deal_cards()
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while not is_game_over:
            
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"\nComputer's First Card : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal= input("Enter 'y' to get another card or 'n' to pass : ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"\n\nYour final cards : {user_cards} Your final score : {user_score}")
    print(f"\nComputer final cards : {computer_cards} Computer final score : {computer_score}")
    print(compare(user_score,computer_score))

     
while input("Do you want to play Blackjack TYPE 'y' or 'no' to Quit the Game : ").lower()=="y":
    print("\n"*20)
    play_game()

