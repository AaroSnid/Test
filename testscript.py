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

if __name__ == "__main__":
    main()