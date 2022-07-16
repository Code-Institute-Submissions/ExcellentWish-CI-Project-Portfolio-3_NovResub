## Project Portfolio 3- Python Essentials - Code Institute.

## Budget App

The project will cover creating a budget manager.
Its aim is to add a user, let them enter there income either by week, month or year. I will break down there income by week, month or year.
After the user should be able to enter there budget,for this we will ask them to enter there budget name and the amount by month and we will work out there weekly and yearly costs. How much they want to spend and what they actually spent, and add it back to there income or minus it from that income.
Then we can ask the user if they want to invest the remaining amount or a percentage of the remaining amount.
For the investment we will also explain how long that invested amount will take to become 1,000,000 with interest from the initial investment.

# Table of Contents
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Site Aims:](#site-aims)
  - [How Is This Will Be Achieved:](#how-is-this-will-be-achieved)
  - [Flowchart](#flowchart)
  - [Tech used](#tech-used)
    - [Functions and Imports](#functions-and-imports)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [GitHub](#github)
    - [Heroku](#heroku)
    - [Make a clone](#make-a-clone)
  - [Credits](#credits)
  - [Reminders](#reminders)
  - [Creating the Heroku app](#creating-the-heroku-app)
  - [Constraints](#constraints)

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
  - I used Prettytable to create tables throughout my project
  - I used datetime for the interest_calculator to help find out how long it takes to become a millionaire
  - I used Colorama for colour in this project as having a plain text is abit boring




## Testing

48 weeks instead of 52 as month income *12 did not add to the same value.
Divide month to week
divide year to month and week but came across user input issue


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
https://www.myloancare.in/fixed-deposit/simple-interest-formula/#:~:text=The%20formula%20for%20calculating%20Principal,and%20T%20is%20Time%20Period for interest calculator



Welcome 

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!