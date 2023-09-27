#Create a program that prompts the user for a number. \
#Generate a random number between 1 and 20.\
#If the users guess is lower than the number print that it is less.\
#If the users guess is higher than the number print that it is higher.\
#If it is out of range print that it is out of range

import random
gen_rand = random.randint(0,20)
user_input = input("Guess a number between 0 and 20: ")
user_input = int(user_input)


while gen_rand != user_input:
    if user_input in range(0,20):
        if gen_rand > user_input:
            print("Your guess is less than random number, guess bigger number")
            user_input = int(input("Guess again a number between 0 and 20: \n"))
        elif gen_rand < user_input:
            print("Your guess is higher than random number, guess smaller number")
            user_input = int(input("Guess again a number between 0 and 20: \n"))
    else:
        print("Your guess is out of range")
        user_input = int(input("Guess again a number between 0 and 20: \n"))


print("You guessed the correct number")




