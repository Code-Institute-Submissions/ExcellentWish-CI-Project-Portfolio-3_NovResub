from income_broken_down import week_income
from prettytable import PrettyTable
from colorama import init
from colorama import Fore
init()

available = week_income
budgets = {}
expenditure = {}


def userInputBudget():
    print(Fore.WHITE)
    valid = False
    while not valid:
        try:
            budgetname = str(input('Enter the budget name: '))
            try:
                budgetAmount = float(input(
                    'Enter the amount for this budget:'))
                valid = True
            except ValueError as e:
                print(e)
                print('Enter a valid number, please')
            try:
                spendings = float(input(
                    'Enter the amount you have spent: '))
                valid = True
            except ValueError as e:
                print(e)
                print('Enter a valid number, please')
        except ValueError:
            print('Enter a valid number, please')
    add_budget(budgetname, budgetAmount)
    spend(budgetname, spendings)


def add_budget(name, amount):
    global available
    if name in budgets:
        raise ValueError("Budget exists")
    if amount > available:
        raise ValueError("Insufficient funds")
    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return


def spend(name, amount):
    """
    Notes the amount of money you spent
    and the name of the budget you want to keep track it against
    """
    if name not in expenditure:
        raise ValueError("No such budget")
    expenditure[name] += amount
    budgeted = budgets[name]
    spent = expenditure[name]
    return


def print_summary():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenditure[name]
        remaining = budgeted - spent
        global left_from_income
        left_from_income = available
        # use pretty tables for print summary
        x = PrettyTable()
        y = PrettyTable()
        z = PrettyTable()
        x.field_names = ["Budget Name", "Budgeted Amount", "Spent"]
        x.add_row([name, budgeted, spent])
        y.field_names = ["Remainder from Budget", "Left from Income"]
        y.add_row([remaining, left_from_income])
        z.field_names = ["Remaining"]
        z.add_row([(remaining + left_from_income)])
        print(x)
        print(y)
        print(z)


print(Fore.WHITE)
userInputBudget()
print(Fore.CYAN)
print_summary()
