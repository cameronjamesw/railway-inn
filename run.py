import gspread
from google.oauth2.service_account import Credentials
import os
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('railway_inn_employees')

employee_page = SHEET.worksheet('Employees')

data = employee_page.get_all_values()
row = data[-1]

class Employee():

    def __init__(self, first_name, last_name, employee_no, contract_hours, wage):
       self.first_name = first_name
       self.last_name = last_name
       self.employee_no = employee_no
       self.contract_hours = contract_hours
       self.wage = wage
    
    def printList(self):
        list = [self.first_name, self.last_name, self.employee_no, self.contract_hours, self.wage]
        print(list)

Hannah = Employee('Hannah', 'Obrien', 2, 40, '£15')


def get_user_option():
    """
    This function displays the options to the user and then
    asks the user to enter a letter corresponding to the options
    """
    print(Fore.YELLOW + 'Welcome to the Railway Inn Employee Portal \n')

    while True:
        print(Style.RESET_ALL + 'Please enter a letter corresponding to an option:')
        print('A - Create a new employee')
        print('B - Update an existing employee')
        print('C - Delete an exisitng employee')
        print('D - Calculate wages of an exisitng employee\n')

        user_input = input("Enter an option: ")
        user_input = user_input.upper()

        if validate_user_option_input(user_input):
            print('Getting the desired option... \n')    
            display_user_option(user_input)
            break

def validate_user_option_input(inp):
    """
    This function checks the option input that the user has 
    input, if it is not a letter between A - D then it returns
    and error
    """
    try:
        if inp not in ['A', 'B', 'C', 'D']:
            raise ValueError(
                f"Please enter a value of A, B, C or D. You entered {inp}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again\n")
        return False
    return True

def display_user_option(inp):
    """
    This function takes the user's input and displays
    the relative option in the terminal
    """

    if inp == 'A':
        display_create_employee()
    elif inp == 'B':
        print('Selected Update Employee\n')
        display_update_employee()
    elif inp == 'C':
        print('You chose C')
    elif inp == 'D':
        print('You chose D')

def display_create_employee():
    new_employee = []
    class_employee = []

    print('Create Employee Selected\n')
    while True:
        first_name = input("Please enter the first name of your new employee: ")
        new_employee.append(first_name)
        class_employee.append(first_name)

        if letter_validation(first_name):
            break

    while True:
        last_name = input("Please enter the last name of your new employee: ")
        new_employee.append(last_name)
        class_employee.append(last_name)

        if letter_validation(last_name):
            break

    while True:
        employee_no = input("Please enter the employee number: ")

        if numeric_validation(employee_no):
            class_employee.append(employee_no)
            employee_no = f"#{employee_no}"
            new_employee.append(employee_no)
            break

    while True:
        contract_hours = input("Please enter the contracted hours of your new employee: ")
        new_employee.append(contract_hours)
        class_employee.append(contract_hours)

        if numeric_validation(contract_hours):
            break

    while True:
        wage = input("Please enter the wage of your new employee: ")
        
        if numeric_validation(wage):
            class_employee.append(wage)
            wage = f"£{wage}"
            new_employee.append(wage)
            break

    print(f"\nFirst Name = {first_name}")
    print(f"Last Name = {last_name}")
    print(f"Employee No. = {employee_no}")
    print(f"Contracted Hours = {contract_hours} hours per week")
    print(f"Wage = {wage}")

    employee_class_list = convert_to_class_list(class_employee)
    full_name = f"{first_name} {last_name}"

    class_push(employee_class_list, full_name)

    while True:    
        if user_check(new_employee):
            break

def letter_validation(inp):
    """
    This function checks to see if the values 
    entered are alphabetic or not
    """
    try:
        if inp.isalpha() != True:
            raise ValueError (
                f"Field must only contain characters [A-Z] or [a-z]. You entered {inp}."
        )
    except ValueError as e:
        print(f"\nInvalid data {e}. Please try again\n")
        return False
    return True

def numeric_validation(inp):
    """
    This function checks to see if the values
    entered are numeric or not
    """
    try:
        if inp.isnumeric() != True:
            raise ValueError (
                f"Field must only contain characters [0-9]. You entered {inp}."
            )
    except ValueError as e:
        print(f"\nInvalid Data {e}. Please try again\n")
        return False
    return True

