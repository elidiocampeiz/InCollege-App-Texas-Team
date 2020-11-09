import pytest
import inCollege_Accnt as accnt
import inCollege_Home as home
import inCollege_CurrentUser as user
import inCollege_Database as database
import inCollege_CurrentUser as user
from inCollege_Student import *
import time
import datetime


time.sleep=lambda x:None

# Test function that asserts whether the passwordChecker() function returned the correct value
@pytest.mark.parametrize("test_password, expected", [("Abcdef1", True), ("Abcdefg", False), ("abcdef1", False), ("Abcde1", False), ("Abcdefghijklm1", False), ("Ab1asd2#", False), ("", False)])
def test_passwordChecker(test_password, expected):
    # passwordChecker() takes a string and returns true if it meets all the requirements for a secure password and false otherwise
    result = accnt.passwordChecker(test_password)
    assert result == expected


# Test Database class
@pytest.fixture(scope="module")
def DB():
    # init database with a testfile
    DB = database.Database("database_test")
    DB.clear()
    return DB


# Create Account Test
@pytest.mark.parametrize("username, password, firstname, lastname, plus, expected",
 [
    (
        "1_acc_username",
        "1_acc_password",
        "1_Firstname",
        "1_Lastname",
        True,
        True,
    ),
    (
        "2_acc_username",
        "2_acc_password",
        "2_Firstname",
        "2_Lastname",
        False,
        True,
    ),
    (
        "3_acc_username",
        "3_acc_password",
        "3_Firstname",
        "3_Lastname",
        False,
        True,
    ),
    (
        "4_acc_username",
        "4_acc_password",
        "4_Firstname",
        "4_Lastname",
        True,
        True,
    ),
    (
        "5_acc_username",
        "5_acc_password",
        "5_Firstname",
        "5_Lastname",
        True,
        True,
    ),
    (
        "6_acc_username",
        "6_acc_password",
        "6_Firstname",
        "6_Lastname",
        True,
        True,
    ),
    (
        "7_acc_username",
        "7_acc_password",
        "7_Firstname",
        "7_Lastname",
        True,
        True,
    ),
    (
        "8_acc_username",
        "8_acc_password",
        "8_Firstname",
        "8_Lastname",
        True,
        True,
    ),
    (
        "9_acc_username",
        "9_acc_password",
        "9_Firstname",
        "9_Lastname",
        True,
        True,
    ),
    (
        "10_acc_username",
        "10_acc_password",
        "10_Firstname",
        "10_Lastname",
        True,
        True,
    ),
    (
        "11_acc_username",
        "11_acc_password",
        "11_Firstname",
        "11_Lastname",
        True,
        False,
    ), # The DB can only have 10 user accounts so if we try to create the 6th the create_account function returns false

])
def test_create_account(DB, username, password, firstname, lastname, plus, expected):
    # create_account() create returning true if the account exists and false otherwise
    result = DB.create_account(username, password, firstname, lastname, plus)
    assert result == expected

# Create Account Test
@pytest.mark.parametrize("username, password, expected",
 [
    # test a correct combination of username and password
    (
        "1_acc_username",
        "1_acc_password",
        True
    ),
    # test a wrong combination of username and password
    (
        "2_acc_username",
        "1_acc_username",
        False
    ),
    # test a correct username and wrong_password
    (
        "1_acc_username",
        "random_wrong_password",
        False
    ),
    # test using a correct username as password
    (
        "1_acc_username",
        "4_acc_password",
        False
    ),


])
def test_login(DB, username, password, expected):
    # loginChecker() authenticates the user login, returning true if the account exists and false otherwise
    result = DB.login(username, password)
    assert result == expected


@pytest.mark.parametrize("title, description, employer, location, salary, name_of_poster, poster_username, expected",
 [
    # test a correct combination of posting job
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_name_of_poster",
        "1_username_of_poster",
        True
    ),
    (
        "2_title",
        "2_description",
        "2_employer",
        "2_location",
        "2_salary",
        "2_name_of_poster",
        "2_username_of_poster",
        True
    ),
    (
        "3_title",
        "3_description",
        "3_employer",
        "3_location",
        "3_salary",
        "3_name_of_poster",
        "3_username_of_poster",
        True
    ),
    (
        "4_title",
        "4_description",
        "4_employer",
        "4_location",
        "4_salary",
        "4_name_of_poster",
        "4_username_of_poster",
        True
    ),
    (
        "5_title",
        "5_description",
        "5_employer",
        "5_location",
        "5_salary",
        "5_name_of_poster",
        "5_username_of_poster",
        True
    ),
    (
        "6_title",
        "6_description",
        "6_employer",
        "6_location",
        "6_salary",
        "6_name_of_poster",
        "6_username_of_poster",
        True
    ),
    (
        "7_title",
        "7_description",
        "7_employer",
        "7_location",
        "7_salary",
        "7_name_of_poster",
        "7_username_of_poster",
        True
    ),
    (
        "8_title",
        "8_description",
        "8_employer",
        "8_location",
        "8_salary",
        "8_name_of_poster",
        "8_username_of_poster",
        True
    ),
    (
        "9_title",
        "9_description",
        "9_employer",
        "9_location",
        "9_salary",
        "9_name_of_poster",
        "9_username_of_poster",
        True
    ),
    (
        "10_title",
        "10_description",
        "10_employer",
        "10_location",
        "10_salary",
        "10_name_of_poster",
        "10_username_of_poster",
        True
    ),
    (
        "11_title",
        "11_description",
        "11_employer",
        "11_location",
        "11_salary",
        "11_name_of_poster",
        "11_username_of_poster",
        False
    ),
])

def test_create_job_posting(DB, title, description, employer, location, salary, name_of_poster, poster_username, expected):
    date = datetime.datetime.now()
    
    result = DB.create_job_posting(title, description, employer, location, salary, name_of_poster, poster_username, date)
    assert result == expected

