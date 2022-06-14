user = input("Type in your name and press return: ")
#try and expect here incase they write numbers in there name
available = float(input("Type in the amount of money you have and press return: "))
#try and expect here incase they write letters  
print(f"Your name is {user} and the amount you have is {available}")
confirm_user = input("Is this correct? Please type y or n: ")
#try and expect or if to continue or change the name or amount

budget = {}
expenditure = {}

def add_budget(name,amount):
    global available
    budget[name] = amount
    available -= amount
    expenditure[name] = 0
    return available

