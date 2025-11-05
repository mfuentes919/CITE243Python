"""
===========================================================
Program Name: pretty_stopwatch.py
Author: Matthew Fuentes
Date: 11/5/2025
Description:
    This program performs the functionality of a stopwatch with a formated output.
    It is designed to keep track of the amount of time it takes to complete a lap.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

# A simple stopwatch program
import time

# Display the program's instructions.
print('Press ENTER to begin and to mark laps. Ctrl-C quits.')
input()  # Press Enter to begin.
print('Started.')
start_time = time.time()  # Get the first lap's start time.
last_time = start_time
lap_number = 1

# Start tracking the lap times.

try:
  while True:
    input()
    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)
    print(f'Lap # {lap_number}:'.ljust(10) + f'{total_time}'.center(12) + f'(   {lap_time})'.rjust(10), end='')
    # Added formatting options with rjust, ljust, and center
    lap_number += 1
    last_time = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