############ TEST REMOVE JOB POSTING ############
@pytest.mark.parametrize(" username, jobTitle, expected",
 [
    (
        '10_username_of_poster',
        '10_title',
        True
    ),
    # Test a valid username that is not the poster
    (
        '1_username_of_poster',
        '10_title',
        False
    ),
    # Test an invalid username 
    (
        'invalid_username',
        '10_title',
        False
    ),
    # Test an invalid title 
    (
        '10_username_of_poster',
        'invalid_title',
        False
    ),

 ])
# Test Accnt function that searches, validates and removes job posting
def test_remove_job(DB, username, jobTitle, expected):
    result = accnt.remove_job(username, jobTitle, DB)
    assert result == expected

# Test database function that removes job posting
def test_remove_job_posting(DB):
    for job in DB.data["Jobs"]:
        assert DB.remove_job_posting(job) == True

# For multiple inputs create a function to be passed to the monkeypatch.setattr that return a string to the respective input call
def fake_inputs(key, firstname, lastname):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "--> First Name: ": firstname,
        "--> Last Name: ": lastname,
    }
    val = prompt_to_return_val[key]
    return val

# Create search_users
@pytest.mark.parametrize("firstname, lastname, expected",
 [
    # Test correct first and name input
    (
        "1_Firstname",
        "1_Lastname",
        True
    ),
    # Test a wrong first name input
    (
        "1_Lastname",
        "1_Lastname",
        False
    ),
    # Test a wrong last name input
    (
        "1_Firstname",
        "1_Firstname",
        False
    ),
    # Test null input
    (
        "",
        "",
        False
    ),
])
def test_search_users(DB, monkeypatch, firstname, lastname, expected):

    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: fake_inputs(x, firstname, lastname))
        # m.setattr('sys.stdin', ans2)
        result = DB.search_users()
        # result = userInputFucntion()
        assert result == expected

def test_clear(DB):
    DB.clear()
    reset_DB_data = {"Students":{}, "Jobs":[], 'Friend Requests': {}}
    DB.load()
    assert DB.data == reset_DB_data
    assert DB.accFull == False
    assert DB.jobFull == False

def test_reset(DB):
    DB.reset()
    reset_DB_data = {"Students":{}, "Jobs":[], 'Friend Requests': {}}
    assert DB.data == reset_DB_data
    assert DB.accFull == False
    assert DB.jobFull == False

def test_load(DB):
    filename = DB.filename
    DB.filename = None
    assert DB.filename == None
    DB.load(filename)
    assert DB.filename == filename

def test_save(DB):
    assert "test_save" not in  DB.data.keys()
    DB.data["test_save"] = True
    DB.save()
    assert "test_save" in  DB.data.keys()
    DB.clear()

# Create Account Test (inCollege_Acct.py)
def create_accout_menu_fake_inputs(key, new_username, new_password, passwordCheck, new_firstname, new_lastname,plus ='Y'):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter username: ": new_username,
        "Enter password: ": new_password,
        "Enter New Password: ": passwordCheck,
        "Enter First Name: ": new_firstname,
        "Enter Last Name: ": new_lastname,
       "Would you like to become a Plus Member for the low monthly price of $10?\nPlus members get special benefits including the ability to send a message to anyone within InCollege.\nNote: Standard members are still able to send messages but they are limited to friends only. Other features may apply.\nPlease input 'Y' if you would like to become a Plus Member, input 'N' if you would prefer to be a Standard Member: ": plus, 
    }
    if not key in prompt_to_return_val.keys():
        return ''
    val = prompt_to_return_val[key]
    return val

# Create Account Test
@pytest.mark.parametrize("new_username, new_password, passwordCheck, new_firstname, new_lastname, expected",
 [
    (
        "1accusername",
        "1Password",
        "Pass123",
        "1Firstname",
        "1Lastname",
        True
    ),
    # invalid password input, default to 'Pass123', pass the test
    (
        "2accusername",
        "2password",
        "Pass123",
        "2Firstname",
        "2Lastname",
        True
    ),
    # invalid username already exists input
    (
        "1accusername",
        "3password",
        "Pass123",
        "3Firstname",
        "3Lastname",
        False
    ),
    # 'q' in the username field
    (
        "x",
        "4Password",
        "Pass123",
        "4Firstname",
        "4Lastname",
        False
    ),
    # 'q' in the password field
    (
        "4accusername",
        "x",
        "Pass123",
        "4Firstname",
        "4Lastname",
        False
    ),
    # invalid password and 'q' in the Default password field
    (
        "4accusername",
        "4password",
        "x",
        "4Firstname",
        "4Lastname",
        False
    ),
    (
        "3accusername",
        "3Password",
        "Pass133",
        "3Firstname",
        "3Lastname",
        True
    ),
    (
        "4accusername",
        "4Password",
        "Pass143",
        "4Firstname",
        "4Lastname",
        True
    ),
    (
        "5accusername",
        "5Password",
        "Pass153",
        "5Firstname",
        "5Lastname",
        True
    ),
    # The DB can only have 5 user accounts so if we try to create the 6th the create_account function returns false
    (
        "6_acc_username",
        "6Password",
        "Pass153",
        "6_Firstname",
        "6_Lastname",
        True
    ),
    (
        "7_acc_username",
        "7Password",
        "Pass153",
        "7_Firstname",
        "7_Lastname",
        True
    ),
    (
        "8_acc_username",
        "8Password",
        "Pass153",
        "8_Firstname",
        "8_Lastname",
        True
    ),
    (
        "9_acc_username",
        "9Password",
        "Pass153",
        "9_Firstname",
        "9_Lastname",
        True
    ),
    (
        "10_acc_username",
        "10Password",
        "Pass153",
        "10_Firstname",
        "10_Lastname",
        True
    ),
    (
        "11_acc_username",
        "11Password",
        "Pass153",
        "11_Firstname",
        "11_Lastname",
        False
    ), # The DB can only have 10 user accounts so if we try to create the 6th the create_account function returns false

])

