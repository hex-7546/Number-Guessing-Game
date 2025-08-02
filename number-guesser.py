import random

intro = """
Welcome to the Number Guessing Game

Level of difficulty is as follows:
Easy : 10 attempts
Medium : 7 attemmpts
Hard : 5 attempts
"""
print(intro)

attempts = int(input("How many attempts do you want: "))

comp_num = random.randint(1, 100)

for i in range(attempts):
    user_num = int(input("Enter a guess> "))

    if user_num == comp_num:
        print("You are correct")
        break
    elif user_num > comp_num:
        print("Your guess is higher")
    elif user_num < comp_num:
        print("Your guess is lower")
else:
    print("Error. Try again")
    