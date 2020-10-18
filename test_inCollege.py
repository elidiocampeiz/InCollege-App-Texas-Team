import pytest
import inCollege_Accnt as accnt
import inCollege_Home as home
import inCollege_CurrentUser as user
import inCollege_Database as database
import inCollege_CurrentUser as user
from inCollege_Student import *
import time
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
@pytest.mark.parametrize("username, password, firstname, lastname, expected",
 [
    (
        "1_acc_username",
        "1_acc_password",
        "1_Firstname",
        "1_Lastname",
        True
    ),
    (
        "2_acc_username",
        "2_acc_password",
        "2_Firstname",
        "2_Lastname",
        True
    ),
    (
        "3_acc_username",
        "3_acc_password",
        "3_Firstname",
        "3_Lastname",
        True
    ),
    (
        "4_acc_username",
        "4_acc_password",
        "4_Firstname",
        "4_Lastname",
        True
    ),
    (
        "5_acc_username",
        "5_acc_password",
        "5_Firstname",
        "5_Lastname",
        True
    ),
    (
        "6_acc_username",
        "6_acc_password",
        "6_Firstname",
        "6_Lastname",
        False
    ), # The DB can only have 5 user accounts so if we try to create the 6th the create_account function returns false

])
def test_create_account(DB, username, password, firstname, lastname, expected):
    # create_account() create returning true if the account exists and false otherwise
    result = DB.create_account(username, password, firstname, lastname)
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


@pytest.mark.parametrize("title, description, employer, location, salary, name_of_poster, expected",
 [
    # test a correct combination of posting job
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_name_of_poster",
        True
    ),
])

def test_create_job_posting(DB, title, description, employer, location, salary, name_of_poster, expected):
    result = DB.create_job_posting(title, description, employer, location, salary, name_of_poster)
    assert result == expected


#For multiple inputs create a function to be passed to the monkeypatch.setattr that return a string to the respective input call
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
    reset_DB_data = {"Students":{}, "Jobs":[]}
    DB.load()
    assert DB.data == reset_DB_data
    assert DB.isFull == False

def test_reset(DB):
    DB.reset()
    reset_DB_data = {"Students":{}, "Jobs":[]}
    assert DB.data == reset_DB_data
    assert DB.isFull == False

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
def create_accout_menu_fake_inputs(key, new_username, new_password, passwordCheck, new_firstname, new_lastname):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Enter username: ": new_username,
        "Enter password: ": new_password,
        "Enter New Password: ": passwordCheck,
        "Enter First Name: ": new_firstname,
        "Enter Last Name: ": new_lastname
        
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
        "6_Password",
        "Pass163",
        "6_Firstname",
        "6_Lastname",
        False
    ),
])

def test_create_accout_menu(DB, monkeypatch, new_username, new_password, passwordCheck, new_firstname, new_lastname, expected ):

    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: create_accout_menu_fake_inputs(x, new_username, new_password, passwordCheck, new_firstname, new_lastname))
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
@pytest.mark.parametrize("title, description, employer, location, salary, fullname, expected",
 [
    # test a correct combination of jobs and names
    (
        "",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
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
        False
    ),
    (
        "1_title",
        "1_description",
        "1_employer",
        "1_location",
        "1_salary",
        "1_fullname",
        True
    ),
])
#Post Job Test
def test_post_job(monkeypatch, DB, title, description, employer, location, salary, fullname, expected ):
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: post_job_fake_inputs(x, title, description, employer, location, salary, expected))
        result = accnt.post_job(fullname, DB)
        assert result == expected

# Test for User Class
@pytest.mark.parametrize("username, expected",
 [
    #Test correct first name from test_create_account
    (
        "1accusername",
        "1Firstname 1Lastname",
    ),
    #Test a wrong combination of
    (
        "2_acc_username",
        ""
    ),
    # Todo: 3 more cases
])
def test_getUserName(DB, username, expected):
    myUser = user.User(username, DB)
    assert expected == myUser.getUserName(username).strip()

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
        # Test a username da doesn't exist in DB
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
    DB.create_account(student.username, student.password, student.firstname, student.lastname)

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
        "Enter a title for your profile: ":                                 kwargs['title']                 if kwargs.get('title') != None else '',
        "Enter the about section of your profile: ":                        kwargs['about']                 if kwargs.get('about') != None else '',
        "Enter your University: ":                                          kwargs['university']            if kwargs.get('university') != None else '',
        "Enter your Major: ":                                               kwargs['major']                 if kwargs.get('major') != None else '',
        "Enter Your Status Year (Freshman, Sophomore, Junior, Senior): ":   kwargs['year']                  if kwargs.get('year') != None else '',
        "Enter Job Title: ":                                                kwargs['job_title']             if kwargs.get('job_title') != None else '',
        "Enter Job Description: ":                                          kwargs['description']           if kwargs.get('description') != None else '',
        "Enter Employer For Job: ":                                         kwargs['employer']              if kwargs.get('employer') != None else '',
        "Enter Job Location: ":                                             kwargs['location']              if kwargs.get('location') != None else '',
        "Enter the Date you Started: ":                                     kwargs['start_date']            if kwargs.get('start_date') != None else '',
        "Enter The Date You Ended: ":                                       kwargs['end_date']              if kwargs.get('end_date') != None else '',
        
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