def test_create_accout_menu(DB, monkeypatch, new_username, new_password, passwordCheck, new_firstname, new_lastname, expected ):

    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: create_accout_menu_fake_inputs(x, new_username, new_password, passwordCheck, new_firstname, new_lastname)) # NOTE: THE PLUS VARIABLE DEFAULTS TO 'Y' since its not important for the function functionality
        # print('BREAKPOINT db is full ', DB.isFull, len(DB.data["Students"]) )
        result = accnt.create_account(DB)
        assert result == expected


def login_fake_inputs(key, username, password):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Your Username: ": username,
        "Enter Your Password: ": password
    }
    val = prompt_to_return_val[key]

    return val

@pytest.mark.parametrize("username, password, expected",
 [
    # Test correct combination of username and password input
    (
        "1accusername",
        "1Password",
        True
    ),
    # Test incorrect password input
    (
        "1accusername",
        "1accusername",
        False
    ),
    # Test incorrect username input
    (
        "2accusername",
        "1Password",
        False
    ),
    # Test quit, case 1
    (
        "q",
        "1Password",
        False
    ),
    # Test quit, case 2
    (
        "1accusername",
        "q",
        False
    ),
    # Todo: 3 more cases
])
# Test Login Acc
def test_login_menu(DB, monkeypatch, username, password, expected):

    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: login_fake_inputs(x, username, password))
        # m.setattr('sys.stdin', ans2)
        result = accnt.login(DB)

        # result = userInputFucntion()
        if result == False:
            assert result == expected
        else:
            #print('result.name', result.name)
            assert result.username != ''


def post_job_fake_inputs(key, title, description, employer, location, salary, expected):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Job Title: ": title,
        "Enter Job Description: ": description,
        "Enter Employer For Job: ": employer,
        "Enter Job Location: ": location,
        "Enter Job Salary: ": salary
    }
    val = prompt_to_return_val[key]
    return val

# Post Job Parameters
@pytest.mark.parametrize("title, description, employer, location, salary, fullname, username_of_poster, expected",
 [
    # test a correct combination of jobs and names
    (
        "",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
        "1_username_of_poster",
        False
    ),
    # test a correct combination of jobs and names
    (
        "1_title",
        "",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
        "1_username_of_poster",
        False
    ),
    # test a correct combination of jobs and names
    (
        "1_title",
        "1_description",
        "",
        "1_location",
        "1_salary",
        "1_fullname",
        "1_username_of_poster",
        False
    ),
    # test a correct combination of jobs and names
    (
        "1_title",
        "1_description",
        "1_employer",
        "",
        "1_salary",
        "1_fullname",
        "1_username_of_poster",
        False
    ),
    # test a correct combination of jobs and names
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "",
        "1_fullname",
        "1_username_of_poster",
        False
    ),
    # test a correct combination of jobs and names
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "",
        "1_username_of_poster",
        False
    ),
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
        "",
        False
    ),
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
        "1_username_of_poster",
        True
    ),
])
#Post Job Test
def test_post_job(monkeypatch, DB, title, description, employer, location, salary, fullname, username_of_poster, expected ):
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: post_job_fake_inputs(x, title, description, employer, location, salary, expected))
        result = accnt.post_job(fullname, username_of_poster, DB)
        assert result == expected


def intro_menu_fake_inputs(key, selection, validSelection):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Your Selection:\n":selection,
        "Enter Your Selection: ":validSelection,
    }
    val = prompt_to_return_val[key]
    return val

# Test for intro menu
@pytest.mark.parametrize("selection, validSelection, expected",
 [
    # Test correct first input, case 1
    (
        "1",
        "1",
        True,
    ),
    # Test correct first input, case 2
    (
        "0",
        "0",
        False,
    ),
    # Test incorrect first input, case 1
    (
        "wrong",
        "1",
        True,
    ),
    # Test incorrect first input, case 2
    (
        "wrong",
        "0",
        False,
    ),
])
def test_intro_menu(monkeypatch, selection, validSelection, expected):
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: intro_menu_fake_inputs(x, selection, validSelection))
        assert expected == home.mainMenuIntroMessage()

@pytest.mark.parametrize("username, expected",
 [
    
    (
        "wrong_username",
        False,
    ),
    (
        "",
        False,
    ),
    (
        "1accusername",
        True,
    ),
 
])
#Test for get student by username
def test_get_student_by_username(DB, username, expected):
    student = DB.get_student_by_username(username)
    if student:
        assert student.username == username
    else:
        assert student == False


@pytest.mark.parametrize("username, update_dict , expected",
 [
        (
            '1accusername',
            {  
                'settings':
                {
                    'guest control' : 
                    {
                        "Email" : False, 
                        "SMS" : True,  
                        "Targeted Advertising" : False
                    },
                    "language" : 'English'
                }
            },
            True
        ),
        (
            '1accusername',
            {  
                'title':
                {
                    'Computer Science Student' 
                }
            },
            True
        ),
        (
            '1accusername',
            {  
                'About':
                {
                    'Computer Science Student' 
                }
            },
            True
        ),
        # Test a username that doesn't exist in DB
        (
            'wrong_username',
            {  
                'About':
                {
                    'Computer Science Student' 
                }
            },
            False
        ),
        # Test a username da doesn't exist in DB
        (
            '',
            {  
                'settings':
                {
                    'guest control' : 
                    {
                        "Email" : False, 
                        "SMS" : True,  
                        "Targeted Advertising" : False
                    },
                    "language" : 'English'
                }
            },
            False
        )
])
def test_set_student(DB, username, update_dict, expected):
    # Get student from DB
    myStudent = DB.get_student_by_username(username)
    # If get_student_by_username returns False (username is not in DB) construct an empty student (update should return False, expected value is False)
    if not myStudent:
        myStudent = Student(username=username)
    # Update local student
    myStudent.update(**update_dict)    
    # Update student in DB 
    result = DB.set_student(myStudent)
    # Get student from DB 
    new_Student = DB.get_student_by_username(username)
    # IF update was correct, asser if each update in update_dict was performed
    if result:
        for key, updated_value in update_dict.items():
            # print(myStudent.__dict__.get(key),updated_value )
            assert (new_Student.__dict__.get(key) == updated_value) == expected
    
    # If update failed then it means Student wasn't in DB, expected should be false
    assert result == expected

