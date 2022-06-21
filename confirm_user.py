def confirm_user_for_project():
    user = input("Type in your name and press return:\n ")
    available = float(input("Type in the amount of money you have and press return: \n"))
    print(f"Your name is {user} and the amount you have is {available}")
    confirm_user = input("Is this correct? Please type y or n:0 \n")
    """
    This will validate the users input 
    """
            
    if confirm_user != "y": 
        while (confirm_user == "n", confirm_user != "y" and confirm_user != "n"):
            if confirm_user != "y" and confirm_user != "n":
                print("Not a valid charater, please enter y or n.\n")
                print(f"Your name is {user} and the amount you have is {available}")
                confirm_user = input("Is this correct? Please type y or n:1 ") 
                
                if confirm_user == "y":
                    break
            
            user = input("Type in your name and press return:\n ")
            available = float(input("Type in the amount of money you have and press return: \n"))
            print(f"Your name is {user} and the amount you have is {available}")
            confirm_user = input("Is this correct? Please type y or n:2 ") 
            if confirm_user == "y":
                break

    print(f"End of user confirmation user:{user} money:{available}")