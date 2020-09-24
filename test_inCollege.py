import pytest
import inCollege_Accnt as accnt
import inCollege_Home as home
import inCollege_CurrentUser as user
import inCollege_Database as database


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
@pytest.mark.parametrize("selectionStr, expected", 
[
    ('0', False),
    ('1', True),
    ('2', True),
    ('3', True),
    ('4', True),
    ('5', True),
    ('6', False),
])
def test_skillSelect(monkeypatch, selectionStr, expected):
    monkeypatch.setattr('builtins.input', lambda x: selectionStr)
    result = home.skillScreen()
    assert result == expected

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
        "Please enter the first name of the user you want to connect to: ": firstname,
        "Please enter the last name of the user you want to connect to: ": lastname,
    }
    val = prompt_to_return_val[key]
    return val

# Create search_users
@pytest.mark.parametrize("firstname, lastname, expected",
 [
    #Test correct first name from test_create_account
    (
        "1_Firstname",
        "1_Lastname", 
        True
    ),
    #Test a wrong combination of 
    (
        "2_acc_username",
        "1_acc_username", 
        False
    ),
    # Todo: 3 more cases
    
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
    assert DB.data == reset_DB_data
    assert DB.isFull == False

# Create Account Test (inCollege_Acct.py)
def create_accout_menu_fake_inputs(key, username, password, passwordCheck, firstname, lastname):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Please enter username, type 'q' to cancel: ": username,
        "Please enter password, type 'q' to cancel: ": password,
        "Please enter new password or type 'q' to quit: ": passwordCheck,
        "Please enter first name, type 'q' to cancel: ": firstname,
        "Please enter last name, type 'q' to cancel: ": lastname
    }
    val = prompt_to_return_val[key]
    return val

# Create Account Test
@pytest.mark.parametrize("username, password, passwordCheck, firstname, lastname, expected",
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
        "q",
        "4Password",
        "Pass123",  
        "4Firstname",
        "4Lastname",
        False
    ),
    # 'q' in the password field
    (
        "4accusername",
        "q",
        "Pass123",  
        "4Firstname",
        "4Lastname",
        False
    ),
    # invalid password and 'q' in the Default password field
    (
        "4accusername",
        "4password", 
        "q", 
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

def test_create_accout_menu(DB, monkeypatch, username, password, passwordCheck, firstname, lastname, expected ):
    
    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: create_accout_menu_fake_inputs(x, username, password, passwordCheck, firstname, lastname))
        # print('BREAKPOINT db is full ', DB.isFull, len(DB.data["Students"]) )
        result = accnt.create_account(DB)
        assert result == expected


def login_fake_inputs(key, username, password):
    # Each Key has to be the same string as the respective input statement
    prompt_to_return_val = {
        "Please enter your username, type 'q' to cancel: ": username,
        "Please enter your password, type 'q' to cancel: ": password
    } 
    val = prompt_to_return_val[key]

    return val
@pytest.mark.parametrize("username, password, expected",
 [
    #Test correct first name from test_create_account
    (
        "1_acc_username",
        "1_acc_password", 
        False
    ),
    #Test a wrong combination of 
    (
        "2_acc_username",
        "1_acc_username", 
        False
    ),
    # Todo: 3 more cases
])
def test_login(DB, monkeypatch, username, password, expected):

    with monkeypatch.context() as m:
        # the x parameter of the lambda function becomes the key used to access each respective input call
        m.setattr('builtins.input', lambda x: login_fake_inputs(x, username, password))
        # m.setattr('sys.stdin', ans2)
        result = accnt.login(DB)
        # result = userInputFucntion()
        assert result == expected