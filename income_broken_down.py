from confirm_user import available
from prettytable import PrettyTable
from colorama import Fore

week_income = available
fortnight_income = 0
month_income = 0
year_income = 0
"""
This will calculate the income of the user,
from there weekly to monthly to yearly income
This will help with what there budgets.
48 weeks in a working year to equal 12 months pay
"""


def week_income_to_fortnight(week_income):
    # Gets the weekly income to your income every 2 weeks
    global fortnight_income
    fortnight_income = week_income * 2
    return fortnight_income

week_income_to_fortnight(week_income)


def week_income_to_monthly(week_income):
    # Gets the weekly income to your income every 4 weeks for a month
    global month_income
    month_income = week_income * 4
    return month_income

week_income_to_monthly(week_income)


def week_income_to_year(week_income):
    """
    Gets the weekly income to your income every 48 weeks
    for a year as 52 changes the result for the monthly
    """
    global year_income
    year_income = week_income * 48
    return year_income

week_income_to_year(week_income)


def month_income_to_week(month_income):
    # Gets the monthly income to your weekly income
    week_income = month_income / 4
    return

month_income_to_week(month_income)


def month_income_to_year(month_income):
    # Gets the monthly income to your yearly income
    year_income = month_income * 12
    return

month_income_to_year(month_income)


def year_income_to_month(year_income):
    # Gets the yearly income to your monthly income
    month_income = year_income / 12
    return

year_income_to_month(year_income)


def year_income_to_week(year_income):
    # Gets the yearly income to your weekly income
    week_income = year_income / 48
    return

year_income_to_week(year_income)


def summary():  # Gets a pretty table of summary of your income
    x = PrettyTable()
    x.field_names = ["Week", "Fortnight", "Month", "Year"]
    x.add_row([week_income, fortnight_income, month_income, year_income])
    print(x)

print(Fore.CYAN)
summary()
