"""
=====================================================================
Program Name:   passwd_checker.py
Author:         Matthew Fuentes
Date:           9-24-2025
Description:
    This program takes a user-input string and checks it to see if it is a strong password.
    It is designed to validate that the string is at least 8 characters long, have both upper and lowercase characters,
        and have at least one digit.

Usage:
    Run the program using Python 3.13.7. Ensure all dependencies are installed before execution.
    Humre was used, install in cmd line using: "pip install humre"
"""

import re

while True:
    # Asks user for a password
    print("Welcome to Password Checker!")
    print("Please input a password:")
    
    psswd = input()

    # Checks if passwod is 8 characters or more
    if len(psswd) >= 8:
        psswd_len = True
    else:
        psswd_len = False

    # Checks is password has an uppercase character    
    psswd_up_regex = re.compile(r'[A-Z]')

    if psswd_up_regex.search(psswd) == None:
        psswd_up = False
    else:
        psswd_up = True

    # Checks if password has a lowercase character
    psswd_low_regex = re.compile(r'[a-z]')

    if psswd_low_regex.search(psswd) == None:
        psswd_low = False
    else:
        psswd_low = True

    # Checks if password has at least one number
    psswd_num_regex = re.compile(r'\d+')

    if psswd_num_regex.search(psswd) == None:
        psswd_num = False
    else:
        psswd_num = True

    # Checks if password meets all requirements, asks user to put in new password if not
    if psswd_len == True and psswd_num == True and psswd_up == True and psswd_low == True:
        print("You're password has been accepted!")
    else:
        print("You're password has been rejected!\n")
        print("Please input a password that is:\n- 8 characters or more long\n- Has an uppercase and lowercase character\n- Has one or more numbers\n")
        continue

    # Asks if user wants to use the program again, ends if not
    play_again = input("Would you like to check another password? (y/n): ")
    if play_again == 'y':
        continue
    elif play_again == 'n':
        print("Thank you for using Password Checker!")
        break