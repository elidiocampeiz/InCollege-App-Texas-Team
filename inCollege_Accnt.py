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

# def clear_accounts():
#     # Init DB
#     DB = database.Database()
#     DB.clear()

# Function for login UI
def login(DB):
    # Init DB
    # DB = database.Database()
    # Get user input
    username = input("Please enter your username, type 'q' to cancel: ")
    if (username == 'q'):
        return False
    password = input("Please enter your password, type 'q' to cancel: ")
    if (password == 'q'):
        return False
    # Try to login with username and password combination
    login = DB.login(username, password)
    # Handle error TODO: Replace by Try/catch block
    if (login == False):
        print("\nLogin Error")
        return login

    theUser = user.User(username, DB)
    return theUser

# Function for create an account UI
def create_account(DB):
    # Init DB
    # DB = database.Database()
    # Get user input
    username = str(input("Please enter username, type 'q' to cancel: "))
    if (username == 'q'):
        return False
    password = str(input("Please enter password, type 'q' to cancel: "))
    if (password == 'q'):
        return False
    # Check if password is secure
    while passwordChecker(password) == False:
        password = str(input("Please enter new password or type 'q' to quit: "))
        if password == 'q':
            return False

    # Getting name
    firstName = str(input("Please enter first name, type 'q' to cancel: "))
    if (firstName == 'q'):
        return False
    lastName = str(input("Please enter last name, type 'q' to cancel: "))
    if (lastName == 'q'):
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

    #Get user input
    title = str(input("Please enter job title: "))
    description = str(input("Please enter job description: "))
    employer = str(input("Please enter employer for job: "))
    location = str(input("Please enter job location: "))
    salary = str(input("Please enter job salary: "))

    create_job_posting = DB.create_job_posting(title, description, employer, location, salary, fullname)

    if (create_job_posting == False):
        print("\nCreate Job Posting Error")
    
    create_job_posting
    
