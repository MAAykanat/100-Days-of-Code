#Day Number: 7
#Day Level: Beginner
#The topic: Hangman

# Duty: Creating code that offers you to play Hangman game
import random
def random_word(word_list):
    rand_index = random.randint(0,len(word_list)-1)
    random_word = word_list[rand_index]
    return random_word

def blank_list(word):
    blank = []
    for _ in range(0,len(word)):
        blank.append("_")
    return blank

def display(stage_index):
    stages = ['''
        +----+
        |       |
        O       |
       /|\      |
       / \      |
                |
    ===========
    ''','''
        +----+
        |       |
        O       |
       /|\      |
       /        |
                |
    ==========
    ''','''
        +----+
        |       |
        O       |
       /|\      |
                |
                |
    ==========
    ''','''
        +----+
        |       |
        O       |
       /|       |
                |
                |
    ==========
    ''','''
        +----+
        |       |
        O       |
       /        |
                |
                |
    ==========
    ''','''
        +----+
        |       |
        O       |
                |
                |
                |
    ==========
    ''','''
        +----+
        |       |
                |
                |
                |
                |
    ==========
    ''']
    print(stages[stage_index])

def display_blanks(blank_list):
    blank = ''
    for _ in range(0,len(blank_list)-1):
        blank = " ".join(blank_list)
    
    return blank

word_list = ["ardvark", "baboon", "camell"]

word = random_word(word_list)
word_lenght = len(word)
blanks = blank_list(word)

check_loop = False
num_of_lives = 6
iteration_number = 0
print(word)
# print(word_lenght)

while (check_loop != True):
    display(num_of_lives)
    print(display_blanks(blanks))
    iteration_number += 1

    print("The iteration step of loop is: {}".format(iteration_number))
    guess_letter = input("Guess a letter: ").lower()

    for i in range(0,word_lenght):
        if word[i] == guess_letter:
            blanks[i] = guess_letter

    if ('_' not in blanks): 
        check_loop = True
        print("You win buddy!!!")
    elif guess_letter not in word:
        num_of_lives -= 1
    elif num_of_lives == 0:
        print("You lose buddy:(")
        check_loop = True

# print("The result is: {}".format(blank))