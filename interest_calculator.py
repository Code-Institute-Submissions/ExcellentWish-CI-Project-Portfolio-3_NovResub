"""
Calculate interest from investing. Average etf and MTF are 8% a year.
We take an amount the user wants to invest and add 8% until they make a million and tell them how long 
it takes 
"""

def interest():                    
    principal = float(input('Enter the principal: ')) #the amount of money initially invested
    print("Average rate is 8% a year")
    rate = float(8)
    time = float(input('Enter the time in years: '))
    Simple = (principal * rate * time/ 100.00)     #interest formula
    print(f"Simple Interest value over the years. = {Simple}")
    print(Simple + principal)
interest()
