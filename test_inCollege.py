import pytest
import inCollege_Accnt as accnt
import inCollege_Home as home
import inCollege_CurrentUser as user
import inCollege_Database as database
import inCollege_CurrentUser as user
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

# # Test function that selects a skill
# @pytest.mark.parametrize("selection, expected",
# [
#     (0, False),
#     (1, True),
#     (2, True),
#     (3, True),
#     (4, True),
#     (5, True),
#     (6, False),
# ])
# def test_skillSelect(selection, expected):
#     result = home.selectionScreen(selection)
#     assert result == expected
# @pytest.mark.parametrize("selectionStr, expected",
# [
#     ('1', True),
#     ('2', True),
#     ('3', True),
#     ('4', True),
#     ('5', True),
#     ('x', False),
# ])
# def test_skillSelect(monkeypatch, selectionStr, expected):
#     monkeypatch.setattr('builtins.input', lambda x: selectionStr)
#     result = home.skillScreen()
#     assert result == expected

#Create Job testing
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

# #Test login prompt
# @pytest.mark.parametrize("selection, expected",
# [
#     (-1, False),
#     (0, False),
#     (1, True),
#     (2, True),
# ])
# #Test function loginprompt, Not sure if its correctly tested
# def test_login_prompt(selection, expected):
#     result = home.login_prompt(selection)
#     assert result == expected

#for testing purposes
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
    reset_DB_data = {"Students":[], "Jobs":[]}
    DB.load()
    assert DB.data == reset_DB_data
    assert DB.isFull == False

def test_reset(DB):
    DB.reset()
    reset_DB_data = {"Students":[], "Jobs":[]}
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
def test_login(DB, monkeypatch, username, password, expected):

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
            assert result.name != ''


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
        "username",
        False,
    ),
    (
        "1accusername",
        True,
    ),
 
])
#Test for get student by username
def test_get_student_by_username(DB, username, expected):
    result = DB.get_student_by_username(username)
    if result:
        assert result["username"] == username
    else:
        assert result == False

# def test_hello(capsys, inputStr, expected):
#     outputFunction(inputStr)
#     captured_stdout, captured_stderr = capsys.readouterr()
#     # You can use .strip here to eliminate '\n', or include it in the expected string
#     assert captured_stdout.strip() == expected