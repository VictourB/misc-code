#! python3
# by Victour Bue

# Ask the player if they'd like to play rock, paper scissors.
# Give the option to have the rules of the game explained.

from random import randint


def invite_player():
    print("""
    Welcome to the Rock, Paper, Scissors Game!
    Step right up and see if you can defeat the all knowing ~algorithm~
    """)
    consent = input("Would you like to play? Yes/No/Huh? ")
    if ( consent.lower() == "yes" or consent.lower() == "no"):
        return consent
    elif (consent.lower() == "huh" or consent.lower() == "huh?"):
        print(f"""
    The goal of Rock, Paper, Scissors is to pick one of the three titular items and see how it pairs up with an opponent.
    There is a set way of determining the winners and losers here. Rock beats Scissors, Scissors beats Paper, and finally Paper beats Rock.
        """)
        return invite_player()
    else:
        print("Sorry, I don't understand that.")
        return invite_player()


def get_computer_response():
    ai_hand_state = randint(0,3)
    print("I'm ready, are you?")
    return ai_hand_state
    

def get_player_response():
    player_hand_state = input("What's it gonna be? Rock/Paper/Scissors ")
    match player_hand_state.lower():
        case "rock":
            return 0
        case "paper":
            return 1
        case "scissors":
            return 2
        case _:
            print("ERROR not a valid case.")
    return get_player_response()


def calc_winner(player, ai):
    print("")
    if (ai == player):
        print("The game ended in a tie!")
        if player == 0 : player = "Rock"
        elif player == 1 : player = "Paper"
        else : player = "Scissors"

        if ai == 0 : ai = "Rock"
        elif ai == 1 : ai = "Paper"
        else : ai = "Scissors"

        print(f"You chose {player}")
        print(f"The Computer chose {ai}")
    elif(ai == 0 and player == 2):
        print("The Computer chose Rock!")
        print("You chose Scissors")
        print("The Computer Wins!")
    elif(ai == 1 and player == 0):
        print("The Computer chose Paper!")
        print("You chose Rock.")
        print("The Computer Wins!")
    elif(ai == 2 and player == 1):
        print("The Computer chose Scissors!")
        print("You chose Paper.")
        print("The Computer Wins!")
    else:
        print("I guess you're not as bad as I thought.")
        if player == 0 : player = "Rock"
        elif player == 1 : player = "Paper"
        else : player = "Scissors"

        if ai == 0 : ai = "Rock"
        elif ai == 1 : ai = "Paper"
        else : ai = "Scissors"
        print(f"You chose {player}")
        print(f"The Computer chose {ai}")
    

def main():
    consent = invite_player()
    if consent.lower() == "no":
        return
    ai_response = get_computer_response()
    player_response = get_player_response()
    calc_winner(player_response,ai_response)

    return main()


main()