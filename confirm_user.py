from colorama import init
from colorama import Fore
init()


user = input("Type in your name and press return:\n ")
available = float(input(Fore.GREEN + "What is your weekly income: "))
print(Fore.BLUE + f"Your name is {user} and the amount you have is {available}" + Fore.WHITE)
confirm_user = input("Is this correct? Please type y or n:0 \n")
"""
This will validate the users input 
"""
        
if confirm_user != "y": 
    while (confirm_user == "n", confirm_user != "y" and confirm_user != "n"):
        if confirm_user != "y" and confirm_user != "n":
            print(Fore.RED + "Not a valid charater, please enter y or n.\n")
            print(Fore.BLUE + f"Your name is {user} and the amount you have is {available}" + Fore.WHITE)
            confirm_user = input("Is this correct? Please type y or n:1 ") 
            
            if confirm_user == "y":
                break
        
        user = input("Type in your name and press return:\n ")
        available = float(input("Type in the amount of money you have and press return: \n"))
        print(Fore.BLUE + f"Your name is {user} and the amount you have is {available}" + Fore.WHITE)
        confirm_user = input("Is this correct? Please type y or n:2 ") 
        if confirm_user == "y":
            break

print(Fore.BLUE + f"End of user confirmation user: {user} money: {available}\n" + Fore.WHITE)