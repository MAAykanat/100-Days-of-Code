#Day Number: 3
#Day Level: Beginner
#The topic: Control Flow and Logical Operators

# Duty: Treasure Island
## Creating a program that you can get a tresuare in Treasure Island

def door_decision_func():

    door_decision = input("Which door do you want to pass?\nB(Blue)-Y(Yellow)-R(Red)")

    if door_decision.lower() == 'b':
            print("You win!")
    else:
        print("Game Over!")

try_of_game = 'y'

while(try_of_game.lower() != 'n'):
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    direction = input("Which direction do you want to go?\n E(East)-W(West)-N(North)-S(South)")
    if direction.lower() == 'e':
        if input("Do you know how to swim?(Y/N)\n").lower() == 'y':
            print("You passed the secret lake")
            door_decision_func()
        elif input("Do you know how to fly?(Y/N)").lower() == 'y':
            print("You passed the secret lake")
            door_decision_func()
        else:
            print("Game Over!")

    elif direction.lower() == 's':
        print("There is volcano and no going back")
        print("Game over!")

    elif direction.lower() == 'n':
        self_defence = input("There are wild animals!\nDo you have gun?(Y/N)")
        if self_defence == 'Y':
            print("You are alive go through the doors!")
            door_decision_func()
        else:
            print("Game over!")
    elif direction.lower() =='w':
        print("There is a maze!")
        decision = input("Do you wanna try it?(Y/N)\n")
        if decision.lower() == 'y':
            print("Wrong choice\nGame Over!")
        elif decision.lower() == 'n':
            print("Be brave and select yes!")
            decision2 = input("Do you wanna try it?(Y/N)\n")
            if decision2.lower() =='y':
                print("Nice try brave heart but wrong again!")
                print("Game over!")
            else:
                print("Okay it was at least try.")
    else:
        print("You did not enter a direction. Correct it!")

    try_of_game = input("Do wanna try again?(Y/N)")