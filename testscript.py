import time
import random

# Main stuff yo
def main():
    while(1):
        i = input("Enter \"1\" for timer, or \"2\" for an odd/even function")
        if i == 1:
            timer()
        elif i == 2:
            is_even()
        else:
            print("Uhh, try again?\n")

def timer():
    while(y != 'y'):
        y = 'n'
        init_time = time.time()
        x = input("Press the spacebar")
        if x == " ":
            tot_time = time.time() - init_time
            print(f"Wow, it took you {} seconds to press the spacebar\n", tot_time)
            y = input("exit?")

def is_even(x):
    if x % 2 == 0:
        return("Yep\n")
    else:
        return("Nope\n")

def coin_flip():
    return random.choice(['Heads', 'Tails'])

# In case this is ever imported
if __name__ == "__main__"
    main()