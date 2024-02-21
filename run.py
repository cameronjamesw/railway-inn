import gspread
from google.oauth2.service_account import Credentials

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
    print('Welcome to the Railway Inn Employee Portal \n')

    while True:
        print('Please enter a letter corresponding to an option:')
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
        print('You chose B')
    elif inp == 'C':
        print('You chose C')
    elif inp == 'D':
        print('You chose D')

def display_create_employee():
    new_employee = []

    print('Create Employee Selected\n')
    first_name = input("Please enter the first name of your new employee: ")
    new_employee.append(first_name)
    letter_validation(first_name)

    last_name = input("Please enter the last name of your new employee: ")
    new_employee.append(last_name)
    letter_validation(last_name)

    employee_no = input("Please enter the employee number: ")
    new_employee.append(employee_no)

    contract_hours = input("Please enter the contracted hours of your new employee: ")
    new_employee.append(contract_hours)

    wage = input("Please enter the wage of your new employee: ")
    new_employee.append(wage)

    print(f"\nFirst Name = {first_name}")
    print(f"Last Name = {last_name}")
    print(f"Employee No. = #{employee_no}")
    print(f"Contracted Hours = {contract_hours} hours per week")
    print(f"Wage = £{wage}")

def letter_validation(inp):
    """
    This functions chekcs to see if the values 
    entered are alphabetic or not
    """
    try:
        raise ValueError (
            f"Field must only contain [A-Z] or [a-z]. You entered {inp}."
        )
    except ValueError as e:
        print(f"\nInvalid data {e}. Please try again\n")

get_user_option()