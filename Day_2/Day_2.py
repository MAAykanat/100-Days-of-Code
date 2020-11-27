#Day Number: 2
#Day Level: Beginner
#The topic: Understanding Data Types and How to Manipulate Strings

# Duty: Tip Calculator
## Creating a program that calculates to find out bill for per person including selecting tip

print("Welcome to tip calculator!")

total_bill = float(input("What was the total bill?\n"))
tip_perc = int(input("What percentage tip would yo like to give?\n"))
num_of_people = int(input("How many people to split the bill?\n"))
bill_per_person = (total_bill + (total_bill*tip_perc/100))/num_of_people

print(round(bill_per_person,2))
