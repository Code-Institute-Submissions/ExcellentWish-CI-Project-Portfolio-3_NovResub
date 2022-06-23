from confirm_user import available

week_income = available
fortnight_income = 0
month_income = 0
year_income = 0
""" 
This will calculate the income of the user from there weekly to monthly to yearly income
This will help with what there budgets.
48 weeks in a working year in Ireland to count for holidays and to equal 12 months pay
"""
def week_income_to_fortnight(week_income):
    global fortnight_income
    fortnight_income = week_income * 2
    print(f"Your fortnight income is {fortnight_income} and weekly is {week_income}")
    return fortnight_income

week_income_to_fortnight(week_income)

def week_income_to_monthly(week_income):
    global month_income
    month_income = week_income * 4
    print(f"Your weekly income is {week_income} but your monthly income is {month_income}")
    return  month_income

week_income_to_monthly(week_income)

def week_income_to_year(week_income):
    global year_income
    year_income = week_income * 48
    print(f"Your weekly income is {week_income} but your yearly income is {year_income}")
    return year_income

week_income_to_year(week_income)

def month_income_to_week(month_income):
    week_income = month_income / 4
    print(f"Your monthly income is {month_income} but your weekly income is {week_income}")
    return    

month_income_to_week(month_income)

def month_income_to_year(month_income):
    year_income = month_income * 12
    print(f"Your monthly income is {month_income} but your yearly income is {year_income}")
    return

month_income_to_year(month_income)

def year_income_to_month(year_income):
    month_income = year_income / 12
    print(f"Your yearly income is {year_income} but your monthly income is {month_income}")
    return

year_income_to_month(year_income)

def year_income_to_week(year_income):
    week_income = year_income / 48
    print(f"Your yearly income is {year_income} but your weekly income is {week_income}")
    return

year_income_to_week(year_income)