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

print('Welcome to the Railway Inn Employee Portal \n')
print('Please enter a letter corresponding to an option:')
print('A - Create a new employee')
print('B - Update an existing employee')
print('C - Delete an exisitng employee')
print('D - Calculate wages of an exisitng employee\n')

user_input = input("Enter an option: ")
print(user_input)