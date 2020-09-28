import inCollege_Database as database
import inCollege_CurrentUser as user

# function that validates a secure password
def passwordChecker(password):
    contains_upper = False
    contains_digit = False
    contains_alpha = True
    if password== None or len(password)<7 or len(password)>13:
        print('password must contain at least 7 and at most 13 characters.')
        return False
    for character in password:
        if character.isupper():
            contains_upper = True
        if character.isdigit():
            contains_digit = True
        if password.isalnum():
            contains_alpha = False
    # If password is does not meet the minimum conditions return False
    if contains_digit == False or contains_upper == False or contains_alpha == True:
        # Tell the user why the password is not secured
        if contains_digit == False:
            print('password must contain at least one digit (0-9).')
        if contains_upper == False:
            print('password must contain at least one upper case letter (A-Z).')
        if contains_alpha == True:
            print("password must not contain alpha-numeric characters (e.g. '^', ']', '#').")
        return False
    # else return True
    return True
# hhh
# def clear_accounts():
#     # Init DB
#     DB = database.Database()
#     DB.clear()

# Function for login UI
def login(DB):
    # Init DB
    # DB = database.Database()
    # Get user input
    print("|*|NOTE - Enter 'x' at any time to go back|*|\n")
    print("+--------------+")
    print("|    Log In    |")
    print("+--------------+")
    username = input("Enter Your Username: ")
    if (username == 'x'):
        return False
    password = input("Enter Your Password: ")
    if (password == 'x'):
        return False

    # Try to login with username and password combination
    login = DB.login(username, password)
    # Handle error TODO: Replace by Try/catch block
    if (login == False):
        print("\n     ***Login Error***")
        return login

    theUser = user.User(username, DB)
    return theUser

# Function for create an account UI
def create_account(DB):
    # Init DB
    # DB = database.Database()
    # Get user input
    print("|*|NOTE - Enter 'x' at any time to go back|*|\n")
    print("+-------------------+")
    print("| Create An Account |")
    print("+-------------------+\n")
    username = str(input("Enter username: "))
    if (username == 'x'):
        return False
    password = str(input("Enter password: "))
    if (password == 'x'):
        return False
    # Check if password is secure
    while passwordChecker(password) == False:
        password = str(input("Please enter new password: "))
        if password == 'x':
            return False

    # Getting name
    firstName = str(input("Please enter first name: "))
    if (firstName == 'x'):
        return False
    lastName = str(input("Please enter last name: "))
    if (lastName == 'x'):
        return False

    # Try to create new student account in DB
    create_account = DB.create_account(username, password, firstName, lastName)
    # Handle error TODO: Replace by Try/catch block
    if (create_account == False):
        print("\nCreate Account Error")
    return create_account

def post_job(fullname, DB):
    # Init DB
    # DB = database.Database()

    print("|*|NOTE - Enter 'x' at any time to go back|*|\n")
    print("+-------------------+")
    print("|    Post A Job     |")
    print("+-------------------+\n")

    #Get user input
    title = input("Enter Job Title: ")
    if title == 'x':
        return False
    description = input("Enter Job Description: ")
    if description == 'x':
        return False
    employer = str(input("Enter Employer For Job: "))
    if employer == 'x':
        return False
    location = str(input("Enter Job Location: "))
    if location == 'x':
        return False
    salary = str(input("Enter Job Salary: "))
    if salary == 'x':
        return False

    create_job_posting = DB.create_job_posting(title, description, employer, location, salary, fullname)

    if (create_job_posting == False):
        print("\nCreate Job Posting Error")
    
    return create_job_posting
    
def clear_accounts():
    database.Database