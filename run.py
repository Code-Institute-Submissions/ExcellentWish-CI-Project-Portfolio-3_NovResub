import os
import sys
import confirm_user
import income_broken_down
import budget
import interest_calculator
import summary_table


def main():
    confirm_user
    income_broken_down
    budget
    interest_calculator
    summary_table


main()

restart = input("\nDo you want to restart the program? [y/n] > ")

if restart == "y":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
else:
    print("\nThe program will be closed...")
    print("\nThank you and goodbye!")
    sys.exit(0)
