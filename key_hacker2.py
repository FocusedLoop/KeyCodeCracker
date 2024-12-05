import pydirectinput
import keyboard
import time

# Key press delay
pydirectinput.PAUSE = 0.01

try:
    digit_combination = input("How many digits is the combination?")
    digit_combination = int(digit_combination)
    total_combinations = 10**digit_combination

    for i in range(5, 0, -1):
        print(f"Starting in {i}")
        time.sleep(1)
    
    # Attempt Combinations
    for i in range(total_combinations):

        # Check for stop key
        if keyboard.is_pressed('-'):
            print("\nProcess stopped by user")
            break

        combination = f"{i:0{digit_combination}d}"
        for d in combination:
            pydirectinput.press(f"{d}")
        time.sleep(0.5) # Account for game time
        
        print(f"Progress: {i + 1}/{total_combinations} combinations attempted")

except StopIteration:
    print("\nAll possible combinations have been achieved!")
except KeyboardInterrupt:
    print("\nAre ya cracking the code son?")