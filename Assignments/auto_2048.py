"""
===========================================================
Program Name: auto_2048
Author: Matthew Fuentes
Date: 10/13/2025
Description:
    This program plays the game 2048 with random inputs
    It is designed to bruteforce the most effective way of playing 2048.
    
Usage:
    Run the script using Python 3.14. Ensure all dependencies
    are installed before execution.

===========================================================
"""

# Import modules
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Sets browser as Firefox
browser = webdriver.Firefox()

# Opens 2048
browser.get('https://play2048.co/')
html_elem = browser.find_element(By.TAG_NAME, 'html')

# Waits for page to load
time.sleep(3)

# List of inputs
inputs = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

# Did max of 200 moves, farthest program got during testing with about 150
for i in range(200):
    rand_input = random.choice(inputs) # Grabs random key input from list
    html_elem.send_keys(rand_input) # Sends to website
    time.sleep(0.5) # Pause to prevent getting IP banned from 2048