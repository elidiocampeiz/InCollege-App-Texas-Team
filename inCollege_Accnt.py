import inCollege_Database as database
import inCollege_CurrentUser as user
from inCollege_Student import *
import time
# This will be used for formatting tex (ensuring lines do not exceed a certain amount for ex)
import textwrap


# function that validates a secure password
def passwordChecker(password):
    contains_upper = False
    contains_digit = False
    contains_alpha = True
    if password == None or len(password) < 7 or len(password) > 13:
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
            print(
                "|*| Password Must Not Contain Alpha-Numeric Characters (e.g. '^', ']', '#') |*|")
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

    plusDone = False
    while (plusDone == False):
        plusChoice = input("Would you like to become a Plus Member for the low monthly price of $10?\nPlus members get special benefits including the ability to send a message to anyone within InCollege.\nNote: Standard members are still able to send messages but they are limited to friends only. Other features may apply.\nPlease input 'Y' if you would like to become a Plus Member, input 'N' if you would prefer to be a Standard Member: ")[0]
        if (plusChoice == 'y' or plusChoice == 'Y'):
            plus = True
            plusDone = True
        elif (plusChoice == 'n' or plusChoice == 'N'):
            plus = False
            plusDone = True
        else:
            print("We're sorry, but that is not a valid input. Please try again.")
            plusDone = False

    # Try to create new student account in DB
    create_account = DB.create_account(
        username, password, firstname, lastname, plus)
    # Get student form DB to call update profile info
    student = DB.get_student_by_username(username)

    if not create_account or not student:
        print("\n|*| Create Account Error |*|")
        return False

    # TODO: Addp functionality to add real friends
    # Add Dummy friends
    # student.add_dummy_friends()
    # Save Dummy Friends
    DB.set_student(student)

    # Get Profile Info
    update_profile_info(DB, student)

    # print("\n|*| You Can Change Profile Later! |*|")

    return True
    # return create_account

    # Add Dummy friends
    #student.add_dummy_friends()
    # Save Dummy Friends
    #DB.set_student(student)

    # Get Profile Info
    update_profile_info(DB, student)

    # print("\n|*| You Can Change Profile Later! |*|")

    return True
    # return create_account


def post_job(fullname, username, DB):
    # Init DB
    # DB = database.Database()

    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
    print("+-------------------+")
    print("|    Post A Job     |")
    print("+-------------------+\n")

    # Get user input
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

    create_job_posting = DB.create_job_posting(
        title, description, employer, location, salary, fullname, username)

    if (create_job_posting == False):
        print("\n|*| Create Job Posting Error |*|")

    return create_job_posting


def remove_job(username, jobTitle, DB):
    # print("Attempting to remove job...")
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            # print("Job found!")
            # print(job)
            if job['poster_id'] == username:
                print("Job poster verified!")
                DB.remove_job_posting(job)
                return True
    return False


# This SHOULD tell you how many messages are in the inbox. Does not currently support...
def display_number_in_inbox(student):
    # ...differentiation between read/unread, but that can be easily modified.
    count = len(student.messages)
    # for message in enumerate(student.messages):
    #     if (message[0]):
    #         count += 1
    if (count > 0):
        print("You have ", count, " messages in your inbox.\n")
        return True
    else:
        return False

# This function searches for job in database using job title.
# It will return true if the job title entered
# by the user results in an existing match, and false otherwise
# It then prints out the details of the Job
def display_job_info(DB, jobTitle):

    # will be true if there is a match
    isFound = False

    # searching for jobtitle match
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            print()
            print("Title: ", job['title'])
            print("Description: ", job['description'])
            print("Employer: ", job['employer'])
            print("Location: ", job['location'])
            print("Salary: ", job['salary'])
            isFound = True

    return isFound

def data_format(date_input):
    if len(date_input) < 10 or not date_input[0].isnumeric or not date_input[1].isnumeric or not date_input[2] =='/' \
        or not date_input[3].isnumeric or not date_input[4].isnumeric or not date_input[5] =='/' \
            or not date_input[6].isnumeric or not date_input[7].isnumeric or not date_input[8].isnumeric \
                or not date_input[9].isnumeric:
        return False
    return True

