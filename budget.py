from income_broken_down import week_income

available = week_income
budgets = {}
expenditure = {}

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
        print(name, budgeted, spent, remaining, left_from_income)
    


add_budget("food", 100)
spend("food",90)

print_summary()