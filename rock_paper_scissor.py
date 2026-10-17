import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
user_input=int(input("Lets play Rock,Paper and Scissor !chosse 0 rock 1 scissor 2 paper"))
com_input=random.randint(0,2)
if user_input==0:
    print(rock)
    if com_input==0:
        print(rock)
        print("Match Tied")
    elif com_input==1:
        print(scissor)
        print("You Won")
    elif com_input==2 :
        print(paper)
        print("You Lost")
    else :
        print("Invalid input")
if user_input==1:
    print(scissor)
    if com_input==0:
        print(rock)
        print("You lost")
    elif com_input==1:
        print(scissor)
        print("Match Tied")
    elif com_input==2 :
        print(paper)
        print("You Won")
    else :
        print("Invalid input")
if user_input==2:
    print(paper)
    if com_input==0:
        print(rock)
        print("You Won")
    elif com_input==1:
        print(scissor)
        print("You Lost")
    elif com_input==2 :
        print(paper)
        print("Match Tied")
    else :
        print("Invalid input")
