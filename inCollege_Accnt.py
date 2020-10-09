import inCollege_Database as database
import inCollege_CurrentUser as user
import time

# function that validates a secure password
def passwordChecker(password):
    contains_upper = False
    contains_digit = False
    contains_alpha = True
    if password== None or len(password)<7 or len(password)>13:
        print("...")
        time.sleep(1)
        print('|*| Error - Password Must contain 7 --> 13 characters |*|')
        time.sleep(1)
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
            print('|*| Password Must Contain At Least One Digit (0-9) |*|')
        if contains_upper == False:
            print('|*| Password Must Contain At Least One Upper Case Letter (A-Z) |*|')
        if contains_alpha == True:
            print("|*| Password Must Not Contain Alpha-Numeric Characters (e.g. '^', ']', '#') |*|")
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
    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
    print("+--------------+")
    print("|    Log In    |")
    print("+--------------+\n")
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
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("\n|*| Login Error |*|\n")
        return login

    theUser = user.User(username, DB)
    return theUser

# Function for create an account UI
def create_account(DB):
    # Init DB
    # DB = database.Database()
    # Get user input
    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
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
        password = str(input("Enter New Password: "))
        if password == 'x':
            return False

    # Getting name
    firstName = str(input("Enter First Name: "))
    if (firstName == 'x'):
        return False
    lastName = str(input("Enter Last Name: "))
    if (lastName == 'x'):
        return False

    # Try to create new student account in DB
    create_account = DB.create_account(username, password, firstName, lastName)
    # Handle error TODO: Replace by Try/catch block
    if (create_account == False):
        print("\n|*| Create Account Error |*|")
    return create_account

def post_job(fullname, DB):
    # Init DB
    # DB = database.Database()

    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
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
        print("\n|*| Create Job Posting Error |*|")
    
    return create_job_posting

#Getting School info from student
def school_info(school_name, major, year, DB):
    # Init DB
    # DB = database.Database()

    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
    print("+--------------------------------------------------+")
    print("|    Add University, major and your school year    |")
    print("+--------------------------------------------------+\n")

    #Get user input
    university = input("Enter The University you attend: ")
    if university == 'x':
        return False
    major = input("Enter The Major you're taking: ")
    if major == 'x':
        return False
    year = str(input("Enter Your Status Year(Freshman, Sophomore, Junior, Senior): "))
    if year == 'x':
        return False

    set_education = DB.set_education(university, major, year)

    if (set_education == False):
        print("\n|*| Putting School info Error |*|")
    
    return set_education

#Gets the Users experience  
def user_experience(DB, experience):
    
    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
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
    start_date = str(input("Enter the Date you Started: "))
    if location == 'x':
        return False
    end_date = str(input("Enter The Date You Ended: "))
    if end_date == 'x':
        return False

    set_experience = DB.set_experience(title, description, employer, location, start_date, end_date)

    if (set_experience == False):
        print("\n|*| Set experience Error |*|")
    
    return set_experience

def title(self):
    profile_title = str(input("Enter a title for you profile: "))
    
    set_title = DB.set_title(profile_title)
    return set_title

def about(self):
    profile_about = str(input("Tell Us About Yourself: "))
    
    set_title = DB.set_title(profile_title)
    return set_title


def clear_accounts():
    database.Database

# TODO
# Change Account Settings 
# field is the settings type (e.g. )