# Fixture for defauld student object
@pytest.fixture (scope = "module")
def default_Student(DB): 
    guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
    # laguage settings
    language = "English"
    settings = {'guest control' : guest_control, "language" : language} 
    # language settings
    # Init new student 
    new_student = {'username':"1accusername", 'password':"New_password1",'firstname':"John", 'lastname':"Smith", 'settings': settings}
    # my_student = Student(**new_student)
    # return new_student

    # Init Student 
    student = Student(**new_student)
    
    # Add student to DB
    DB.create_account(student.username, student.password, student.firstname, student.lastname, False)
    
    return student

@pytest.fixture (scope = "module")
def default_Student2(DB): 
    guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
    # laguage settings
    language = "English"
    settings = {'guest control' : guest_control, "language" : language} 
    # language settings
    # Init new student 
    new_student = {'username':"2accusername", 'password':"New_password1",'firstname':"John", 'lastname':"Smith", 'settings': settings}
    # my_student = Student(**new_student)
    # return new_student

    # Init Student 
    student = Student(**new_student)
    # Add student to DB
    DB.create_account(student.username, student.password, student.firstname, student.lastname, True)

    return student

@pytest.mark.parametrize(" update_dict",
 [
        
    (
        {
            'settings':
                {
                    'guest control':
                    {
                        "Email": False,
                        "SMS": True,
                        "Targeted Advertising": False
                    },
                    "language": 'Spanish'
                }
        }
    ),
    (
        {
            'title': 'Computer Science Student'
        }
    ),
    (
        {
            'About': 'Computer Science Student'  # doesn't matter what value is
        }
    ),
    # Test a username da doesn't exist in DB
    (
        {
            'About':'Computer Science Student'
        }   
    ),
    # Test a username da doesn't exist in DB
    (
        {
            'settings':
            {
                'guest control':
                {
                    "Email": False,
                    "SMS": True,
                    "Targeted Advertising": False
                },
                "language": 'English'
            }
        }
    )
])
def test_student_update(default_Student, update_dict):
    # student = Student(**default_Student)
    # student = default_Student
    default_Student.update(**update_dict)

    for key, updated_value in update_dict.items():
        print(default_Student.key)
        assert default_Student.__dict__.get(key) == updated_value


@pytest.mark.parametrize("title, employer, start_date, end_date, location, description, expected",
 [
    # Test 
    (  
        'title1',
        'employer1',
        'start_date1',
        'end_date1',
        'location1',
        'description1',
        True
    ),
    (  
        'title2',
        'employer2',
        'start_date2',
        'end_date2',
        'location2',
        'description2',
        True
    ),
    (  
        'title3',
        'employer3',
        'start_date3',
        'end_date3',
        'location3',
        'description3',
        True
    ),
    # Maximum of 3 Job Experiences -> False
    (  
        'title4',
        'employer4',
        'start_date4',
        'end_date4',
        'location4',
        'description4',
        False
    ),
])
def test_student_add_job_experience(default_Student,title, employer, start_date, end_date, location, description, expected):
    # student = default_Student

    result = default_Student.add_job_experience(title, employer, start_date, end_date, location, description)
    
    assert result == expected

@pytest.mark.parametrize("index, expected",
 [
    (
        0,
        True
    ),
    (
        1,
        True
    ),
    (
        2,
        True
    ),
    (
        4,
        False
    ),
])
def test_student_get_experience(default_Student, index, expected):
    
    result = default_Student.get_experience(index)
    if result:
        assert isinstance(result, dict)
    else:
        assert result == expected

@pytest.mark.parametrize("university, major, year",
 [
    (
        'University of South Florida',
        'Computer Science',
        'Senior',
    ),
    (
        'University of South Carolina',
        'Computer Engineering',
        'Freshman',
    ),
])
def test_student_set_education(default_Student, university, major, year):
    default_Student.education = {}
    default_Student.set_education(university, major, year)
    
    assert default_Student.education['university'] == university
    assert default_Student.education['major'] == major
    assert default_Student.education['year'] == year

@pytest.mark.parametrize("friend_username",
 [
    (
        
        'JohnSmith',
    ),
    (
        
        'JaneDoe',
    ),
    (
        
        'MarkPolo',
    ),
    (
        
        'MariaSilva',
    ), 
])
def test_student_add_friend(default_Student, friend_username):
    student_dict = default_Student.__dict__.copy()
    student_dict['username'] = friend_username
    friend = Student(**student_dict)
    default_Student.add_friend(friend)

    assert friend in default_Student.friends

# title, about, university, major, year, job_title, employer, start_date, end_date, location, description
def profile_fake_inputs(key, **kwargs):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {                                                                                # Avoid the error of trying to access a nonexistent key in kwargs using in line if 
        # Keys if input() function                                          # Value depending on kwargs     # Use the same fake arguments to test all profile menus
        "Enter a title for your profile: ":                                 kwargs['title']                 if kwargs.get('title')          != None else '',
        "Enter the about section of your profile: ":                        kwargs['about']                 if kwargs.get('about')          != None else '',
        "Enter your University: ":                                          kwargs['university']            if kwargs.get('university')     != None else '',
        "Enter your Major: ":                                               kwargs['major']                 if kwargs.get('major')          != None else '',
        "Enter Your Status Year (Freshman, Sophomore, Junior, Senior): ":   kwargs['year']                  if kwargs.get('year')           != None else '',
        "Enter Job Title: ":                                                kwargs['job_title']             if kwargs.get('job_title')      != None else '',
        "Enter Job Description: ":                                          kwargs['description']           if kwargs.get('description')    != None else '',
        "Enter Employer For Job: ":                                         kwargs['employer']              if kwargs.get('employer')       != None else '',
        "Enter Job Location: ":                                             kwargs['location']              if kwargs.get('location')       != None else '',
        "Enter the Date you Started: ":                                     kwargs['start_date']            if kwargs.get('start_date')     != None else '',
        "Enter The Date You Ended: ":                                       kwargs['end_date']              if kwargs.get('end_date')       != None else '',
        
    }
    val = prompt_to_return_val[key]
    return val

