#! python3
# by Victour Bue

# You can either guess a number or have the computer guess your number.

from random import randint


def game_selection():
    print("\nWelcome to the Number Guessing Game!")
    game = input("Would you like to play as the Guesser or the Guessie? (enter to quit) ")
    if (game.lower() == "guesser" or game.lower() == "guessie"):
        return game
    elif not game:
        return game
    else:
        print("Sorry I don't understand that. Please try again.")
        return game_selection()



def guessie_game():
    print("Okay you pick any number between 1-100 and I'll try to guess")
    getting_number = True
    while getting_number:
        response = input("Did you think of a number? yes/no ")
        if (response == "yes" or response == "Yes"):
            getting_number = False
            number_of_guesses = 0
            guessing = True
            min = 1
            max = 100
            computer_guess = randint(min,max)
            while guessing:
                player_feedback = input(f"\nIs {computer_guess} '<' or '>' or '=' your number? ")
                if (player_feedback == ">"):
                    print(f"So {computer_guess} is greater than your number. Okay, I'll remember that!")
                    max = computer_guess - 1
                    computer_guess = randint(min,max)
                    number_of_guesses += 1
                elif (player_feedback == "<"):
                    print(f"So {computer_guess} is less than your number. Okay, I'll remember that!")
                    min = computer_guess +1
                    computer_guess = randint(min,max)
                    number_of_guesses += 1
                elif (player_feedback == "="):
                    print("WOW! That is the correct number")
                    number_of_guesses += 1
                    print(f"It took me {number_of_guesses} guesses!")
                    guessing = False
                else:
                    print("sorry I didn't understand that, please try again.")
                    
        elif (response == "no" or response == "No"):
            print("Okay, I'll wait a bit longer...")
        else:
            print("Sorry I didn't understand that.") 



def guesser_game():
    print("Selecting a random number between 1-100...")
    computer_number = randint(1, 100)
    guessing = True
    number_of_guesses = 0 
    print("Okay I'm all ready.")
    while guessing:
        try:
            user_guess = int(input("\nPlease guess a number between 1-100 "))
        except:
            print("sorry I didn't understand that, please try again.")
            continue

        if (user_guess < computer_number):
            print("Your guess is less than the correct number.")
            number_of_guesses += 1
        elif (user_guess > computer_number):
            print("Your guess is greater than the correct number.")
            number_of_guesses += 1
        elif (user_guess == computer_number):
            print("WOW! That is the correct number")
            number_of_guesses += 1
            print(f"It took you {number_of_guesses} guesses!")
            guessing = False
        else:
            print("sorry I didn't understand that, please try again.")
 
  

def main():
    game = game_selection()
    if not game:
        return

    if (game.lower() =="guessie"):
        guessie_game()
    else:
        guesser_game()
    
    return main()


main()
