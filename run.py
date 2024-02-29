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
tax_page = SHEET.worksheet('Taxes')

data = employee_page.get_all_values()
row = data[-1]

column_1 = employee_page.col_values(1)
column_slice = slice(1, -1)
first_name_column = column_1[column_slice]
column_2 = employee_page.col_values(2)
second_name_column = column_2[column_slice]

def get_user_option():
    """
    This function displays the options to the user and then
    asks the user to enter a letter corresponding to the options
    """
    print(Fore.YELLOW + 'Welcome to the Railway Inn Employee Portal \n')

    while True:
        print(Fore.WHITE + 'Please enter a letter corresponding to an option:')
        print(Fore.WHITE + 'A - Create a new employee')
        print(Fore.WHITE + 'B - Display existing employee')
        print(Fore.WHITE + 'C - Calculate wages of an exisitng employee\n')

        user_input = input("Enter an option: \n")
        user_input = user_input.upper()

        if validate_user_option_input(user_input):
            print( Fore.GREEN +'Getting the desired option... \n')    
            display_user_option(user_input)
            break

def validate_user_option_input(inp):
    """
    This function checks the option input that the user has 
    input, if it is not a letter between A - D then it returns
    and error
    """
    try:
        if inp not in ['A', 'B', 'C']:
            raise ValueError(
                Fore.RED + f"Please enter a value of A, B or C. You entered {inp}"
            )
    except ValueError as e:
        print( Fore.RED + f"Invalid data: {e}. Please try again\n")
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
        print('Selected Display Employee\n')
        display_employee()
    elif inp == 'C':
        get_employee_name()

def display_create_employee():
    new_employee = []

    print('Create Employee Selected\n')
    while True:
        first_name = input(Fore.WHITE + "\nPlease enter the first name of your new employee: \n")
        new_employee.append(first_name)

        if letter_validation(first_name):
            break

    while True:
        last_name = input(Fore.WHITE + "\nPlease enter the last name of your new employee: \n")
        new_employee.append(last_name)

        if letter_validation(last_name):
            break

    while True:
        employee_no = input(Fore.WHITE + "\nPlease enter the employee number: \n")

        if numeric_validation(employee_no):
            employee_no = f"#{employee_no}"
            new_employee.append(employee_no)
            break

    while True:
        contract_hours = input(Fore.WHITE + "\nPlease enter the contracted hours of your new employee: \n")
        new_employee.append(contract_hours)

        if numeric_validation(contract_hours):
            break

    while True:
        wage = input(Fore.WHITE + "\nPlease enter the wage of your new employee: \n")
        
        if numeric_validation(wage):
            wage = f"{wage}"
            new_employee.append(wage)
            break

    print(f"\nFirst Name = {first_name}")
    print(f"Last Name = {last_name}")
    print(f"Employee No. = {employee_no}")
    print(f"Contracted Hours = {contract_hours} hours per week")
    print(f"Wage = {wage}")

    full_name = f"{first_name} {last_name}"

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
                Fore.RED + f"Field must only contain characters [A-Z] or [a-z]. You entered {inp}."
        )
    except ValueError as e:
        print(Fore.RED + f"\nInvalid data {e}. Please try again\n")
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
                Fore.RED + f"Field must only contain characters [0-9]. You entered {inp}."
            )
    except ValueError as e:
        print(Fore.RED + f"\nInvalid Data {e}. Please try again\n")
        return False
    return True

def user_check(data):
    """
    This function allows the user to check if
    the inputs they have entered are correct
    """
    user_check = input("\nIs the data you entered correct? (Y/N): \n")
    user_check = user_check.upper()
    letter_validation(user_check)

    try:
        if user_check == 'Y':
            print(Fore.GREEN + 'You answered yes')
            push_new_employee(data)
            return True
        elif user_check == 'N':
            print(Fore.GREEN + 'You answered no')
            os.system('cls||clear')
            display_create_employee()
            pass
            return True
    except ValueError as e:
        print(Fore.RED + f"Invalid Data {e}, you entered {user_check}")
        return False

def push_new_employee(employee_data):
    """
    This function takes the newly created employee
    and pushes it to the Google Sheet
    """
    print(Fore.GREEN + '\nUpdating employee database...\n')
    employee_page.append_row(employee_data)
    print(Fore.GREEN + 'Employee database updated!\n')

    main_menu_input()

