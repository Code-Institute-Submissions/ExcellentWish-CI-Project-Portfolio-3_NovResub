from confirm_user import confirm_user_summary
from income_broken_down import income_broken_down_summary
from budget import print_summary
from interest_calculator import interest_calculator_summary
from colorama import init
from colorama import Fore
init()

print(Fore.WHITE)
print("Here is your final summary")


def summary():
    confirm_user_summary()
    income_broken_down_summary()
    print_summary()
    interest_calculator_summary()


summary()
