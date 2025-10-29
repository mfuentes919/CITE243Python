"""
===========================================================
Program Name: ingredients_db.py
Author: Matthew Fuentes
Date: 10/22/25
Description:
    This program performs a database creation, and then asks for user input.
    It is designed to add meals and their ingredients to a database, which is then displayed.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import sqlite3

# Creates database called meal_ingredients and creates two tables for meals and ingredients within
conn = sqlite3.connect('meal_ingredients.db', isolation_level=None)
cursor = conn.cursor()
conn.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals (rowdid))')

conn.commit()

# Main loop for program
while True:
    # Asks for user input of meal and its ingredients
    # TO CLEAR TABLES: enter 'refresh'
    ming = input("> ").strip()

    # Checks user input
    if ming.lower() == 'quit':
        print("See you later!")
        break
    
    elif ming.lower() == 'refresh':
        cursor.execute('SELECT * FROM meals').fetchall()
        cursor.execute('DELETE FROM meals')
        cursor.execute('SELECT * FROM ingredients').fetchall()
        cursor.execute('DELETE FROM ingredients')

    elif ':' in ming:
        
        # Seperates input to put into different tables
        meal, ingred = ming.split(':', 1)
        ingredients = [i.strip() for i in ingred.split(',') if i.strip()]
        
        # Insert meal amd ingredient values into tables
        if meal.strip() and ingredients:
            cursor.execute('INSERT INTO meals (name) VALUES (?)', (meal,))
            meal_id = cursor.lastrowid
            for ing in ingredients:
                cursor.execute('INSERT INTO ingredients (name, meal_id) VALUES (?, ?)', (ing.strip(), meal_id))
            conn.commit()
            print(f"Meal added: {meal}")

    else:
        # Lists ingredients found in meals, or meals that use ingredients.
        cursor.execute('SELECT rowid FROM meals WHERE name = ?', (ming,))
        row = cursor.fetchone()
        if not row:
            cursor.execute('SELECT DISTINCT meals.name FROM meals JOIN ingredients ON meals.rowid = ingredients.meal_id WHERE ingredients.name = ?', (ming,))
            meals = cursor.fetchall()
            if meals:
                print(f"Meals that use {ming}:")
                for m in meals:
                    print(f"    {m[0]}")
                continue
            else:
                print("No Match Found")
                continue
        else:
            print(f"Ingredients of {ming}:")
        meal_id = row[0]
        cursor.execute('SELECT name FROM ingredients WHERE meal_id = ?', (meal_id,))
        ingredients = cursor.fetchall()
        for ing in ingredients:
            print(f"    {ing[0]}")

# Clean up after program runs | COMMENT OUT AFTER PROGRAM FINISHED
#cursor.execute('SELECT * FROM meals').fetchall()
#cursor.execute('DELETE FROM meals')
#cursor.execute('SELECT * FROM ingredients').fetchall()
#cursor.execute('DELETE FROM ingredients')