def main_menu_input():
    while True:
        user_input = input(Fore.YELLOW + '\nReturn to the main menu? (Y/N): \n')

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
            print(Fore.GREEN + 'You answered yes')
            os.system('cls||clear')
            get_user_option()
            return True
        elif inp == 'N':
            confirm = input(Fore.YELLOW + 'Are you sure you want to exit the application? (Y/N): \n')
            confirm = confirm.upper()
            try:
                if confirm == 'Y':
                    os.system('cls||clear')
                    return True

                elif confirm == 'N':
                    main_menu_input()
                    return False
                else:
                    raise ValueError (
                    Fore.RED + f'Please enter a value of "Y" or "N", you entered {confirm}'
                )
            except ValueError as e:
                print(Fore.RED + f"Invalid Data {e}, please try again")
                return False
        else:
            raise ValueError (
                Fore.RED + f'Please enter a value of "Y" or "N", you entered {inp}'
            )
            return True
    except ValueError as e:
        print(Fore.RED + f"Invalid Data: {e}, please try again.")
        return False

def display_employee():
    """
    This function displays the update employee option
    to the user. It gets the two inputs of the first and 
    last name.
    """
    while True:
        print(Fore.WHITE + '\nPlease enter the first name of the employee you wish to display..')
        f_name = input('Employee First Name: \n')
        f_name = f_name.capitalize()
        if letter_validation(f_name):
            break

    while True:
        print(Fore.WHITE + '\nPlease enter the last name of the employee you wish to display..')
        l_name = input('Employee Last Name: \n')
        l_name = l_name.capitalize()
        if letter_validation(l_name):
            break

    display_variable = 'display'

    concat_input = concatonate_inputs(f_name, l_name)
    if check_name(concat_input, l_name, display_variable):
        main_menu_input()

def concatonate_inputs(input1, input2):
    """
    This function takes the two inputs from update_employees
    and concatenates them together into one string. Returns
    a full name.
    """
    full_name = f"{input1} {input2}"
    return full_name

def check_name(name, l_name, variable):
    """
    This function takes the full name from concatenate_inputs function,
    and checks to see if the name exists in the database.
    """
    database_names = []
    for fname, lname in zip(first_name_column, second_name_column):
        full_name = f"{fname} {lname}"
        database_names.append(full_name)

    try:
        if name in database_names:
            display_employee_details(l_name)
            return True
    
        else:
            raise ValueError (
                Fore.RED + f'{name} does not exist in the Employee Database'
            )
            return False
    except ValueError as e:
        print(Fore.RED + f'\nInvalid data {e}. Please try another name.')
        
        
    
   
    if name not in database_names:
        
        while True:
            if try_again(variable):
                break    

def try_again(variable):
    """
    This function prints the try again text to
    the terminal. Anything other than "Y" or "N" raises
    an error to the terminal. 
    """
    user_input = input(Fore.YELLOW + f"\nDo you want to try again? (Y/N): \n")
    user_input = user_input.upper()

    try:    
        if user_input == 'Y':
            if variable == 'display':
                display_employee()
                return True
            elif variable == 'calculate':
                get_employee_name()
        elif user_input == 'N':
            main_menu_input()
            return True
        else:
            raise ValueError (
                Fore.RED + f'Please enter a value of "Y" or "N", you entered {user_input}'
                )
    except ValueError as e:
        print(Fore.RED + f'Invalid input: {e}. Please try again')
        return False

def display_employee_details(lname):
    """
    This function takes the perameter of the last name and uses it
    to locate the employee in the database and then display the
    relevent employee details to the console.
    """
    
    try:
        if check_name:

            index = column_2.index(lname)
            user_data = data[index]

            print(f'\nFirst Name = {user_data[0]}')
            print(f'Last Name = {user_data[1]}')
            print(f'Employee Number = {user_data[2]}')
            print(f'Contracted Hours = {user_data[3]} hours p/wk')
            print(f'Wage = {user_data[4]} p/hr')
        else:
            raise ValueError (
                Fore.RED + f'{lname} is not in the employee database'
            )
    except ValueError as e:
        print(Fore.RED + f'Invalid name: {e}. Please enter another name')

def get_employee_name():
    """
    This function asks the user to enter the employee first name
    and last name and will then check it against the database
    through calling the check name function. This will also
    concatenate the two inputs together. 
    """
    while True:
        print(Fore.WHITE + '\nPlease enter the first name of the employee..')
        f_name = input('Employee First Name: \n')
        f_name = f_name.capitalize()
        if letter_validation(f_name):
            break

    while True:
        print(Fore.WHITE + '\nPlease enter the last name of the employee..')
        l_name = input('Employee Last Name: \n')
        l_name = l_name.capitalize()
        if letter_validation(l_name):
            break

    calculate_variable = 'calculate'

    concat_input = concatonate_inputs(f_name, l_name)
    
    if check_last_name(l_name, concat_input):
        check_name(concat_input, l_name, calculate_variable)
        while True:
             if get_employee_hours(concat_input, l_name, f_name):
                break
    else:
        try_again(calculate_variable)

def check_last_name(l_name, name):
    try:
        if l_name in column_2:
            return True
        else:
            raise ValueError (
                print(Fore.RED + f'{name} is not in the Employee Database')
            )
            return False 
    except ValueError as e:
        (Fore.RED + f'Invalid Data: {e}, please try again.')