def date_checker(date_input):
    if not data_format(date_input):
        print("Invalid input. Please type data in mm/dd/yyyy format.")
        return False

    date = date_input.split("/")
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    if (month < 1 or month > 12):
        print("Invalid month input. The month cannot exceed 12 nor be less than 1.")
        return False
    if (day < 1 or day > 31):
        print("Invalid day input. The day cannot exceed 31 nor be less than 1.")
        return False
    if (year < 2010 or year > 2030):
        print("Invalid year input. The year cannot exceed 2030 nor be earlier than 2010.")
        return False
    return True


# This function returns true upon successful completion of whole application
# returns false if only part of the application is filled
# if they already applied for the job it returns false
def apply_for_job(DB, jobTitle, username):

    # Checking if user has already applied
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            # testing, prints all users who have applied
            # print(job['users_applications'])
            for vals in job['users_applied']:
                if vals['username'] == username:
                    print("Application Denied - Already Applied")
                    return False

    hasApplied = False

    print("Enter x at any time to cancel")
    print("      +-----------------+")
    print("     | Job Application |")
    print("      +-----------------+")
    print()
    print("Enter datesin the following format")
    print("mm/dd/yyyy")
    print()
    grad_date = input("Enter Graduation Date: ")
    valid_date = date_checker(grad_date)

    if grad_date == "x":
        return False

    while (valid_date == False):  # If false, keep looping until it is true.
        grad_date = input("Reenter Graduation Date: ")
        if grad_date == "x":
            return False
        valid_date = date_checker(grad_date)

    strt_date = input("Enter Date to Begin Work: ")
    valid_date2 = date_checker(strt_date)

    if strt_date == "x":
        return False

    while (valid_date2 == False):
        strt_date = input("Reenter Date to Begin Work: ")
        if strt_date == "x":
            return False
        valid_date2 = date_checker(strt_date)

    why_me = input("Describe why you are fit for the job: ")
    if why_me == "x":
        return False

    # Creating dictionary with values
    users_application = {'username': username,
                         'graduationdate': grad_date, 'startdate': strt_date, 'whyme': why_me}
    # locating job
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            print("Job found")
            job['users_applied'].append(users_application)
            # print("TEST: User Appended")
            hasApplied = True

    DB.save()
    return hasApplied


def save_job(DB, jobTitle, username):

    # Checking if user has already saved
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            for vals in job['users_saved']:
                if vals == username:
                    print("Save Denied - Already Saved")
                    return False

    hasSaved = False

    # locating job
    for job in DB.data["Jobs"]:
        if job['title'] == jobTitle:
            job['users_saved'].append(username)
            hasSaved = True

    DB.save()
    return hasSaved


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

# Getting School info from student


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

# Gets the Users experience


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
        i += 1
    return True


def clear_accounts():
    database.Database

def display_profile(student):
    # if student.username=='':
    #     # Invalid Input all students must have a username Student
    #     return False

    # student object's dictionary
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
    # ' +' + 40 +  ' +'  = 44 chars
    print(" +----------------------------------------+ ")

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
    print(' |', 'About Me:'.center(40-2, ' '), '| ')
    print(" +----------------------------------------+")
    print(' |', prof_about.center(40-2, ' '), '| ')  # prof_about
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
    
def edit_profile_menu(student):
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
        return True  # continue loop in Home line 966


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
    # 2(' |') + 40('-') + 2('| ) chars
    print(" +----------------------------------------+ ")

    for index, friend in enumerate(student.friends):
        fullname = friend.firstname.capitalize() + ' ' + friend.lastname.capitalize()
        sel_index = str(index+1)+'.'
        # Chars:   2        3            40                  2
        print(" |", sel_index, fullname.ljust(40-5, ' '), "| ")

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

