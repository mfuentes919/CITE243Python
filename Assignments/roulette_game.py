"""
===========================================================
Program Name: roulette_game.py
Author: Matthew Fuentes
Date: 9/29/2025
Description:
    This program simulates roulette, having the user bet on a number and color.
    It is designed to take a user's bet, the amount they bet on, and compare it against
        the rolled number and color. 
    
Usage:
    Run the script using Python 3.x. Ensure all dependencies
    are installed before execution.

===========================================================
"""


# Numbered from 0 - 36
# From 1 - 10 & 19 - 28, odd numbers are red and even are black
# From 11 - 18 and 29 - 36, odd is black and even is red

# Simple roulette game

import random
import time
import math

# Roulette table, built as a dictionary
table = { 
    0: 'green',
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'black',
    12: 'red',
    13: 'black',
    14: 'red',
    15: 'black',
    16: 'red',
    17: 'black',
    18: 'red',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'black',
    30: 'red',
    31: 'black',
    32: 'red',
    33: 'black',
    34: 'red',
    35: 'black',
    36: 'red',
}

# Function that greets user
def start_game(game_balence):
    print("Welcome to Roulette for Russians!")
    print("Place your bets!")
    print(f"Your current balence is: ${game_balence}")

# Function that starts game, asks user if they want to loose it all
""" join_game not needed
def join_game(start):
    while True:
        if start.lower() == 'y':
            print("Excellent!")
            break
        elif start.lower() == 'n':
            print("Maybe another time...\nPlease come again!")
            break
        # Error handling for invalid input
        else:
            print("ERROR : Please try again")
            start = input("Will you be joining us at the table today? (y/n) ")
            if start.lower() == 'y':
                print("Excellent!")
                break
            elif start.lower() == 'n':
                print("Maybe another time...\nPlease come again!")
                break
            else:
                continue
"""

# Checks that user number bet is valid
def betting_option_num(num):
    while True:
        # Checks if betting on number
        if num >= 0 and num <= 36:
            number_betting = True
            return number_betting
        else:     
            number_betting = False
            return number_betting

# Checks that user color bet is valid
def betting_option_color(color):
    while True:
        # Checks if betting on color
        if color.lower() == 'red' or color.lower() == 'black':
            color_betting = True
            return color_betting
        else:
            color_betting = False
            return color_betting        

# Checks that user did not select 'no' for both number and color
def betting_option_check(num_betting, color_betting):
    if num_betting == False and color_betting == False:
        return False
    else:
        return True

# Simulates rolling
def rolling(roulette_num, roulette_color):
    print("May the odds be in your favor!\n")
    print("Roll \'em!")
    print("The ball is rolling...")
    time.sleep(1)
    print("The ball is slowing...")
    time.sleep(1)
    print(f"\nThe ball has landed on {roulette_num} {roulette_color.title()}!")


    """Note on Winner
    Function computes which is the outcome:
    
    1. Both number and color were bet on
    2. Only number
    3. Only color
    
    From which:
    
    1. win-win, win-lose, lose-win, lose-lose
    2. win, lose
    3. win, lose
    """
# Computes winning values to bet values and outputs win/lose on each bet
def winner(roulette_num, roulette_color, n_bet, c_bet, is_n_bet, is_c_bet):
    if is_n_bet == True and is_c_bet == True:
        if roulette_num == n_bet and roulette_color == c_bet:
            return 1
        elif roulette_num == n_bet and roulette_color != c_bet:
            return 2
        elif roulette_num != n_bet and roulette_color == c_bet:
            return 3
        else:
            return 4
    elif is_n_bet == True and is_c_bet == False:
        if roulette_num == n_bet:
            return 5
        else:
            return 6
    elif is_n_bet == False and is_c_bet == True:
        if roulette_color == c_bet:
            return 7
        else:
            return 8

# Calculates winnings based off of winner function
def win_lose_value(wcon, n_bet_amount, c_bet_amount, tbet=0):
    
    if wcon == 1:
        tbet = n_bet_amount + c_bet_amount
        return tbet
    elif wcon == 2:
        tbet == n_bet_amount - c_bet_amount
        return tbet
    elif wcon == 3:
        tbet = c_bet_amount - n_bet_amount
        return tbet
    elif wcon == 4:
        tbet = n_bet_amount + c_bet_amount
        tbet = -abs(tbet)
        return tbet
    elif wcon == 5:
        tbet = n_bet_amount
        return tbet
    elif wcon == 6:
        tbet = n_bet_amount
        tbet = -abs(tbet)
        return tbet
    elif wcon == 7:
        tbet = c_bet_amount
        return tbet
    elif wcon == 8:
        tbet = c_bet_amount
        tbet = -abs(tbet)
        return tbet

