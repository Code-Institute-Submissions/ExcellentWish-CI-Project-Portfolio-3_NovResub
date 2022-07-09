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
    budgetname = str(input('Enter the budget name: '))
    budgetAmount = float(input('Enter the amount you have set aside for the budget: '))
    spendings = float(input('Enter the amount you have spent: '))
    add_budget(budgetname, budgetAmount)
    spend(budgetname, spendings)

def add_budget(name , amount):
    global available
    if name in budgets:
        raise ValueError("Budget exists")
    if amount > available:
        raise ValueError("Insufficient funds")    
    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return print(budgets, available)

def spend(name, amount):
    """
    Notes the amount of money you spent and the name of the budget you want to keep track it against
    """
    if name not in expenditure:
        raise ValueError("No such budget")
    expenditure[name] += amount
    budgeted = budgets[name]
    spent = expenditure[name]
    
    remaining_from_budget = budgeted - spent
    return print(f"{remaining_from_budget} remaining from budget")    

def print_summary():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenditure[name]
        remaining = budgeted - spent
        global left_from_income
        left_from_income = remaining + available

        # use pretty tables for print summary
        x = PrettyTable()
        x.field_names = ["Budget Name", "Budgeted Amount", "Spent", "Remainder from Budget", "Left from Income"]
        x.add_row([name, budgeted, spent, remaining, left_from_income])
        print(x)
        # print('This is your budget summary:')
        # print('Name | Budgeted | Spent | Remaining | Left From Income')
        # print(name, budgeted, spent, remaining, left_from_income)
    
print(Fore.WHITE)
userInputBudget()
print(Fore.CYAN)
print_summary()