def get_wage(lname):
    """
    This function will specifically get the wage of
    the employee who's name has been passed as the parameter.
    This function returns the result as wage.
    """
    index = column_2.index(lname)
    user_data = data[index]
    wage = user_data[4]
    return wage

def get_hours(lname):
    """
    This function will specifically get the contracted hours of
    the employee who's name has been passed as the parameter.
    This function returns the result as hours.
    """
    index = column_2.index(lname)
    user_data = data[index]
    hours = user_data[3]
    return hours

def get_employee_hours(name, lname, fname):
    """
    This function will ask the user if the employee worked their
    contracted hours, and if not will display the user an input
    to alter the hours worked for the month.
    """
    hours = get_hours(lname)
    wage = get_wage(lname)
    hours = int(hours)

    while True:
        print(Fore.WHITE + f'\n{name} is contracted to work {hours} hours per week ({hours * 4} hours per month).')
        user_input = input(f'Did {name} work their contracted hours? (Y/N): \n')
        user_input = user_input.upper()
        if letter_validation(user_input):
            break
    try:
        if user_input == 'Y':
            print(Fore.WHITE + f'\n{name} worked {hours} hours this pay period.')
            calculate_pay_before_tax(name, hours, wage, fname, lname)
            return True
        elif user_input == 'N':
            new_hours = input(f'How many total hours did {name} work: \n')
            new_hours = int(new_hours)
            print(Fore.WHITE + f'\n{name} worked {new_hours} hours this pay period.')
            calculate_pay_before_tax(name, new_hours, wage, fname, lname)
            return True
        else:
            raise ValueError (
                print(Fore.RED + f'Please enter a value of "Y" or "N", you entered {user_input}')
            )
            return False
    except ValueError as e:
        print(Fore.RED + f'Invalid input {e}. Please try again.')
        return False

def calculate_pay_before_tax(name, hours, wage, fname, lname):
    """
    This function takes 3 parameters of name, hours and wage. It will
    calculate the gross income of the employee without deducting
    taxes.
    """
    wage = int(wage)

    gross_income = wage * hours
    calculate_taxes(gross_income, name, fname, lname)

def calculate_taxes(pay, name, fname, lname):
    """
    This function takes two parameters of gross pay and name.
    This function will calculate the income tax and national insurance of
    the employee in question.
    """
    tax = 0.2
    national_insurance = 0.1

    national_insurance_tax = pay * national_insurance
    income_tax = tax * pay
    total_tax = national_insurance_tax + income_tax
    net_pay = pay - total_tax

    print(Fore.GREEN + f"{name}'s income details are as follows:")
    print(Fore.WHITE + f'First Name = {fname}')
    print(Fore.WHITE + f'Last Name = {lname}')
    print(Fore.WHITE + f'Gross Income = {pay}')
    print(Fore.WHITE + f'Net Income = {net_pay}')
    print(Fore.YELLOW + f'Income Tax = {income_tax}')
    print(Fore.YELLOW + f'NI Tax = {national_insurance_tax}')
    print(Fore.YELLOW + f'Total Tax = {total_tax}')

    taxes = add_tax_list(fname, lname, pay, net_pay, income_tax, national_insurance_tax, total_tax)

    user_input = input('\nDo you want to add this data to the Employee Database? (Y/N): \n')
    user_input = user_input.upper()

    while True:
        if append_validation(user_input, taxes):
            break

def append_validation(inp, taxes):

    try:
        if inp == 'Y':
            append_employee_tax(taxes)
            return True
        elif inp == 'N':
            main_menu_input()
            return True
        else:
            raise ValueError (
                Fore.RED + f'please enter a value of "Y" or "N", you have entered {inp}'
            )
            return False
    except ValueError as e:
            print(Fore.RED + f'Invalid Data: {e}. Please try again')
            return False

def add_tax_list(fname, lname, pay, net_pay, income_tax, national_insurance_tax, total_tax):
    employee_tax_info = []

    pay = f"£{pay:.2f}"
    net_pay = f"£{net_pay:.2f}"
    income_tax = f"£{income_tax:.2f}"
    national_insurance_tax = f"£{national_insurance_tax:.2f}"
    total_tax = f"£{total_tax:.2f}"

    employee_tax_info.append(fname)
    employee_tax_info.append(lname)
    employee_tax_info.append(pay)
    employee_tax_info.append(net_pay)
    employee_tax_info.append(income_tax)
    employee_tax_info.append(national_insurance_tax)
    employee_tax_info.append(total_tax)

    return employee_tax_info

def append_employee_tax(taxes):

    print(Fore.GREEN + 'Updating Employee Database..')

    tax_page.append_row(taxes)

    print(Fore.GREEN + '\nEmployee Database Updated!')

    main_menu_input()

get_user_option()
