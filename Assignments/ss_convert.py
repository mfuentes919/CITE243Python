"""
===========================================================
Program Name: ss_convert.py
Author: Matthew Fuentes
Date: 10/20/25
Description:
    This program performs a spreadsheet upload to Google Sheets, and then downloads the same sheet in two other formats.
    It is designed to convert an uploaded spreadsheet to different file formats.
    
Usage:
    Run the script using Python 3.9.21. Ensure all dependencies
    are installed before execution. 

    Required: test_spreadsheet.xlsx file in folder where program is run.

===========================================================
"""

import ezsheets

# Convertor function
def convert_spreadsheet(spreadsheet):
    while True:
        try:
            choice = input("\nPlease enter which format you would like your spreadsheet in: Excel (XL), ODS, CSV, TSV, PDF, or HTML (Zip Files) ")

            choice = choice.lower().strip() # Sanitize

            if choice == 'xl':
                spreadsheet.downloadAsExcel()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            elif choice == 'ods':
                spreadsheet.downloadAsODS()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            elif choice == 'csv':
                spreadsheet.downloadAsCSV()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            elif choice == 'tsv':
                spreadsheet.downloadAsTSV()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            elif choice == 'pdf':
                spreadsheet.downloadAsPDF()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            elif choice == 'html':
                spreadsheet.downloadAsHTML()
                print(f"Your {choice.upper()} file has been downloaded!")
                break
            else:
                print("Please enter an acceptable value. Try again.")
                continue

        except ValueError:
            print("Please enter an acceptable value. Try again.")
            continue



# Test spreadsheet made in Libre Calc and placed in Scripts folder
ss = ezsheets.upload('test_spreadsheet.xlsx')

# Download spreadsheet in Excel format
while True:
    try:
        convert_spreadsheet(ss)

        again = input("Would you like to convert you spreadsheet to another format? (y/n): ")
        if again == 'y':
            continue
        elif again == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
            break
    except ValueError:
        print("Please enter 'y' or 'n'.")
        break