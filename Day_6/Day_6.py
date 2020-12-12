#Day Number: 6
#Day Level: Beginner
#The topic: Python Functions

# Duty: Helping Robot Reeborg to get out of maze
## This script is not actually Python script, I had used link below to give a path to Robot Reborg
## It was very enjoyable to do it, Link is below go and try :)
## https://reeborg.ca/reeborg.html
### Search for Maze and used code below to run the code :)

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    
    if not right_is_clear() and front_is_clear():
       move()
    elif not right_is_clear() and not front_is_clear():
        turn_left()
    else:
        turn_right()
        move()

'''