@pytest.mark.parametrize("title, about, university, major, year, job_title, employer, start_date, end_date, location, description, expected",
 [
    (
        
        'title1', 'about1', 'university1', 'major1', 'year1', 'job_title1', 'employer1', 'start_date1', 'end_date1', 'location1', 'description1', True,
    ),
    (
        
        'title2', 'about2', 'university2', 'major2', 'year2', 'job_title2', 'employer2', 'start_date2', 'end_date2', 'location2', 'description2', True,
    ),
    (
        
        'title3', 'about3', 'university3', 'major3', 'year3', 'job_title3', 'employer3', 'start_date3', 'end_date3', 'location3', 'description3', True,
    ),
    (
        
        'x', 'about4', 'university4', 'major4', 'year4', 'job_title4', 'employer4', 'start_date4', 'end_date4', 'location4', 'description4', False,
    ),
    (
        
        'title5', 'x', 'university5', 'major5', 'year5', 'job_title5', 'employer5', 'start_date5', 'end_date5', 'location5', 'description5', False,
    ),
    (
        
        'title6', 'about6', 'x', 'major6', 'year6', 'job_title6', 'employer6', 'start_date6', 'end_date6', 'location6', 'description6', False,
    ),
    (
        
        'title7', 'about7', 'university7', 'x', 'year7', 'job_title7', 'employer7', 'start_date7', 'end_date7', 'location7', 'description7', False,
    ),
    (
        
        'title8', 'about8', 'university8', 'major8', 'x', 'job_title8', 'employer8', 'start_date8', 'end_date8', 'location8', 'description8', False,
    ),
    (
        
        'title9', 'about9', 'university9', 'major9', 'year9', 'x', 'employer9', 'start_date9', 'end_date9', 'location9', 'description9', False,
    ),
    (
        
        'title10', 'about10', 'university10', 'major10', 'year10', 'job_title10', 'x', 'start_date10', 'end_date10', 'location10', 'description10', False,
    ),
    (
        
        'title11', 'about11', 'university11', 'major11', 'year11', 'job_title11', 'employer11', 'x', 'end_date11', 'location11', 'description11', False,
    ),
    (
        
        'title12', 'about12', 'university12', 'major12', 'year12', 'job_title12', 'employer12', 'start_date12', 'x', 'location12', 'description12', False,
    ),
    (
        
        'title13', 'about13', 'university13', 'major13', 'year13', 'job_title13', 'employer13', 'start_date13', 'end_date13', 'x', 'description13', False,
    ),
    (
        
        'title14', 'about14', 'university14', 'major14', 'year14', 'job_title14', 'employer14', 'start_date14', 'end_date14', 'location14', 'x', False,
    ),
])
def test_update_profile_info(DB, default_Student, monkeypatch, title, about, university, major, year, job_title, employer, start_date, end_date, location, description, expected):
    
    
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        kwargs={'title':title, 'about':about, 'university':university, 'major':major, 'year':year, 'job_title':job_title, 'employer':employer, 'start_date':start_date, 'end_date':end_date, 'location':location, 'description':description}
        m.setattr('builtins.input', lambda x: profile_fake_inputs(x, **kwargs))

        result = accnt.update_profile_info(DB, default_Student)
        assert result == expected
        
@pytest.mark.parametrize(" university, major, year, expected",
 [
    (
        
        'university1', 'major1', 'year1', True,
    ),
    (
        
        'x', 'major1', 'year1', False,
    ),
    (
        
        'university1', 'x', 'year1', False,
    ),
    (
        
        'university1', 'major1', 'x', False,
    ),
])
def test_update_education_info(DB, default_Student, monkeypatch, university, major, year, expected):
    
    
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        kwargs={ 'university':university, 'major':major, 'year':year }
        m.setattr('builtins.input', lambda x: profile_fake_inputs(x, **kwargs))

        result = accnt.update_education_info(DB, default_Student)
        assert result == expected
        

@pytest.mark.parametrize(" job_title, employer, start_date, end_date, location, description, expected",
 [
    (
        
        'job_title1', 'employer1', 'start_date1', 'end_date1', 'location1', 'description1', True,
    ),
    (
        
        'x', 'employer2', 'start_date2', 'end_date2', 'location2', 'description2', False,
    ),
    (
        
        'job_title3', 'x', 'start_date3', 'end_date3', 'location3', 'description3', False,
    ),
    (
        
        'job_title4', 'employer4', 'x', 'end_date4', 'location4', 'description4', False,
    ),
    (
        
        'job_title5', 'employer5', 'start_date5', 'x', 'location5', 'description5', False,
    ),
    (
        
        'job_title6', 'employer6', 'start_date6', 'end_date6', 'x', 'description6', False,
    ),
    (
        
        'job_title7', 'employer7', 'start_date57', 'end_date7', 'location7', 'x', False,
    ),
])
def test_update_experience_info(DB, default_Student, monkeypatch, job_title, employer, start_date, end_date, location, description, expected):
    
    
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        kwargs={ 'job_title':job_title, 'employer':employer, 'start_date':start_date, 'end_date':end_date, 'location':location, 'description':description}
        m.setattr('builtins.input', lambda x: profile_fake_inputs(x, **kwargs))

        result = accnt.update_experience_info(DB, default_Student)
        assert result == expected
        
# test add_dummy_friends function
def test_add_dummy_friends(default_Student):
    # Delete all friends
    default_Student.friends = []
    # functions adds 2 dummy friends to the Student
    default_Student.add_dummy_friends()
    # Assert frinds lentgh is not zero
    assert len(default_Student.friends) > 0


# def edit_profile_fake_inputs(key, selection):
#     # Each Key has to be the same string as the respective input statement
#     prompt_to_return_val = {
#         "Enter Your Selection: ":selection,
#     }
#     val = prompt_to_return_val[key]
#     return val