def diplay_sendMessage_list_plus(DB, student):  # Needs Plus functionality DEFCON1
    print(" +----------------------------------------+ ")
    print(" |             Send Message               | ")
    print(" +----------------------------------------+ ")
    print(" |  Select a user to message              | ")
    # 2(' |') + 40('-') + 2('| ) chars
    print(" +----------------------------------------+ ")
    # used for tracking down a given student in a list of ALL students accessed by a Plus Member
    username = []
    #index = 0

    # this references which user to send message to
    dictOfUsers = DB.data["Students"]
    for k in dictOfUsers.keys():
        if k != student.username:
            username.append(k)
        #index += 1
    #index = 0

    #iterating through dictionary
    for index, student_username in enumerate(username):
        if student_username!= student.username:
            fname = dictOfUsers[student_username].firstname.capitalize()
            lname = dictOfUsers[student_username].lastname.capitalize()
            fullname = fname + ' ' + lname
            sel_index = str(index+1)+'.'
            
            print(" |", sel_index, fullname.ljust(40-5, ' '), "| ")

    print(" | x. Go Back                             |")
    print(" +----------------------------------------+ ")
    index = input("Enter Your Selection: ")
    if index == 'x':
        return False
    # if index is a string of a number in range of the student.friends List
    if index.isnumeric():
        idx = int(index) - 1

        if idx < len(DB.data["Students"]):
            # in theory, this might let you take the
            recipient_un = username[idx]
            recipient = DB.get_student_by_username(recipient_un)
            print("|*| NOTE - Enter 'x' to cancel message |*|\n")
            print("Sending message to ", recipient.firstname,
                    " ", recipient.lastname, "\n\n")

            # get user's message
            message_body = input("Enter Message Here: ")
            if message_body == "x":
                return False
            else:
                message = [student, message_body]
                # Add to recipient's messages
                recipient.add_message(message)
                # saving student's method info in database
                DB.set_student(recipient)
                print("Message sent successfully!")
                return True

    print("...Invalid Input")
    time.sleep(1)
    return True


#Prints the student's friends and asks which one's he would like to send a message to
#TODO make a conditional statement in this function that takes care of plus members who can message anyone
def diplay_sendMessage_list(DB, student):
    print(" +----------------------------------------+ ")
    print(" |             Send Message               | ")
    print(" +----------------------------------------+ ")
    print(" |  Select a user to message              | ")
    # 2(' |') + 40('-') + 2('| ) chars
    print(" +----------------------------------------+ ")

    for index, friend in enumerate(student.friends):
        fullname = friend.firstname.capitalize() + ' ' + friend.lastname.capitalize()
        sel_index = str(index+1)+'.'
        # Chars:   2        3            40                  2
        print(" |", sel_index, fullname.ljust(40-5, ' '), "| ")

    print(" | x. Go Back                             |")
    print(" +----------------------------------------+ ")
    index = input("Enter Your Selection: ")
    if index == 'x':
        return False
    # if index is a string of a number in range of the student.friends List
    if index.isnumeric():
        idx = int(index) - 1

        #Sending Message....
        if idx < len(student.friends):
            isSent = send_message(student, student.friends[idx], DB)
            if isSent == "x":
                return False
            else:
                return True
            
    print("...Invalid Input")
    time.sleep(1)
    return True 

# returns true if message is successfully sent, false otherwise
def send_message(student, recipient, DB):
    print("\n|*| NOTE - Enter 'x' to cancel message |*|\n")
    print("|*|Sending message to ", recipient.firstname, " ", recipient.lastname, "|*|\n")

    message_body = input("Enter Message Here: ")# get user's message
    if message_body == "x":
        return False
    else:
        message = [student, message_body]           
        recipient.add_message(message)              # Add to recipient's messages
        DB.set_student(recipient)           #saving student's method info in database
        print("\n... message sent successfully!\n")
        time.sleep(1)
        return True
        
