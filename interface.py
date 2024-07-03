# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Computers.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('\nWelcome to the Computers database\n\n'
                        'Type the number for the query that you would like to see.:\n\n' 
                        'A: View all data\n'
                        'B: Brand, model, year, price\n'
                        'C: Model, price\n'
                        'D: Model, RAM, speed\n'
                        'E: Model, year\n'
                        'F: Type, brand, country\n'
                        'G: Year, model, speed (ordered by year ASC)\n'
                        'H: Type, model, speed, RAM, year, price (ordered by price ASC)\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All data')
    elif menu_choice == 'B':
        print_query('Brand, model, year, price')
    elif menu_choice == 'C':
        print_query('Model, price')
    elif menu_choice == 'D':
        print_query('Model, RAM, speed')
    elif menu_choice == 'E':
        print_query('Model, year')
    elif menu_choice == 'F':
        print_query('Type, brand, country')
    elif menu_choice == 'G':
        print_query('Year, model, speed')
    elif menu_choice == 'H':
        print_query('Type, model, speed, RAM, year, price')