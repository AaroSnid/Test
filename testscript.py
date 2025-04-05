import time

while(y != 'y'):
    y = 'n'
    init_time = time.time()
    x = input("Press the spacebar")
    if x == " ":
        tot_time = time.time() - init_time
        print(f"Wow, it took you {} seconds to press the spacebar\n", tot_time)
        y = input("exit?")

