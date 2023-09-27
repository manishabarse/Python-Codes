'''
 Create an interface like that from the movie War Games.\
 Ask the "Shall we play a game?"\
 If the user asks to play any game but chess print "Wouldn't you prefer to play chess?"\
 If they say chess, print something and exit.
'''

print(" 'War Games' \n ")
user_response = (input("Shall we play a game? Answer Yes or No: \n")).capitalize()

while True:
    if user_response.capitalize() == 'Yes' or user_response.capitalize() == 'No':
        break
    else:
        print("Please answer Yes or No \n")
        user_response = (input("Shall we play a game? Answer Yes or No: \n")).capitalize()


        
if user_response == 'No':
    print("Okay, see you later")
elif user_response == 'Yes':
    game = (input('Which game do you want to play?')).capitalize()
    if game == 'Chess':
        print("Yay! Let's play Chess")
    else:
        response = (input("Wouldn't you prefer to play Chess? 'Yes' or 'No'")).capitalize()
        while True:
            if response == 'Yes' or response == 'No':
                if response == "Yes":
                    print("Yay! Let's play Chess")
                    break
                else:
                    response = (input("Wouldn't you prefer to play Chess? 'Yes' or 'No'")).capitalize()
            else:
                print("Please answer in Yes or No: \n")
                response = (input("Wouldn't you prefer to play Chess? 'Yes' or 'No'")).capitalize()
        




