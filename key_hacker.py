import pydirectinput
import random as rand
import time

pydirectinput.PAUSE = 0.01

try:
    for i in range(5):
        print("printing in", 5 - i)
        time.sleep(1)

    combinations = set()
    digit_combination = 4
    total_combinations = 10**digit_combination

    while True:
        combination = tuple([rand.randint(0, 9) for _ in range(digit_combination)])
        
        if combination in combinations:
            combinations.remove(combination)
            print("Removed combination:", combination)
        else:
            combinations.add(combination)
            print("New combination:", combination)

        for i in combination:
            pydirectinput.press(f"{i}")
        
        progress = len(combinations)
        

        if progress == total_combinations:
            raise StopIteration

except StopIteration:
    print("\nAll possible combinations have been achieved!")
except KeyboardInterrupt:
    print("\nAre ya cracking the code son?")
