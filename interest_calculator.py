from math import ceil
from budget import left_from_income
from prettytable import PrettyTable
from datetime import date
from colorama import init
from colorama import Fore
init()


def interest_heading():
    # Heading for app
    print(Fore.WHITE)
    x = PrettyTable()
    x.field_names = ["Your Interest Calculator"]
    x.add_row(["This will calculate 10% of your income"])
    x.add_row(["It will then multiply it into a year amount"])
    x.add_row(["And also show you how much you can invest"])
    x.add_row(["And also show you how long to become a millionaire"])
    print(x)


interest_heading()


def interested_income():
    """
    This function will find 20% and 10% of the income
    that is recommended amount for investing
    We have to remember investing can carry risk to the user
    """
    print(Fore.GREEN)
    print("Recommended 20% of your income for savings and investing.")
    print("I will take 10% of your remaining income after your your budgeted")
    ten_percent_of_income = (10/100) * left_from_income  # get a % of income
    year_amount_from_income = ten_percent_of_income * 48
    # The year amount of the 10%
    twenty_percent_of_income = (20/100) * left_from_income
    year_amount_of_twenty_percent = twenty_percent_of_income * 48
    ten_percent_of_income = round(ten_percent_of_income, 2)
    # To round the answers to 2 decmial places
    year_amount_from_income = round(year_amount_from_income, 2)
    twenty_percent_of_income = round(twenty_percent_of_income, 2)
    year_amount_of_twenty_percent = round(year_amount_of_twenty_percent, 2)
    y = PrettyTable()
    z = PrettyTable()
    y.field_names = ["20% of Income", "Annual 20%"]
    y.add_row([twenty_percent_of_income, year_amount_of_twenty_percent])
    z.field_names = ["10% of Income", "Annual 10%"]
    z.add_row([ten_percent_of_income,  year_amount_from_income])
    print(y)
    print(z)


interested_income()

"""
Calculate interest from investing. Average etf and  Mutual funds are 8% a year.
We take an amount the user wants to invest and add 8% until
they make a million and tell them how long it takes
"""

print(Fore.WHITE)
print("Principal is the total amount of money you would like to invest")
print("Average rate is 8% from ETF(exchange-traded fund) and Mutual Funds")
print("Remember all investments carry some degree of risk.")
print("Stocks, bonds, mutual funds and exchange-traded funds can lose value")


def interest():
    # the amount of money initially invested
    print(Fore.WHITE)
    global principal
    while True:
        principal = float(input('Enter the principal amount for the year: '))
        try:
            if principal == "":
                raise ValueError('empty value')
        except ValueError as e:
            print(e)
            print('Enter a valid number, please')
            continue
        if principal == float():
            break
        else:
            print('Valid Thank you')
            break
    print("Average rate is 8% a year")
    rate = float(8)
    global time
    while True:
        time = float(input('Enter the time in years: '))
        try:
            if time == "":
                raise ValueError('empty Value')
        except ValueError as e:
            print(e)
            print('Enter a valid value, please')
            continue
        if time == float():
            break
        else:
            break
    global simple
    simple = (principal * rate * time / 100.00)     # interest formula
    global total_simple
    total_simple = simple + principal
    print(Fore.MAGENTA)
    print(f"Simple Interest value over the years. = {simple}")
    total_amount_invested = 1000000  # set to 1 million
    global year
    year = (total_amount_invested) / (principal * rate / 100)
    roundedYear = ceil(year)
    current_year = date.today().year
    global date_year
    date_year = current_year + roundedYear
    print(f"After {year} years your money will be {total_amount_invested}")
    print(f"That is in approximately the year {date_year}")


interest()


def interest_calculator_summary():
    # Gets a pretty table of summary of interest
    x = PrettyTable()
    x.field_names = [
        "Invested", "Time Invested", "Value of Interest", "Total Value"
        ]
    x.add_row([principal, time, simple, total_simple])
    print(x)
    z = PrettyTable()
    z.field_names = ["Total of Investment"]
    z.add_row([total_simple])
    y = PrettyTable()
    y.field_names = ["Years to be a Millionaire", "Year will be"]
    y.add_row([year, date_year])
    print(y)
