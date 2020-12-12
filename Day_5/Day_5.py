#Day Number: 5
#Day Level: Beginner
#The topic: Python Loops

# Duty: Create a Password Generator
## Creating a program that can create password as you wish

import random

def printing_password(generated_password):
    password = ''
    for _ in range(0,len(generated_password)-1):
        password = ''.join(generated_password)

    print(password)

def loop_func(list_name,length):
    generated_password = []
    for _ in range(0,length):
        random_variable = random.randint(0,(len(list_name)-1))
        generated_password.append(list_name[random_variable])
    return generated_password

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

result_password = []

print("Welcome to the Pypassword Generator!")
num_letters = int(input("How many letters would you like in you password?"))
num_symbols = int(input("How many symbols would you like?")) 
num_digits = int(input("How many digits would you like?"))

result_password = [*result_password,*(loop_func(letters,num_letters)),*(loop_func(symbols,num_symbols)),*(loop_func(digits,num_digits))]

printing_password(result_password)
