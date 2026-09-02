# Exercise 6

import random
import time

def dice_roll(guess=(1, 3), n=100):
    start_time = time.perf_counter()
    correct_count = 0
    
    for _ in range(n):
        roll = random.randint(1, 6)
        if roll in guess:
            correct_count += 1
            
    end_time = time.perf_counter()
    proportion = correct_count / n
    execution_time = end_time - start_time
    
    return proportion, execution_time

proportion, running_time = dice_roll(guess=(1, 6), n=100000)
print(f"Proportion: {proportion}")
print(f"Running Time: {running_time:.6f} seconds")