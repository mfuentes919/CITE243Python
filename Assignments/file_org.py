"""
===========================================================
Program Name: file_org.py
Author: Matthew Fuentes
Date: 9/29/25
Description:
    This program performs the task of finding all text files within a folder and copies them to another.
    It is designed to automate organizing file types.
    
Usage:
    Run the script using Python 3.13 Ensure all dependencies
    are installed before execution.

===========================================================
"""
# Imports functions
from pathlib import Path
import shutil, os

# Creates variable and library folder to move text documents to
h = Path.home()
(h / 'library').mkdir(exist_ok=True)

# Creates test folder from which all files will be copied from.
(h / 'test').mkdir(exist_ok=True)
(h / 'test/point').mkdir(exist_ok=True)
(h / 'test/port').mkdir(exist_ok=True)
for f in ['test/file1.txt', 'test/point/win.txt', 'test/port/https.txt', 'test/port/http.txt',]:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('Hello')

# Finds all files with the extension 'txt' in the user folder and copies them to the library folder.
for root, dirs, filenames in os.walk(h / 'test'):
    for filename in filenames:
        if filename.endswith(".txt"):
            file_path = os.path.join(root, filename)
            shutil.copy(file_path, h / 'library')