def class_push(data, employee_name):
    """
    This function takes a parameter and
    pushes it into the Employee class
    """
    employee_name = Employee(data[0], data[1], data[2], data[3], data[4])

def convert_to_class_list(list):
    """
    This function takes a list containing strings, and
    converts the items to the relevent data types.
    """
    new_list = []
    for item in list:
        if item.isalpha() != True:
            item = int(item)
            new_list.append(item)
        elif item.isnumeric() != True:
            item = str(item)
            new_list.append(item)
    return new_list

def user_check(data):
    """
    This function allows the user to check if
    the inputs they have entered are correct
    """
    user_check = input("\nIs the data you entered correct? (Y/N): ")
    user_check = user_check.upper()
    letter_validation(user_check)

    try:
        if user_check == 'Y':
            print('You answered yes')
            push_new_employee(data)
            return True
        elif user_check == 'N':
            print('You answered no')
            os.system('cls||clear')
            display_create_employee()
            pass
            return True
    except ValueError as e:
        print(f"Invalid Data {e}, you entered {user_check}")
        return False

def push_new_employee(employee_data):
    """
    This function takes the newly created employee
    and pushes it to the Google Sheet
    """
    print('\nUpdating employee database...\n')
    employee_page.append_row(employee_data)
    print('Employee database updated!\n')

    main_menu_input()

def main_menu_input():
    while True:
        user_input = input('Return to the main menu? (Y/N): \n')

        if return_to_main_menu(user_input):
            break

def return_to_main_menu(inp):
    """
    This function allows the user to return
    to the main menu
    """
    inp = inp.upper()

    try:
        if inp == 'Y':
            print('You answered yes')
            os.system('cls||clear')
            get_user_option()
            return True
        elif inp == 'N':
            confirm = input('Are you sure you want to exit the application? (Y/N): ')
            confirm = confirm.upper()
            try:
                if confirm == 'Y':
                    os.system('cls||clear')
                elif confirm == 'N':
                    confirm = 'Y'
                    return_to_main_menu(confirm)
            except ValueError as e:
                print(f"Invalid Data {e}, you entered {inp}")
                return False

            return True
    except ValueError as e:
        print(f"Invalid Data {e}, you entered {inp}")
        return False

def display_update_employee():
    """
    This function displays the update employee option
    to the user. It gets the two inputs of the first and 
    last name.
    """
    print('\nPlease enter the first name of the employee you wish to update..')
    f_name = input('Employee First Name: ')
    print('\nPlease enter the last name of the employee you wish to update..')
    l_name = input('Employee Last Name: ')

    concat_input = concatonate_inputs(f_name, l_name)
    check_name(concat_input)
    

def concatonate_inputs(input1, input2):
    """
    This function takes the two inputs from update_employees
    and concatenates them together into one string. Returns
    a full name.
    """
    full_name = f"{input1} {input2}"
    return full_name

def check_name(name):
    """
    This function takes the full name from concatenate_inputs function,
    and checks to see if the name exists in the database.
    """
    
    column_1 = employee_page.col_values(1)
    column_slice = slice(1, -1)
    first_name_column = column_1[column_slice]
    column_2 = employee_page.col_values(2)
    second_name_column = column_2[column_slice]

    database_names = []
    for fname, lname in zip(first_name_column, second_name_column):
        full_name = f"{fname} {lname}"
        database_names.append(full_name)

    try:
        if name in database_names:
            print(f'You have entered {name}')
        else:
            raise ValueError (
                f'{name} does not exist in the Employee Database'
            )
    except ValueError as e:
        print(f'\nInvalid data {e}. Please try another name.')
    
   
    if name not in database_names:
        
        while True:
            if try_again():
                break
        

def try_again():
    """
    This function prints the try again text to
    the terminal. Anything other than "Y" or "N" raises
    an error to the terminal. 
    """
    user_input = input(f"Do you want to try again? (Y/N): ")
    user_input = user_input.upper()

    try:    
        if user_input == 'Y':
            display_update_employee()
            return True
        elif user_input == 'N':
            main_menu_input()
            return True
        else:
            raise ValueError (
                f'Please enter a value of "Y" or "N", you entered {user_input}'
                )
    except ValueError as e:
        print(f'Invalid input: {e}. Please try again')
        return False
            
    
get_user_option()