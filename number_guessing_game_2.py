'''
- Create a new random number guessing program.\
- All the previous conditions are the same plus:\
– Have the user keep guessing until the get the number correct.\
– Count the number of guesses.\
– If the number of guesses is 1, print "Excellent"\
– If the number of guesses 2-19 print "OK"\
– If the number of guesses is 20 print "Bad."
'''


import random

print("Guess Random Number Game")

gen_rand = random.randint(0,20)

while True:
    try:
        user_input = int(input("Guess a number between 0 and 20: \n"))
        break
    except:
        print('Exception occured')
        continue
    
count = 1
while gen_rand != user_input:
    try:
        if user_input in range(1,20): ###range() includes start value, excludes stop values
            if gen_rand > user_input:
                print("Your guess is less than the random number, guess bigger number \n")
                user_input = int(input("Guess again a number between 0 and 20: \n"))
                count += 1
            elif gen_rand < user_input:
                print("Your guess is higher than the random number, guess smaller number \n")
                user_input = int(input("Guess again a number between 0 and 20: \n"))
                count += 1
        else:
            print("Your guess is out of range")
            user_input = int(input("Guess again a number between 0 and 20: \n"))
            count += 1
    except Exception as ex:
        print(ex)
        
if count == 1:
    print("Excellent! You guessed the correct number in the first attempt!")
elif 2<= count <= 19:
    print(f'OK, You guessed the correct number in the {count} attempt!')
else:
    print(f'Bad, You exhausted all the chances!')
