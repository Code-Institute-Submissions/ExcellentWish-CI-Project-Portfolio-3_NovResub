from prettytable import PrettyTable
from colorama import init
from colorama import Fore
init()


def heading():
    # Heading for app
    x = PrettyTable()
    x.field_names = ["Budget Calculator"]
    x.add_row(["This will calculate your Income"])
    x.add_row(["This will also create your budgets"])
    x.add_row(["And also show you how much you can invest"])
    x.add_row(["And how long to become a millionaire"])
    print(x)


heading()


while True:
    user = input("Type in your name and press return:\n ")
    try:
        if user == "":
            raise ValueError('empty string')
    except ValueError as e:
        print(e)
        print('Valid name, please')
        continue
    if user == str(user):
        break
    else:
        print('Valid Thank you')

while True:
    try:
        available = float(input(Fore.GREEN + "What is your weekly income: "))
        if available == "":
            raise ValueError('empty Value')
    except ValueError as e:
        print(e)
        print('Valid value, please')
        continue
    if available == float():
        break
    else:
        print('Valid Thank you')
        break


print(Fore.BLUE)
print(f"Your name is {user} and your income is {available}")
print(Fore.WHITE)
confirm_user = input("Is this correct? Please type y or n: \n")

"""
This will validate the users input
"""

if confirm_user != "y":
    while (confirm_user == "n", confirm_user != "y" and confirm_user != "n"):
        if confirm_user != "y" and confirm_user != "n":
            print(Fore.RED + "Not a valid charater, please enter y or n.\n")
            print(Fore.BLUE)
            print(f"Your name is {user} and your income is {available}")
            print(Fore.WHITE)
            confirm_user = input("Is this correct? Please type y or n:\n")
            if confirm_user == "y":
                break
        user = input("Type in your name and press return:\n ")
        available = float(input("Enter your weekly income:\n"))
        print(Fore.BLUE)
        print(f"Your name is {user} and your income is{available}")
        print(Fore.WHITE)
        confirm_user = input("Is this correct? Please type y or n:\n")
        if confirm_user == "y":
            break
print(Fore.BLUE)


def confirm_user_summary():
    # Gets a pretty table of summary of your user
    x = PrettyTable()
    x.field_names = ["Your Name", "Your Weekly Income"]
    x.add_row([user, available])
    print(x)


confirm_user_summary()