@pytest.mark.parametrize("selection, expected",
 [
    (
        
        '1', True,
    ),
    (
        
        'x', False,
    ),
    (
        
        'worng_string',  True,
    ),
])
def test_edit_profile_menu(monkeypatch, default_Student, selection, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: selection)
        result = accnt.edit_profile_menu(default_Student)
        assert result == expected 

@pytest.mark.parametrize("selection, expected",
 [
    (
        
        'x', False,
    ),
    (
        
        'random_string',  True,
    ),
])
def test_display_friend_profile(monkeypatch, default_Student, selection, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: selection)
        result = accnt.display_friend_profile(default_Student)
        assert result == expected

@pytest.mark.parametrize("selection, expected",
 [
    (
        
        '1', True,
    ),
    (
        
        '2', True,
    ),
    (
        
        'x', False,
    ),
    (
        
        'worng_string',  True,
    ),
])
def test_diplay_friend_list(monkeypatch, default_Student, selection, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: selection)
        result = accnt.display_friend_profile(default_Student)
        assert result == expected

# test that uses capsys to capture the output of print functions 
# such that we can test whether display_profile printed anything
def test_display_profile(capsys, default_Student):
    accnt.display_profile(default_Student)
    captured = capsys.readouterr()
    assert captured.out != ''

@pytest.mark.parametrize("to_username, from_username, expected",
 [
    (
        
        'username1','username2', True, # 2nd if -> New valid request
    ),
    (
        
        'username1','username2', False, # 3rd if -> Request already exists return false
    ),
    (
        
        'username1','username3', True, # 4th if -> additional valid request
    ),
    (
        
        'username1','username1',  False, # 1st if -> invalid request
    ),
])
def test_add_friend_request(DB, to_username, from_username, expected):
    result = DB.add_friend_request(to_username, from_username)
    assert result == expected

@pytest.mark.parametrize("to_username, from_username, expected",
 [
    (
        
        'username1','username2', True, # 3nd if -> More than one Request with to_username
    ),
    (
        
        'username1','username2', False, # 2th if -> # Nothing to remove with from_username
    ),
    (
        
        'username1','username3', True, # 4rd if -> Last Request with to_username
    ),
    (
        
        'username1','username3', False, # 2th if -> # Nothing to remove with to_username
    ),
    (
        
        '','username3', False, # 2th if -> # Nothing to remove with invalid to_username
    ),
    (
        
        'username1','username1',  False, # 1st if -> invalid removal 
    ),
])
def test_remove_friend_request(DB, to_username, from_username, expected):
    result = DB.remove_friend_request(to_username, from_username)
    assert result == expected

def friend_request_menu_fake_inputs(key, search_value, isRequest, ):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "\nType Here: ":            search_value,
        "Type Here: ":              isRequest,
    }
    val = prompt_to_return_val[key]
    return val

@pytest.mark.parametrize("isRequest, search_value, expected",
 [
    (
        
        'y','University of Central Florida', False, # inalid Search
    ),
    (
        
        'y','Smith', True, # Found 
    ),
    (
        
        'x','Smith', True, # Found but request already created
    ),
    (
        
        'x','CS', False, # 4rd if -> Last Request with to_username
    ),
    
])
def test_send_friend_request_menu(monkeypatch, DB, default_Student, default_Student2, search_value, isRequest, expected):
    # a = DB.set_student(default_Student)
    # b = DB.set_student(default_Student2)
    
    # print(a,b)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: friend_request_menu_fake_inputs(x, search_value, isRequest))
        result = accnt.send_friend_request_menu(DB, default_Student2)
        assert result == expected

def diplay_friend_request_list_fake_inputs(key, request_list_selection, accept_selection ):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Your Selection: ":   accept_selection, # 1 or 2 or x
        "Enter Chooice: ":          request_list_selection, # number (1) or x
    }
    val = prompt_to_return_val[key]
    return val

@pytest.mark.parametrize("request_list_selection, accept_selection, expected",
 [
    (
        
        '1','1', True, # Select Accept Request 1 
    ),
    (
        
        '1','1', False, # no pending requests
    ),
    (
        
        'x','1', False, # Quit
    ),
    
])
def test_diplay_friend_request_list(monkeypatch, DB, default_Student, default_Student2,request_list_selection, accept_selection, expected):
    
    # DB.add_friend_request(default_Student.username, 'fakeusername2')
    # print('lenth: ',len( DB.data['Friend Requests'][default_Student.username]))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: diplay_friend_request_list_fake_inputs(x, request_list_selection, accept_selection))
        result = accnt.diplay_friend_request_list(DB, default_Student)
        assert result == expected



@pytest.mark.parametrize("request_list_selection, accept_selection, expected",
 [
    (
        
        '1','1', False, # Select Accept Request 1 
    ),
    (
        
        '1','1', False, # no pending requests
    ),
    (
        
        'x','4', True, # invalid input selection
    ),
    
])
def test_diplay_friend_request_list(monkeypatch, DB, default_Student, default_Student2,request_list_selection, accept_selection, expected):
    
    DB.add_friend_request(default_Student.username, default_Student2.username)
    # print('lenth: ',len( DB.data['Friend Requests'][default_Student.username]))
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: diplay_friend_request_list_fake_inputs(x, request_list_selection, accept_selection))
        result = accnt.display_accept_request_menu(DB, default_Student, default_Student2)
        assert result == expected

def apply_for_job_fake_inputs(key, graduation_date, graduation_date2, start_date, start_date2, why_me):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Graduation Date: ":graduation_date,
        "Reenter Graduation Date: ":graduation_date2,
        "Enter Date to Begin Work: ":start_date,
        "Reenter Date to Begin Work: ":start_date2,
        "Describe why you are fit for the job: ":why_me,
    }
    val = prompt_to_return_val[key]
    return val


