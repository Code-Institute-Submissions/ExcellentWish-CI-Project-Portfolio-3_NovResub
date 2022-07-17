# Project Portfolio 3- Python Essentials - Code Institute.

## Budget App

The project will cover creating a budget manager.
Its aim is to add a user, let them enter there income either by week, month or year. I will break down there income by week, month or year.
After the user should be able to enter there budget,for this we will ask them to enter there budget name and the amount by month and we will work out there weekly and yearly costs. How much they want to spend and what they actually spent, and add it back to there income or minus it from that income.
Then we can ask the user if they want to invest the remaining amount or a percentage of the remaining amount.
For the investment we will also explain how long that invested amount will take to become 1,000,000 with interest from the initial investment.

# Table of Contents
- [Project Portfolio 3- Python Essentials - Code Institute.](#project-portfolio-3--python-essentials---code-institute)
  - [Budget App](#budget-app)
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Site Aims:](#site-aims)
  - [How Is This Will Be Achieved:](#how-is-this-will-be-achieved)
  - [Flowchart](#flowchart)
  - [Tech used](#tech-used)
    - [Functions and Imports](#functions-and-imports)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Link To Google Doc for testing](#link-to-google-doc-for-testing)
    - [Bugs and Issues](#bugs-and-issues)
  - [Deployment](#deployment)
    - [GitHub](#github)
    - [Heroku](#heroku)
    - [Make a clone](#make-a-clone)
  - [Credits](#credits)

## User Experience

* As a user I want to be able to find out my income through out the year
* I want the user to know there fortnight, monthly and yearly incomes
* I want to be able to create budgets and find out what the spendings are
* I want to be able to display the information as it helps users to see rather then have it in the back ground
* After I want to help get the idea to invest by using simple interest.
*  I want it to be a simple app for a User
  
## Site Aims:
* I wanted to learn Python and show my logic with a budget, app as we are experiencing higher inflation in Europe.
* I want to show the importance of saving and budgeting
* I want to show the importance of investing 

## How Is This Will Be Achieved:
* By using Github, Python and heroku.

## Flowchart
![Flowchart](assets/images/python%20flow%20chart.png)


## Tech used
- For this project I used Github to save my project.
- I used Gitpod as my editor for the code. 
- I used python for the code in the project.
- I used HeroKu for deployment of this project
- 
  ### Functions and Imports
  - Main() this starts the project in `run.py`
  - Heading() creates a table that I used for a heading for this project.
  - I created functions in Income_broken_down to find out differnt values of income throughout the year
  - week_income_to_fortnight(week_income) Calculates the week income to an income for every 2 weeks
  - week_income_to_monthly(week_income) Calculates the week income to an income for every 4 weeks
  - week_income_to_year(week_income) Calculates the week income to an income for every 48 weeks (more information in testing)
  - Created functions to divide the month to week (more in testing)
  - Created functions to divide the year to week (more in testing)
  - Created functions to divide the year to month (more in testing)
  - userInputBudget() Allows user to input there budgets 
  - add_budget(name , amount) Creates the budget and adds it to a table 
  - spend(name, amount) Notes the amount of money you spent and the name of the budget you want to keep track it against
  - print_summary() Creates the table for the budgets created.
  - interest_heading() Creates a table for the interest_calculator as a heading
  - interested_income() Finds a recommended amount to invest from your income after budget.
  - interest() Finds the calculated interested from interested_income and finds simple interest formula
  
  - I used Prettytable to create tables throughout my project
  - I used datetime for the interest_calculator to help find out how long it takes to become a millionaire
  - I used Colorama for colour in this project as having a plain text is abit boring




## Testing
Used PEP8 for testing 
Used print(f"End of user confirmation user: {user} money: {available}\n") in confirm user to test the values.
Used print(expenditure)
    return print(f"{remaining_from_budget} remaining from budget") in budget.py spend function
    and 
return print(budgets, available)  add_budgets   
This allowed me to test the values being entered 


### Validator Testing 
Using PEP8 I came accoss issues in my code.
Here are the before and after

Run.py before


![Run.py](assets/images/PEP8-run.py-errors.PNG)


And After

![Run.py](assets/images/PEP8-run.png)

Confirm_user.py


![Confirm_user.py](assets/images/PEP8-confirm_user-errors.PNG)

And After


![Confirm_user.py](assets/images/PEP8-confirm_user.png)

Income_broken_down.py


![Income_broken_down.py](assets/images/PEP8-Income-broken-down.pyerrors.PNG)

And After

![Income_broken_down.py](assets/images/PEP8-Income-broken-down.png)

budget.py


![Budget.py](assets/images/PEP8-budget-errors.PNG)

And After

![budget](assets/images/PEP8-budget.png)

interst_calculator.py

![interest_calculator](assets/images/PEP8-interest_calculator.py%20errors.PNG)

And After

![interest_calculator](assets/images/PEP8-interest_calculator.png)

### Link To Google Doc for testing 
Google doc for testing 
[Google-doc](https://docs.google.com/spreadsheets/d/18BBtH5rpuu0lOS5O8NnxxMkAo9nqqgCsV6n0X579aEA/edit#gid=0)

and Image

![Google-doc-testing](assets/images/GoogleDocTesting.PNG)

### Bugs and Issues
- I had to use 48 weeks instead of 52. As month income *12 did not add to the same value as week * 52.
- Eg 200 * 52 = 10400 but 200 * 4 = 800 and 800 * 12 = 9600
- In budget.py I wanted the left over income  to be taken away each time a new budget was created and print the value before it is taken away.
  It only prints out the final value after it is taken away.

## Deployment

### GitHub 
  - [Login](https://github.com/) to GitHub
  - Click "Repository" and select "New"
  - Give the repository a name and description and then click "Create repository"
  - Click "Gitpod" to start editing
  - In the terminal enter "python3 run.py" to run your code

### Heroku
* The project was deployed using [Heroku](https://www.heroku.com)
*  Navigate to your [heroku dashboard](https://dashboard.heroku.com/apps)
- Click "New" and select "Create new app".  
- Input a meaningful name for your app and choose the region best suited to
  your location.  
- Select "Settings" from the tabs.  
  - Click "Reveal Config Vars".  
  - Input `PORT` and `8000` as one config var and click add.  
  - Click "Add buildpack".  
  - Add "nodejs" and "python" from the list or search if necessary, remember to
    click save.  
  - The ordering is as follows:
      1. `heroku/python`
      2. `heroku/nodejs`
  - Python must be the first buildpack. They can be dragged into the correct
    position if needed.  
- Select "Deploy" from the tabs.  
  - Select "GitHub - Connect to GitHub" from deployment methods.  
  - Click "Connect to GitHub" in the created section.  
  - Search for the GitHub repository by name.  
  - Click to connect to the relevant repo.  
  - Either click `Enable Automatic Deploys` for automatic deploys or `Deploy
    Branch` to deploy manually. Manually deployed branches will need
    re-deploying each time the repo is updated.  
  - Click `View` to view the deployed site.  
- The live site can also be accessed from your repo in GitHub from the
  environments section of the repo.
  - Click the link to view deployments history.  
  - Click `View deployment`. This page also shows all the deployment history.  
The site is now live and operational

### Make a clone
- [Login](https://github.com/) to GitHub
  - Click "Repository" and select "project"
	- Click the "Code" dropdown menu.
  - Click "Clone with HTTPS" and copy the link
	- Open IDE "Ternimal" in local machine
  - Type "git clone" followed by URL
  - Press "Enter" to create clone


## Credits
- For [interest formulas](https://www.myloancare.in/fixed-deposit/simple-interest-formula/#:~:text=The%20formula%20for%20calculating%20Principal,and%20T%20is%20Time%20Period) 
- DK books. [Beginner's step by step coding course]( https://www.amazon.com/Beginners-Step-Step-Coding-Course/dp/1465482210)
- Mentor Ronan McClelland 
- To Anna Greaves and her [Love Sandwiches - Essentials Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/58d3e90f9a2043908c62f31e51c15deb/)