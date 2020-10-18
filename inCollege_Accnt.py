import inCollege_Database as database
import inCollege_CurrentUser as user
from inCollege_Student import *
import time
import textwrap #This will be used for formatting tex (ensuring lines do not exceed a certain amount for ex)


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
    firstname = str(input("Enter First Name: "))
    if (firstname == 'x'):
        return False
    lastname = str(input("Enter Last Name: "))
    if (lastname == 'x'):
        return False

    # Try to create new student account in DB
    create_account = DB.create_account(username, password, firstname, lastname)
    
    # Get student form DB to call update profile info
    student = DB.get_student_by_username(username)

    if not create_account or not student:
        print("\n|*| Create Account Error |*|")
        return False
    
    # TODO: Addp functionality to add real friends
    # Add Dummy friends 
    student.add_dummy_friends()
    # Save Dummy Friends
    DB.set_student(student)

    # Get Profile Info
    update_profile_info(DB, student)
    
    # print("\n|*| You Can Change Profile Later! |*|")
    
    return True
    # return create_account

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

    print("|*|     NOTE - Enter 'x' to go back and skipp    |*|\n")
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

    print()
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

    # We don't need this because this function is a continuation of "update profile"
    # print("+--------------------------------------------------+")
    # print("|      Enter University, Major and School Year     |")
    # print("+--------------------------------------------------+\n")
    # print("|*|    NOTE - Enter 'x' at any time to go back   |*|\n")

    print()
    # Get University input
    words = input("Enter your University: ")
    if words == 'x':
        return False
    university = ''
    # Captilize each starting letter
    for word in words.split():
        university += word.capitalize() + ' '
    
    print()
    # Get Major input
    words = input("Enter your Major: ")
    if words == 'x':
        return False
    major = ''
    # Captilize each starting letter
    for word in words.split():
        major += word.capitalize() + ' '
    
    print()
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
    print("|*|     NOTE - Enter 'x' to go back and skipp    |*|\n")
    i = 0
    job_list = ['First ', 'Second', 'Third ']
    while i < 3:
        print("+------------------------------------+")
        print("|     Enter {} Job Experience    |".format(job_list[i]))
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
        if start_date == 'x':
            return False
        end_date = input("Enter The Date You Ended: ")
        if end_date == 'x':
            return False
        # Add new job experience to Student
        result = student.add_job_experience(title, employer, start_date, end_date, location, description)
        # If add_job_experience not success
        if not result:
            print("\n|*| Maximum Number of Jobs |*|")
            
        # Save Update
        DB.set_student(student)
        # Next iteration
        i+=1
    return True


def clear_accounts():
    database.Database

# TODO display profile
def display_profile(student):
    # if student.username=='':
    #     # Invalid Input all students must have a username Student 
    #     return False
     
    # student object's dictionary
<<<<<<< HEAD
    fullname = ""
    prof_title = ""
    prof_about = ""
    dict_Jobs = ""
    stu_university = ""
    stu_major = ""
    stu_schoolYear = ""

    #looping through stud info to populate variables 
    for key, value in student.__dict__.items():
        print(key,': ', value)
        if key == "firstname":
            fullName = value
        elif key == "lastname":
            fullName = fullName + " " + value
        elif key == "title":
            prof_title = value
        elif key == "about":
            wrapper = textwrap.TextWrapper(width=41) #ensures the text does not exceed 41
            prof_about = wrapper.fill(text=value) #when this prints, it will not exceed 41 chars
        elif key == "education":
            #since "education" key has a value that is a dict with other keys,
            # we must extract those key's values using another for loop
            # (in this case value is )
            for val in value:
                if val == "university":
                    stu_university = val
                elif val == "major":
                    stu_major = val
                elif val == "year":
                    stu_schoolYear = val

        elif key == "experience":
            dict_Jobs = value

    print(" +---------------------------------------+")
    print(" |           inCollege Profile           |")
    print(" +---------------------------------------+")

    print("      ", fullName)
    print("         ", prof_title)
    print(" +---------------------------------------+")
    print(" |                      .--------------. |")
    print(" |                      |      /~~\    | |") 
    print(" |     .........        |   | ( OO )   | |")
    print(" |   ..............     |    \ \--/    | |")
    print(" |   ..............     |      \II     | |")
    print(" |   ................   |       <>\    | |")
    print(" |   .............      |       <>  \  | |")
    print(" |                      |      /  \    | |")
    print(" |                      |     /    \   | |")
    print(" |                      `--------------' |")
    print(" +---------------------------------------+\n")

    print("About Me:\n", prof_about, "\n")
    print("Education History")
    print("-----------------")
    print("School: ", stu_university)
    print("Year: ", stu_schoolYear)
    print("Major: ", stu_major, "\n")
    print(" Job Experience")
    print("-----------------") 
    counter = 0 #this counter keeps track of which section of job dictionary we are in
    outer_counter = 1 # starting at one to label Job1, Job2, Job3
    for job in dict_Jobs:
        for val in job:
            if counter == 0:
                print("Job Title ", outer_counter, ": ", val)
            elif counter == 1:
                print("Employer: ", val)
            elif counter == 2:
                print("Start Date: ", val)
            elif counter == 3:
                print("End Date: ", val)
            elif counter == 4:
                print("Location: ", val)
            elif counter == 5:
                print("Description: ", val) #text wrap
            counter += 1 #incrementing
        outer_counter += 1
        print() #put spacing between each job        
