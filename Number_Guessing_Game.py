"""
Number guessing game. Ask the user to guess a number, check if the guessed number is same as current time seconds
"""

import random
import time
from time import strftime
from datetime import datetime

#formatted_time = curr_time.strftime('%S')
#print("Formatted time in Seconds is",formatted_time)


def number_guessing_game():
    print("Welcome to the guessing game! I'm thinking of a number between 1 and 59. \n")
    curr_time = datetime.now()
    print(type(curr_time))
    gen_number = int(curr_time.strftime('%S'))
    #gen_number = random.randint(1, 59)
    num_guesses = 0

    while num_guesses < 5:
        #curr_time = datetime.now()
        #gen_number = int(curr_time.strftime('%S'))
        #gen_number = int(curr_time.strftime('%S'))
        guess = input("Guess a number: \n")
        num_guesses += 1
        try:
          guess = int(guess)
        except ValueError:
          print("That's not a number! Try again. \n")
          num_guesses -= 1
          continue
        
        if guess in range(2,59):
            if guess < gen_number:
                print("Your guess is less than the random number, guess a bigger number \n")
            elif guess > gen_number:
                print("Your guess is greater than the random number, guess a smaller number \n")
            else:
                break
        else:
            print("Your guess is out of range. \n")
            num_guesses -= 1
    
    if guess == gen_number:
        print('Congratulations! You guessed the number in ' + str(num_guesses) + ' tries!')
    else:
        print('Sorry, you did not guess the number. The number was ' + str(gen_number))



number_guessing_game()