@pytest.mark.parametrize(" jobTitle, username, graduation_date, graduation_date2, start_date, start_date2, why_me, expected",
 [
    (
        
        'job_title1', 
        'username', 
        '01/01/2020', 
        '01/01/2020', 
        '02/01/2020', 
        '02/01/2020', 
        'whyMe1', 
        True,
    ),
    # Already applied -> False
    (
        'job_title1', 
        'username', 
        '01/01/2020', 
        '01/01/2020', 
        '02/01/2020', 
        '02/01/2020', 
        'whyMe1', 
        False,
    ),
    (
        'job_title2', 
        'username2', 
        '01/01',         # grad_date check
        '01/01/2020', 
        '02/01',         # start_date check
        '02/01/2020', 
        'whyMe2', 
        True,
    ),
    # Incomplete application -> False
    (
        'job_title2', 
        'username2', 
        'x',            # Exit
        '01/01/2020', 
        '02/01', 
        '02/01/2020', 
        'whyMe2', 
        False,
    ),
    # Incomplete application -> False
    (
        'job_title2', 
        'username2', 
        '01/01',        # invalid date
        'x',            # Exit 
        '02/01', 
        '02/01/2020', 
        'whyMe2', 
        False,
    ),
    # Incomplete application -> False
    (
        'job_title2', 
        'username2', 
        '01/01/2020', 
        '01/01/2020', 
        'x',            # Exit
        '02/01/2020', 
        'whyMe2', 
        False,
    ),
    # Incomplete application -> False
    (
        'job_title2', 
        'username2', 
        '01/01/2020', 
        '01/01/2020', 
        '02/01',        # invalid date
        'x',            # Exit
        'whyMe2', 
        False,
    ),
    # Incomplete application -> False
    (
        'job_title2', 
        'username2', 
        '01/01/2020', 
        '01/01/2020', 
        '02/01/2020', 
        '02/01/2020', 
        'x',            # Exit
        False,
    ),
])
def test_apply_for_job(monkeypatch,default_Student, DB, jobTitle, username, graduation_date, graduation_date2, start_date, start_date2, why_me, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: apply_for_job_fake_inputs(x, graduation_date, graduation_date2, start_date, start_date2, why_me))
        date = datetime.datetime.now()
        DB.create_job_posting(jobTitle,"10_description", "10_employer","10_location","10_salary","10_name_of_poster",username,date)
        result = accnt.apply_for_job(DB, jobTitle, username, default_Student)
        
        assert result == expected

@pytest.mark.parametrize("jobTitle, username, expected",
 [
    (
        
        'jobTitle1','username1', True, # -> True
    ),
    (
        
        'jobTitle1','username1', False, # Already saved -> False
    ),
    (
        
        'wrong_jobTitle','username2', False, # wrong jobTitle -> False
    ),
])
def test_save_job(DB, jobTitle, username, expected):
    
    if expected:
        date = datetime.datetime.now()
        DB.create_job_posting(jobTitle,"10_description", "10_employer","10_location","10_salary","10_name_of_poster",username,date)
    result = accnt.save_job(DB, jobTitle, username)
    
    assert result == expected

@pytest.mark.parametrize("jobTitle, expected", 
[
    (
        "jobTitle1", True
    ), 
    (
        "wrong_jobTitle", False
    )
])
def test_display_job_info(DB, jobTitle, expected):
    result = accnt.display_job_info(DB, jobTitle)
    assert result == expected

@pytest.mark.parametrize("selection, expected", 
[
    (
        "5", True
    ), 
    (
        "2", True
    ), 
    (
        "0", False
    ), 
    (
        "13asasd", True
    ), 
    (
        "x", False
    ), 
    
])
def test_diplay_job_list(monkeypatch, default_Student, DB, selection, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: selection)
        result = accnt.diplay_job_list(default_Student, DB)
        if isinstance(result, int):
            assert result < len(DB.data["Jobs"])
        else:
            assert result == expected

#Test data_format
@pytest.mark.parametrize("test_date_input, expected", 
[
    (
        "0d/14/2015", False
    ), 
    (
        "25614/2015", False
    ), 
    (
        "04/0/2015", False
    ),
    (
        "0434/2015", False
    ),
    (
        "04/14/2015", True
    ),
])
def test_date_checker(test_date_input, expected):
    result = accnt.data_format(test_date_input)
    assert result == expected

#Test date_checker
@pytest.mark.parametrize("test_date_input, expected", 
[
    (
        "00/14/2015", False
    ), 
    (
        "25/14/2015", False
    ), 
    (
         "04/00/2015", False
    ),
    (
        "04/34/2015", False
    ),
    (
        "04/14/2005", False
    ), 
    (
        "04/14/2040", False
    ),
    (
        "04/14/2015", True
    ),
])
def test_date_checker(test_date_input, expected):
    result = accnt.date_checker(test_date_input)
    assert result == expected

#Test Student add_message
@pytest.mark.parametrize("message", 
[
    (
        "MESSAGE1",
    ), 
    (
        "MESSAGE2",
    ), 
    (
        "MESSAGE3",
    ),
    (
        "MESSAGE4",
    ),
    (
        "",
    ),
])
def test_student_add_message(default_Student, message):
    default_Student.add_message(message)
    
    assert message in default_Student.messages

@pytest.mark.parametrize("message, expected", 
[
    (
        "MESSAGE1", True
    ), 
    (
        "xMESSAGE2", True
    ),
    (
        "x", False
    ),
])
def test_send_message(monkeypatch, default_Student, default_Student2, DB, message, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: message)
        result = accnt.send_message(default_Student, default_Student2, DB)
        assert result == expected
# Sprint 7

def send_message_fake_inputs( key, selection1, message, selection2='1'):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter Your Selection: ":selection1, # index selection
        "Enter Message Here: ":message, # message 
        "Enter Selection: ": selection2,
    }
    val = prompt_to_return_val[key]
    return val
@pytest.mark.parametrize("selection,message, expected", 
[
    (
        '1', "MESSAGE1", True
    ), 
    (
        '1', "xMESSAGE2", True
    ),
    (
        'x', "xMESSAGE2", False
    ),
    (
         '1', "x", False
    ),
])
def test_diplay_sendMessage_list_plus(monkeypatch, DB, default_Student, selection, message, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: send_message_fake_inputs(x, selection, message))
        result = accnt.diplay_sendMessage_list_plus(DB, default_Student)
        assert result == expected

