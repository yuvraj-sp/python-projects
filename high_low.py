import random 
from game_data import data 
from art import logo,vs

def format_data(account):
    """convert the dictionary data into printable form """
    account_name=account["name"]
    account_desc=account["description"]
    account_country=account["country"]
    return (f"{account_name} , a {account_desc} , from {account_country}")

# def compare(acc_a,acc_b):
#     """compare both account A and B with follower."""                maybe i was cooked 
#     winner=""
#     guess=""
#     guess=input("Who has more Followers ? Type 'A' or 'B' ").lower()
#     a_follower=acc_a["follower_count"]
#     b_follower=acc_b["follower_count"]
#     if a_follower>b_follower:
#         winner=a_follower
#     else:
#         winner=b_follower
#     if guess 

def compare(user_guess, a_follower ,b_follower):
    """Takes user guess and follower count and returns if user got it correct"""
    if a_follower > b_follower:
        return user_guess=="a"
    else:
        return user_guess=="b"
    

print(logo)
print("Welcome to Higher Lower game")
score=0
account_b=random.choice(data)
game_should_continue=True

while game_should_continue:

    # generate a random account from the game data 
    account_a=account_b
    account_b=random.choice(data)
    if account_a == account_b :   #still same data can apper so can use while instead
        account_b=random.choice(data)

    print(f"Compare A : {format_data(account_a)} .")
    
    print(vs)
    print(f"Againts B : {format_data(account_b)} .\n")
    guess=input("Who has more Followers ? Type 'A' or 'B' ").lower()
    a_follower=account_a["follower_count"]
    b_follower=account_b["follower_count"]

    is_correct=compare(guess,a_follower,b_follower)

    if is_correct:
        score+=1
        print(f"You are correct ! Current Score : {score}")
        print("\n"*20)
    else:
        print(f"Sorry , Thats wrong Final Score : {score}")
        game_should_continue=False
    
