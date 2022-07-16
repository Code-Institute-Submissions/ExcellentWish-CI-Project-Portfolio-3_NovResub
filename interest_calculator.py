from math import ceil
from budget import left_from_income
from prettytable import PrettyTable
from datetime import date
from colorama import init
from colorama import Fore
init()

def interest_heading():
    #Heading for app  
    print(FORE.WHITE)
    x = PrettyTable()
    x.field_names = ["Your Interest Calculator"]
    x.add_row(["This will calculate 10% of your income"])
    x.add_row(["It will then multiply it into a year amount"])
    x.add_row(["And also show you how much you can invest to become a millionaire"])
    print(x)

interest_heading()

"""
Calculate interest from investing. Average etf and MTF are 8% a year.
We take an amount the user wants to invest and add 8% until 
they make a million and tell them how long it takes 
"""
print(Fore.GREEN + "Recommended 20% of your income for savings and investing.")
print("I will take 10% of your remaining income after your your budgeted")

ten_percent_of_income = (10/100) * left_from_income # get a % of income
year_amount_from_income = ten_percent_of_income * 48 # The year amount of the 10%

print(f"10% of your income is = {ten_percent_of_income} ")
print(f"{year_amount_from_income} is equal to the annual amount of that 10%")


def interest():      
    # the amount of money initially invested
    print(Fore.WHITE)
    principal = float(input('Enter the principal: '))
    print("Average rate is 8% a year")
    rate = float(8)
    time = float(input('Enter the time in years: '))
    Simple = (principal * rate * time/ 100.00)     # interest formula
    print(Fore.MAGENTA)
    print(f"Simple Interest value over the years. = {Simple}")
    total_amount_invested = 1000000 # set to 1 million
    year = (total_amount_invested) / (principal * rate / 100)

    roundedYear = ceil(year)
    current_year = date.today().year
    date_year = current_year + roundedYear

    print(f"After {year} years your money will be {total_amount_invested } in approximately the year {date_year}")
    

interest()
