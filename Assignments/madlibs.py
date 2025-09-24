"""
===========================================================
Program Name:   madlibs.py
Author:         Matthew Fuentes
Date:           9-24-2025
Description:
    This program creates a mablibs text file, finds all the uppercase words, and asks the user to replace them with another adjective/noun/verb of their choice.
    It is designed to create the madlibs experience within python.
    
Usage:
    Run the script using Python 3.13.7 Ensure all dependencies
    are installed before execution.

===========================================================
"""
import re
from pathlib import Path

# Creates madlad file if it doesn't exist, writes base madlibs prompt, and closes file
with open('madlad.txt', 'w', encoding='UTF-8') as madlad:
    madlad.write(f"The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.")

# Stores content of madlad.txt in var, prints it for user to see
with open('madlad.txt', encoding='UTF-8') as madlad:
    content = madlad.read()
print(content)

# Creates a regex that finds all uppercase words and stores them in a var
content_regex = re.compile(r'\w[A-Z]+')
hold = content_regex.findall(content)

# Creates empty list and fills with found uppercase words
place_hold = []
for i in hold:
    place_hold.append(i)

# Goes through values in place_hold and asks user to replace them with their own input
for i in range(len(place_hold)):
    print(f"Enter a {place_hold[i].lower()}:")
    replace = input()
    place_hold[i] = replace

# Replaces previous test within file with new descriptive words and outputs to user
with open('madlad.txt', 'w', encoding='UTF-8') as madlad:
    madlad.write(f"The {place_hold[0]} panda walked to the {place_hold[1]} and then {place_hold[2]}. A nearby {place_hold[3]} was unaffected by these events.")
with open('madlad.txt', encoding='UTF-8') as madlad:
    content = madlad.read()
print(content)