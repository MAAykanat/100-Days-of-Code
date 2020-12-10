#Day Number: 4
#Day Level: Beginner
#The topic: Randomisation and Python Lists

# Duty: Rock-Paper-Scissors
## Creating a program that plays rock-paper-scissors with you :)

import random

rock_ = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_ = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_ = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
map_display = [rock_, paper_, scissors_]
map = ['rock', 'paper', 'scissors']

try_of_game = 'y'
while(try_of_game.lower() != 'n'):
    
    choice = int(input("What do U choose?\n" + "Type 0: Rock " + "Type 1: Paper " + "Type 2: Scissors\nType:"))
    comp_choice = random.randint(0,2)

    print(f"Your choice:\n{map_display[choice]}")
    print(f"Computer choice:\n{map_display[comp_choice]}")

    if map[choice] == 'rock' and map[comp_choice] == 'scissors':
        print("You Win!")
    elif map[choice] == 'rock' and map[comp_choice] == 'paper':
        print("You Lose!")
    elif map[choice] == 'paper' and map[comp_choice] == 'rock':
        print("You Win!")
    elif map[choice] == 'paper' and map[comp_choice] == 'scissors':
        print("You Lose!")
    elif map[choice] == 'scissors' and map[comp_choice] == 'paper':
        print("You Win!")
    elif map[choice] == 'scissors' and map[comp_choice] == 'rock':
        print("You Lose!")
    elif map[choice] == 'rock' and map[comp_choice] == 'scissors':
        print("It is a tie!")
    else: 
        print("You entered wrong choice type\nType between 0 and 2")
    
    try_of_game = input("Do wanna try again?(Y/N)")