# Takes output from winner and win_lose_value functions and announces winnings/loses
def announcement(wcon, wtotal, account):
    
    if wcon == 1:
        print(f"Congratulations! You hit it big and won on both your bets!")
        print(f"You have won: ${wtotal}!!!")
        account = account + wtotal
        print(f"Your balence is now: ${account}!!!")
        return account
    elif wcon == 2:
        print(f"Good news and bad news! You won on your number, but lost on your color.")
        print(f"You have won: ${wtotal}")
        account = account + wtotal
        print(f"Your balence is now: ${account}")
        return account
    elif wcon == 3:
        print(f"Good news and bad news! You won on your color, but lost on your number.")
        print(f"You have won: ${wtotal}")
        account = account + wtotal
        print(f"Your balence is now: ${account}")
        return account
    elif wcon == 4:
        print(f"Better luck next time! You have lost on both your bets!")
        print(f"You have lost: ${wtotal}")
        account = account + wtotal
        print(f"Your balence is now: ${account}")
        return account
    elif wcon == 5:
        print(f"Congratulations! You won on your number!")
        print(f"You have won: ${wtotal}!")
        account = account + wtotal
        print(f"Your balence is now: ${account}!")
        return account
    elif wcon == 6:
        print(f"Better luck next time! You have lost on your number.")
        print(f"You have lost: ${wtotal}")
        account = account + wtotal
        print(f"Your balence is now: ${account}")
        return account
    elif wcon == 7:
        print(f"Congratulations! You won on your color!")
        print(f"You have won: ${wtotal}!")
        account = account + wtotal
        print(f"Your balence is now: ${account}!")
        return account
    else:
        print(f"Better luck next time! You have lost on your color.")
        print(f"You have lost: ${wtotal}")
        account = account + wtotal
        print(f"Your balence is now: ${account}")
        return account

# Starting variables
gambling = True
balence = 15000
bet_num_amount = 0
bet_color_amount = 0

# Main game loop
while gambling == True:

    # Checks if user has money to gamble with. If not, calls the user poor.
    if balence <= 0:
        print("We're sorry, but Roulette for Russians does not accept poor people.")
        print("Please come back when you have more money.")
        break
    else:
        pass
    
    # Starts game and displays balence
    start_game(balence)

    # Asks user for number betting option
    while True:
        try:
            bet_num = int(input("\nPlease bet on a number (0-36) [Enter '444' for no option]: "))
            if bet_num >= 0 and bet_num <= 36 or bet_num == 444:
                number_bet = betting_option_num(bet_num)
                break
            else:
                print("Please enter a number between 0 and 36, or 444 for no option.")
                continue
        except ValueError:
            print("ERROR : Please enter the correct values")
            continue

    # Asks user for color betting option
    while True:
        try:
            bet_color = input("Please bet on a color (red/black) [Enter 'n' for no option]: ")
            bet_color = bet_color.lower().strip()
            if bet_color == 'red' or bet_color == 'black' or bet_color == 'n':
                color_bet = betting_option_color(bet_color)
                break
            else:
                continue
        except ValueError:
            print("ERROR : Please enter the correct values")
            continue

    # Checks that user is betting at least on either a color or number    
    while True:
            bet_check = betting_option_check(number_bet, color_bet)

            if bet_check == False:
                print("\nPlease place a bet on either a number or a color.")
                continue
            else:
                break

    # Asks user to place bet amount if betting on a number
    while True:
        try:
            if number_bet == True:
                bet_num_amount = int(input(f"\nPlace your bets! How much are you betting on {bet_num}: "))
                if bet_num_amount > balence:
                    print(f"Please enter a number less than or equal to: ${balence}")
                    continue
                elif bet_num <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                else:
                    print("Bet accepted!")
                    break
            else:
                break
        except ValueError:
            print("ERROR : Please input a valid number")
            continue

    # Asks user to place bet amount if betting on a color
    while True:
        try:
            if color_bet == True:
                bet_color_amount = int(input(f"\nPlace your bets! How much are you betting on {bet_color}: "))
                if bet_color_amount > balence:
                    print(f"Please input a number less than or equal to: ${balence}")
                    continue
                elif bet_color_amount <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                else:
                    print("Bet accepted!")
                    break
            else:
                break
        except ValueError:
            print("ERROR : Please input a valid number")
            continue

    # Generates winning number and color
    r_num, r_color = random.choice(list(table.items()))

    # Asks for user input, simulates rolling of roulette
    while True:
        try:        
            roll = input("Are you ready to bet it all? (y/n): ")
            if roll.lower().strip() == 'y':
                rolling(r_num, r_color)
                break
            elif roll.lower().strip() == 'n':
                print("There\'s no going back! BET IT ALL!")
                continue
            else:
                print("Please enter 'y' or 'n'")
                continue
        except ValueError:
            print("ERROR : Please enter 'y' or 'n'")
            continue

    # Calculates which win-lose outcome
    win_con = winner(r_num, r_color, bet_num, bet_color, number_bet, color_bet)

    # Calculates winnings
    win_total = win_lose_value(win_con, bet_num_amount, bet_color_amount)

    # Displays win-loss and stores new balence
    balence = announcement(win_con, win_total, balence)

    # Asks user is they want to gamble again, terminates loop if not
    while True:
        try:    
            play_again = input("Care to wager again? (y/n): ")
            if play_again.lower() == 'y':
                print("")
                break
            elif play_again.lower() == 'n':
                print("\nCome again real soon!\n99% of gamblers quit before they hit it big!")
                gambling = False
                break
            else:
                print("\nERROR : Please input 'y' or 'n': ")
                continue
        except ValueError:
            play_again = input("\nERROR : Please input 'y' or 'n': ")
            continue