def diplay_inbox(student, DB):
    print(" +----------------------------------------+ ")
    print(" |                Inbox                   | ")
    print(" +----------------------------------------+ ")
    print(" |  Users listed here have messaged you,  | ")
    print(" |  Select a message to view or delete.   | ")
    # 2(' |') + 40('-') + 2('| ) chars
    print(" +----------------------------------------+ ")

    for index, message in enumerate(student.messages): #each message is a dict
        sender = message[0] #arg at 0 is a student object
        sender_fullname = sender.firstname.capitalize() + ' ' + sender.lastname.capitalize()
        sel_index = str(index+1)+'.'
        # Chars:   2        3            40                  2
        print(" |", sel_index, sender_fullname.ljust(40-5, ' '), "| ")

    print(" | x. Go Back                             |")
    print(" +----------------------------------------+ ")
    index = input("Enter Your Selection: ")
    if index == 'x':
        return False
    # if index is a string of a number in range of the student.friends List
    if index.isnumeric():
        idx = int(index) - 1
        if idx < len(student.messages):
            
            msgContainer = student.messages[idx]
            sender = msgContainer[0]
            messageBody = msgContainer[1]
            print("Message from ", sender.firstname.capitalize())
            print()
            print("\t", messageBody)

            print()
            print(" +--------------------------------------+")
            print(" |   Enter '1' to delete Message        |")
            print(" |   Enter '2' to reply                 |")
            print(" |   Enter 'x' to go back to Messaging  |")
            print(" +--------------------------------------+")

            selection = input("Enter Selection: ")

            if selection == "1":
                student.messages.pop(idx)
                print("\n\nMessage successfully deleted\n\n")
                return True
            elif selection == "2":
                isSent = send_message(student, student.messages[idx][0], DB)
                if isSent:
                    return True
                else:
                    return False #if message was not sent
                
            elif selection == "x":
                return False #user wants to go back to message menu





def display_accept_request_menu(DB, student, student_req):
        fullname = student_req.firstname.capitalize() + ' ' + student_req.lastname.capitalize()
        print(" +------------------------------------------------+ ")        
        print(" {}'s Friend Requests".format(fullname))
        print(" +------------------------------------------------+ ")
        print(" | 1. Accept                                      |")
        print(" | 2. Deny                                        |")
        print(" | x. Go Back                                     |")
        print(" +------------------------------------------------+ ")
        selection = input("Enter Your Selection: ")
        if selection == 'x':
            return False # Returns to the previous menu
        elif selection == '1':
            # add student1 as friend of student2 and vice versa
            student.add_friend(student_req)
            student_req.add_friend(student)
            # save them in DB
            DB.set_student(student_req)
            DB.set_student(student)
            DB.remove_friend_request(student.username, student_req.username)
        elif selection == '2':
            DB.remove_friend_request(student.username, student_req.username)
        else:
            print("...Invalid Input")
            time.sleep(1)
            return True # run again invalid input
        return False 

def diplay_friend_request_list(DB, student):
    username_list = DB.data['Friend Requests'].get(student.username) #gets 
    if username_list == None or len(username_list) < 1:
        return False
    print(" +----------------------------------------------+ ")
    print(" |           Pending Friend Requests            | ")
    print(" +----------------------------------------------+ ")
    print(" | Select Friend Request to accept or delete it | ")
    print(" +----------------------------------------------+ ") # 2(' |') + 46('-') + 2('| ) chars
    
    students_list = []
    for username in username_list:
        user = DB.get_student_by_username(username)
        if user:
            students_list.append(user)
        # Else means the from_username of the request belongs to a user that is not part of the DB anymore
    for index, student_request in enumerate(students_list):

        fullname = student_request.firstname.capitalize() + ' ' + student_request.lastname.capitalize()
        sel_index = str(index+1)+'.'
        # Chars:   2        3            40                  2
        print(   " |", sel_index, fullname.ljust(46-5, ' '),"| ")

    print(" | x. To Quit                                   |")
    print(" +----------------------------------------------+ ")
    index = input("Enter Chooice: ")
    if index == 'x':
        return False
    # if index is a string of a number in range of the student.friends List
    
    if index.isnumeric():
        idx = int(index) - 1
        if idx < len(students_list):
            while display_accept_request_menu(DB, student, students_list[idx]):
                pass
            return True
    
    print("...Invalid Input")
    time.sleep(1)
    return True 
    
     
