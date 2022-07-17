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
    budget_num = int(input("Enter the number of budgets you want to record: "))
    while budget_num > 0:
        budget_num -= 1
        budgetname = str(input('Enter the budget name: '))
        budgetAmount = float(input('Enter the amount this budget:'))
        spendings = float(input('Enter the amount you have spent: '))
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
    remaining_from_budget = budgeted - spent
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
        x.field_names = ["Budget Name", "Budgeted Amount", "Spent"]
        x.add_row([name, budgeted, spent])
        y.field_names = ["Remainder from Budget", "Left from Income"]
        y.add_row([remaining, left_from_income])
        print(x)
        print(y)
print(Fore.WHITE)
userInputBudget()
print(Fore.CYAN)
print_summary()
