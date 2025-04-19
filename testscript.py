import time
import random

def main():
    while 1:

        #Prints the options to the user
        print("Here is a list of available functions:")
        print("1. Timer")
        print("2. Even determiner")
        print("3. Coin flipper\n")

        #Makes sure that the user enters a number for selection
        try:
            i = int(input("Input desired function\'s number\n"))
        except ValueError:
            print("Please enter an integer\n")
            continue

        #Choosing the function to execute
        match i:
            case 1:
                timer()
            case 2:
                print(f"Your number {is_even()} even")
            case 3:
                print(f"The coin flipped {coin_flip()}\n")
            case _:
                print("Invalid number detected, please try again\n")

def timer():
    """Displays the time it takes the user to press the space bar"""

    y = 'n'
    while y != 'y':
        y = 'n'
        init_time = time.time()
        x = input("Press the space bar, then enter")
        if x == " ":
            tot_time = time.time() - init_time
            print(f'It took you {tot_time} seconds to press the space bar\n')
            y = input("exit? (y/n)")

def is_even() -> str:
    """Checks if a value entered by the user is even"""

    #Data validation for the user's number
    while 1:
        y = input("Input your glorious number, and I shall declare if it is even.\n")
        try:
            x = int(y)
            break
        except ValueError:
            print('Please enter an integer')

    if x % 2 == 0:
        return "is"
    else:
        return "is not"

def coin_flip():
    return random.choice(['heads', 'tails'])

def rochambeau():

    #Declaring variables
    y = 'n'
    program_score = 0
    player_score = 0

    #Main loop for the game
    while y != 'y':
        print(f"Current Score:")
        print(f"Player: {player_score} Program: {program_score}\n")

        #Get valid user input
        while 1:
            player_choice = input("Choose rock, paper, or scissors")

            #Dealing with capital letters in user input
            if "ock" in player_choice:
                player_choice = "rock"
                break
            elif "aper" in player_choice:
                player_choice = "paper"
                break
            elif "cissors" in player_choice:
                player_choice = "scissors"
                break
            else:
                print("Invalid selection, please try again")

        #Get the programs choice
        program_choice = random.choice(['rock', 'paper', 'scissors'])

        #Display program choice to the user, for fairness
        print(f"The program's choice is {program_choice}")

        #Determining the winner
        if player_choice == program_choice:
            print("The game is a tie!\n")
        elif player_choice == "paper":
            if program_choice == 'rock':
                print("Congratulations, you have won!\n")
                player_score += 1
            else:
                print("Sorry, you have lost.")
                program_score += 1
        elif player_choice == "rock":
            if program_choice == 'scissors':
                print("Congratulations, you have won!\n")
                player_score += 1
            else:
                print("Sorry, you have lost.")
                program_score += 1
        elif player_choice == "scissors":
            if program_choice == 'paper':
                print("Congratulations, you have won!\n")
                player_score += 1
            else:
                print("Sorry, you have lost.")
                program_score += 1

        y = input("Would you like to play again? (y/n)\n")



if __name__ == "__main__":
    main()