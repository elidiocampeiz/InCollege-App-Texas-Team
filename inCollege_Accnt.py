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

    # theUser = user.User(username, DB)
    # return theUser
    theStudent = DB.get_student_by_username(username)
    return theStudent

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
    # Get student form DB to call update profile info
    student = DB.get_student_by_username(username)
    if not create_account or not student:
        print("\n|*| Create Account Error |*|")
        return False
    
    # Get Profile Info
    profile_complete = update_profile_info(DB, student)
    if not profile_complete:
        print("\n|*| Complete Profile Later |*|")
    
    return profile_complete

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

def update_profile_info(DB, student):

    print("|*|     NOTE - Enter 'x' at any time to go back    |*|\n")
    print("+--------------------------------------------------+")
    print("|             Update Profile Information           |")
    print("+--------------------------------------------------+\n")

    # Ask for Title
    new_profile_title = input("Enter a title for your profile: ")
    if new_profile_title == 'x':
        return False
    # Update Title
    student.update(title=new_profile_title)
    # Save Student Update
    DB.set_student(student)

    # Ask for About 
    new_profile_about = input("Enter the about section of your profile: ")
    if new_profile_about == 'x':
        return False
    # Update student's About
    student.update(about=new_profile_about)
    # Save Student Update
    DB.set_student(student)

    # Ask for Education 
    education = update_education_info(DB, student)
    
    # Ask for Job Experiences 
    experience = update_experience_info(DB, student)
    if not experience:
        return False
    if not education:
        return False
    return True
#Getting School info from student
def update_education_info(DB, student):
    # Init DB
    # DB = database.Database()

    print("+--------------------------------------------------+")
    print("|      Enter University, Major and School Year     |")
    print("+--------------------------------------------------+\n")
    print("|*|    NOTE - Enter 'x' at any time to go back   |*|\n")

    # Get University input
    words = input("Enter your University: ")
    if words == 'x':
        return False
    university = ''
    # Captilize each starting letter
    for word in words.split():
        university += word.capitalize() + ' '
    
    # Get Major input
    words = input("Enter your Major: ")
    if words == 'x':
        return False
    major = ''
    # Captilize each starting letter
    for word in words.split():
        major += word.capitalize() + ' '
    
    # Get year input
    words = input("Enter Your Status Year (Freshman, Sophomore, Junior, Senior): ")
    if words == 'x':
        return False
    # Captilize each starting letter
    year = words.capitalize()

    # Update Student Education 
    student.set_education(university, major, year)
    # Save student update
    result = DB.set_student(student)
    return result

#Gets the Users experience  
def update_experience_info(DB, student):

    print("+--------------------------------------------------+")
    print("|            Enter Up To 3 Job Experiences         |")
    print("+--------------------------------------------------+\n")
    print("|*|   NOTE - Enter 'x' at any time to go back    |*|\n")
    i = 0
    job_list = ['First ', 'Second', 'Third ']
    while i < 3:
        print("+------------------------------------+")
        print("|     Enter {} Job Experience     |".format(job_list[i]))
        print("+------------------------------------+\n")
        title = input("Enter Job Title: ")
        if title == 'x':
            return False
        description = input("Enter Job Description: ")
        if description == 'x':
            return False
        employer = input("Enter Employer For Job: ")
        if employer == 'x':
            return False
        location = input("Enter Job Location: ")
        if location == 'x':
            return False
        start_date = input("Enter the Date you Started: ")
        if location == 'x':
            return False
        end_date = input("Enter The Date You Ended: ")
        if end_date == 'x':
            return False
        # Add new job experience to Student
        result = student.add_job_experience(title, employer, start_date, end_date, location, description)
        # If add_job_experience not success
        if not result:
            print("\n|*| Maximum Number of Jobs |*|")
            return False
        # Save Update
        DB.set_student(student)
        # Next iteration
        i+=1
    return True


def clear_accounts():
    database.Database

# TODO display profile
def display_profile(DB, student):
    # ... Display Profile 
    # Name 
    # Title 
    # About 
    # Education
    # Experience
    
    print(" +-----------------------------+")
    print(" |            Profile          |")
    print(" +-----------------------------+")

    for key, value in student.__dict__.items():
        print(key,': ', value)
    
    print(" +-----------------------------+")
    print(" |        Edit Profile?        |")
    print(" +-----------------------------+")
    print(" | 1. Yes                      |")
    print(" | x. Go Back                  |")
    print(" +-----------------------------+")

    
    edit_selection = input('Enter Your Selection: ')
    if edit_selection == '1':
        print("+=====================================+")
        print("|*| Edit Profile Under Construction |*|")
        print("+=====================================+\n")
        time.sleep(1)
    elif edit_selection == 'x':
        print("... Going Back\n")
        time.sleep(1)
        return False
    else:
        print("...Invalid Input")
        time.sleep(1)
        return True # continue loop in Home line 966
        