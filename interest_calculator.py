from math import ceil
from budget import left_from_income
from datetime import date
from colorama import init
from colorama import Fore
init()

"""
Calculate interest from investing. Average etf and MTF are 8% a year.
We take an amount the user wants to invest and add 8% until 
they make a million and tell them how long it takes 
"""
print("Recommended 20% of your income for savings and investing.")
print("I will take 10% of your remaining income after your your budgeted")

ten_percent_of_income = (10/100) * left_from_income # get a % of income
print(ten_percent_of_income)

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
    # total_amount_invested = Simple + principal
    # print(f"Total amount = {total_amount_invested}")
    
    # total years 
    total_amount_invested = 1000000 # set to 1 million
    year = (total_amount_invested) / (principal * rate / 100)

    roundedYear = ceil(year)
    current_year = date.today().year
    date_year = current_year + roundedYear

    print(f"After {year} years your money will be {total_amount_invested } in approximately the year {date_year}")
    
    """ while total_amount_invested <= 10000:
        total_amount_invested += new_simple       
        year = year + 1
        
        print(f"After {str(time)} years your money will be {total_amount_invested } in the year{year}")"""
        
interest()