#This function allows user to search for friends by last name, university, or major.
#If there is a match the user is given to send a friend request. 
#If they send a friend request the function returns true.
#If they do not senf a friend request the funct    

def send_friend_request_menu(DB, mystudent):
    print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
    search_value = input("\nType Here: ")
    
    if search_value == 'x':
        return False

    # initializing flag to false. If friend is found it is true.
    found = False

    print("\nSearch Results:")
    #for students in the database
    for username, student in DB.data["Students"].items():
        # If lastname, university, or major matches then print the student's information. (Concatenated space to account for space at end of 'university' and 'major'))
        if student.username != mystudent.username and (student.lastname == search_value.capitalize() or student.lastname == search_value or student.get_education()['university'] == search_value.capitalize()+" " or student.get_education()['major'] == search_value.capitalize()+" "):
            found = True
            print("Username: ", student.username, " | Name: ", student.firstname, " ", student.lastname)
            print("University: ", student.get_education()['university'])
            print("Major: ", student.get_education()['major'])
            
            print("\nEnter \'y\' to send a request to ", student.username, " \nor anything else to continue...")
            isRequest = input("Type Here: ")
            # Check if students are already frieneds
            is_friend = False
            for friend in mystudent.friends:
                if friend.username == student.username:
                    print('\nYou are already friends!\n')
                    time.sleep(1)
                    is_friend = True
                    break

                    
            if isRequest == "y" and not is_friend:
                adding_friend = DB.add_friend_request(student.username, mystudent.username)
                if adding_friend == True:
                    print("Request Sent!\n")
                    time.sleep(1)
                else:
                    print("Request was already sent...\n")
                    time.sleep(1)
            
    if found == False:
        print("...")
        time.sleep(1)
        print("They are not yet a part of the InCollege system yet!\n")
        time.sleep(1)
        return False
    else:
        return True


    print("...Invalid Input")
    time.sleep(1)
    return True


def diplay_job_list(student, DB):
    # print(" +----------------------------------------+ ")
    # print(" |            List of Friends             | ")
    # print(" +----------------------------------------+ ")
    # print(" |  Select Friend to view their profile   | ")
    # 2(' |') + 40('-') + 2('| ) chars
    # print(" +----------------------------------------+ ")
    # Below is the new
    print("          +---------------+")
    print("          |  Job Listing  |         ")
    print("+----------------------------------+")
    print("|      Job Titles Listed Below     |")
    print("+----------------------------------+")
    for index, jobs in enumerate(DB.data["Jobs"]):
        indication = ""
        sel_index = str(index+1)+'.'
        for vals in jobs['users_applied']:
            # means user has already applied
            if vals['username'] == student.username:
                indication = "(Applied)"
        print("| ", sel_index, jobs['title'], indication)

    print("+----------------------------------+")
    print("| To see more about a specific job,|")
    print("| type out the Job Title below;    |")
    print("| or type x to go back.            |")
    print("+----------------------------------+")

    index = input("Enter Your Selection: ")
    if index == 'x':
        return False

    if index.isnumeric():
        idx = int(index) - 1
        if idx < len(DB.data["Jobs"]):
            return idx

    print("...Invalid Input")
    time.sleep(1)
    return True

    # above is the new

#    for index, friend in enumerate(student.friends):
#        fullname = friend.firstname.capitalize() + ' ' + friend.lastname.capitalize()
#        sel_index = str(index+1)+'.'
#        # Chars:   2        3            40                  2
#        print(" |", sel_index, fullname.ljust(40-5, ' '), "| ")

#    print(" | x. Go Back                             |")
#    print(" +----------------------------------------+ ")
#    index = input("Enter Your Selection: ")
#    if index == 'x':
#        return False
    # if index is a string of a number in range of the student.friends List

#    if index.isnumeric():
#        idx = int(index) - 1
#        if idx < len(student.friends):
#            while display_friend_profile(student.friends[idx]):
#                pass
#            return True

#    print("...Invalid Input")
#    time.sleep(1)
#    return True