@pytest.mark.parametrize("selection,message, expected", 
[
    (
        '1', "MESSAGE1", True
    ), 
    (
        '1', "xMESSAGE2", True
    ),
    (
        'x', "xMESSAGE2", False
    ), 
])
def test_diplay_sendMessage_list_plus(monkeypatch, DB, default_Student, selection, message, expected):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: send_message_fake_inputs(x, selection, message))
        result = accnt.diplay_sendMessage_list(DB, default_Student)
        assert result == expected

@pytest.mark.parametrize("selection1 ,selection2, message, expected", 
 [
    (
        '1','1', "MESSAGE1", True
    ), 
    (
        '1','2', "xMESSAGE2", True
    ),
    (
        'x','1', "xMESSAGE2", False
    ),
    (
         '1','x', "MESSAGE3", False
    ),
    (
         '1','2', "x", False
    ),
    (
         '1','1', "x", True
    ),
])
def test_diplay_inbox(monkeypatch, DB, default_Student, default_Student2, selection1, selection2, message, expected):
    
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: send_message_fake_inputs(x, selection1, message, selection2))
        accnt.send_message(default_Student, default_Student2, DB) 
        result = accnt.diplay_inbox(default_Student2, DB)
        assert result == expected

def test_check_job_posts(capsys, default_Student, DB):
    
    # Test if the student logs in and there is no new job 
    date = datetime.datetime.now()
    default_Student.date_recently_accessed = date
    # check job post
    accnt.check_job_posts(default_Student, DB)
    captured = capsys.readouterr()
    # the function should not output anything 
    assert captured.out == ''
    
    # change the login date of the student to 2018
    date_time_str = '2018-06-29 17:08:00'
    date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    default_Student.date_recently_accessed = date
    # post a job with posting date equals to now 
    jobTitle = '1_title'
    # job = {jobTitle, 'description', 'employer', 'location', 'salary', 'name_of_poster', 'poster_username', date}
    DB.create_job_posting(jobTitle, 'description', 'employer', 'location', 'salary', 'name_of_poster', 'poster_username', date)
    default_Student.add_applied_job(jobTitle)
    DB.set_student(default_Student)
    # check job post
    accnt.check_job_posts(default_Student, DB)
    captured = capsys.readouterr()
    # function should have printed the new job notification
    assert captured.out != ''

    # if we log in again there is no notification 
    date = datetime.datetime.now()
    default_Student.date_recently_accessed = date
    accnt.check_job_posts(default_Student, DB)
    captured = capsys.readouterr()
    # the function should not output anything 
    assert captured.out == ''
    
    # if a job the student applyed for gets removed 
    # he should get a notification
    # Search and delete a job
    for jobs in DB.data["Jobs"]:
        if jobs['title'] == jobTitle:
            # print('succes')
            DB.remove_job_posting(jobs)
    # check job post notifications
    accnt.check_job_posts(default_Student, DB)
    captured = capsys.readouterr()
    # function should have printed the new job notification
    assert captured.out != ''

def test_check_new_users(capsys, default_Student, default_Student2, DB):
    # Test if the student logs in and there is no new Student 
    date = datetime.datetime.now()
    default_Student.date_recently_accessed = date
    accnt.check_new_users(default_Student, DB)
    captured = capsys.readouterr()
    # Function should not have print anything
    assert captured.out == ''

    # Channge joined date of Student 2 to now
    default_Student2.date_recently_accessed = date
    DB.set_student(default_Student2)
    # Change last logged in date to 2018
    date_time_str = '2018-06-29 17:08:00'
    date_past = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    default_Student.date_recently_accessed = date_past
    accnt.check_new_users(default_Student, DB)
    captured = capsys.readouterr()
    # Function should not have print anything
    assert captured.out != ''

def test_check_last_seven_days_app(capsys, default_Student):
    # Simulate the default student have just applyed to a job
    date_now = datetime.datetime.now()
    default_Student.date_last_app_sent = date_now
    accnt.check_last_seven_days_app(default_Student)
    captured = capsys.readouterr()
    # Function should not have print anything
    assert captured.out == ''

    # Change last logged in date to 2018
    date_time_str = '2018-06-29 17:08:00'
    date_past = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    default_Student.date_last_app_sent = date_past
    accnt.check_last_seven_days_app(default_Student)
    captured = capsys.readouterr()
    # Function should not have print anything
    assert captured.out != ''

def test_get_job_count(default_Student):
    applied_jobs_len = len(default_Student.applied_jobs)
    assert applied_jobs_len == default_Student.get_job_count()


@pytest.mark.parametrize("jobTitle",
                         [
                             (
                                 "MESSAGE1",
                             ),
                             (
                                 "MESSAGE2",
                             ),
                             (
                                 "MESSAGE3",
                             ),
                             (
                                 "MESSAGE4",
                             ),
                             (
                                 "",
                             ),
                         ])
def test_add_applied_job(default_Student, jobTitle):
    default_Student.add_applied_job(jobTitle)
    assert jobTitle in default_Student.applied_jobs
    

@pytest.mark.parametrize("jobTitle",
                         [
                             (
                                 "MESSAGE1",
                             ),
                             (
                                 "MESSAGE2",
                             ),
                             (
                                 "MESSAGE3",
                             ),
                             (
                                 "MESSAGE4",
                             ),
                             (
                                 "",
                             ),
                         ])
def test_remove_applied_job(default_Student, jobTitle):
    default_Student.remove_applied_job(jobTitle)
    assert jobTitle not in default_Student.applied_jobs
# TODO: Epic 8
# DONE: test_check_job_posts                (ACCT) 
# DONE: test_check_new_users                (ACCT)
# DONE: test_check_last_seven_days_app      (ACCT) 
# TODO: test_get_job_count                  (ACCT)
# DONE: test_add_applied_job                (Student)
# TODO: test_remove_applied_job             (Student)
# 
