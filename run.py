user = input("Type in your name and press return:\n ")
#try and expect here incase they write numbers in there name
available = float(input("Type in the amount of money you have and press return: \n"))
#try and expect here incase they write letters  
print(f"Your name is {user} and the amount you have is {available}")
confirm_user = input("Is this correct? Please type y or n: ")
#try and expect or if to continue or change the name or amount

budget = {}
expenditure = {}

def add_budget(name,amount):
    """
    Takes the name of the budget and the amount of money to be budgeted
    """
    global available
    if name in budget:
        raise ValueError("Budget name exists")
    if amount > available:
        raise ValueError("Insufficient funds")
    budget[name] = amount
    available -= amount
    expenditure[name] = 0
    return available

name = input("What is this budget for?")
amount = float(input("How much can you afford for this?"))

add_budget(name,amount)
print(f"the amount left {add_budget(name,amount)}")

def spend(name,amount):
    """
    Notes the amount of money you spent and the name of the budget you want to keep track it against
    """
    if name not in expenditure:
        raise ValueError("No such budget")
    expenditure[name] += amount
    budgeted = budget[name]
    spent = expenditure[name]
    return budgeted - spent    