=======
    fullname = student.firstname.capitalize() + ' ' + student.lastname.capitalize()
    prof_title = student.title
    prof_about = student.about
    list_of_jobs = student.experience
    # stu_education = student.get_education()
    stu_university = student.get_education('university')
    stu_major = student.get_education('major')
    stu_schoolYear = student.get_education('year')
    # 
    print(" +----------------------------------------+ ")
    print(" |            inCollege Profile           | ")
    print(" +----------------------------------------+ ") # ' +' + 40 +  ' +'  = 44 chars

    print(' |', fullname.center(40-2, ' '), '| ')
    print(' |', prof_title.center(40-2, ' '), '| ')
    print(" +----------------------------------------+")
    print(" |                       .--------------. |")
    print(" |                       |      /~~\    | |") 
    print(" |      .........        |   | ( OO )   | |")
    print(" |    ..............     |    \ \--/    | |")
    print(" |    ..............     |      \II     | |")
    print(" |    ................   |       <>\    | |")
    print(" |    .............      |       <>  \  | |")
    print(" |                       |      /  \    | |")
    print(" |                       |     /    \   | |")
    print(" |                       `--------------' |")
    print(" +----------------------------------------+\n")

    print(" +----------------------------------------+")
    print(' |','About Me:'.center(40-2, ' '), '| ') 
    print(" +----------------------------------------+")
    print(' |', prof_about.center(40-2, ' '), '| ') # prof_about
    print(" +----------------------------------------+\n")

    print(" +----------------------------------------+")
    print(" |           Education History            |")
    print(" +----------------------------------------+")
    print(' | School: ', stu_university.center(40-9-2, ' '), '| ')
    print(" | Year: ", stu_schoolYear.center(40-7-2, ' '), '| ')
    print(" | Major: ", stu_major.center(40-8-2, ' '), '| ')
    print(" +----------------------------------------+")
    print()
    print(" +----------------------------------------+")
    print(" |             Job Experience             |")

    
    for job_experience in list_of_jobs:
        print(" +----------------------------------------+")
        print(" | Job Title:  ", job_experience['title'].ljust(40-13-2, ' '), '| ')
        print(" | Employer:   ", job_experience['employer'].ljust(40-13-2, ' '), '| ')
        print(" | Start Date: ", job_experience['start_date'].ljust(40-13-2, ' '), '| ')
        print(" | End Date:   ", job_experience['end_date'].ljust(40-13-2, ' '), '| ')
        print(" | Location:   ", job_experience['location'].ljust(40-13-2, ' '), '| ')
        print(" | Description:", job_experience['description'].ljust(40-13-2, ' '), '| ')
        # print(' |', job_experience['description'].ljust(40-2, ' '), '| ')
    
    print(" +----------------------------------------+ ")
    print()
>>>>>>> d6011407a894b25bf3747c78ebe73327f859009d
    
def edit_profile_menu( student):
    print(" +----------------------------------------+ ")
    print(" |            Edit Profile?               |")
    print(" +----------------------------------------+ ")
    print(" | 1. Yes                                 |")
    print(" | x. Go Back                             |")
    print(" +----------------------------------------+ ")

    
    edit_selection = input('Enter Your Selection: ')
    if edit_selection == '1':
        print("+=====================================+")
        print("|*| Edit Profile Under Construction |*|")
        print("+=====================================+\n")
        time.sleep(1)
        return True
    elif edit_selection == 'x':
        print("... Going Back\n")
        time.sleep(1)
        return False
    else:
        print("...Invalid Input\n")
        time.sleep(1)
        return True # continue loop in Home line 966

def display_friend_profile(student):

    display_profile(student)
    print(" +----------------------------------------+")
    print(" |          Enter 'x' to go back          |")
    print(" +----------------------------------------+")

    selection = input('Enter Your Selection: ')
    if selection == 'x':
        print("... Going Back\n")
        time.sleep(1)
        return False
    else:
        print("...Invalid Input")
        time.sleep(1)
        return True

def diplay_friend_list(student):
    print(" +----------------------------------------+ ")
    print(" |            List of Friends             | ")
    print(" +----------------------------------------+ ")
    print(" |  Select Friend to view their profile   | ")
    print(" +----------------------------------------+ ") # 2(' |') + 40('-') + 2('| ) chars
    

    for index, friend in enumerate(student.friends):
        fullname = friend.firstname.capitalize() + ' ' + friend.lastname.capitalize()
        sel_index = str(index+1)+'.'
        # Chars:   2        3            40                  2
        print(   " |", sel_index, fullname.ljust(40-5, ' '),"| ")

    print(" | x. Go Back                             |")
    print(" +----------------------------------------+ ")
    index = input("Enter Your Selection: ")
    if index == 'x':
        return False
    # if index is a string of a number in range of the student.friends List
    
    if index.isnumeric():
        idx = int(index) - 1
        if idx < len(student.friends):
            while display_friend_profile(student.friends[idx]):
                pass
            return True
    
    print("...Invalid Input")
    time.sleep(1)
    return True 
    
