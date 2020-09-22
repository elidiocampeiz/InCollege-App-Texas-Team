import pytest
import inCollege_Accnt as accnt
import inCollege_Home as home

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
@pytest.mark.parametrize("username, password, expected",
 [
    (
        "1_acc_username",
        "1_acc_password", 
        True
    ),
    (
        "2_acc_username",
        "2_acc_password", 
        True
    ),
    (
        "3_acc_username",
        "3_acc_password", 
        True
    ),
    (
        "4_acc_username",
        "4_acc_password", 
        True
    ),
    (
        "5_acc_username",
        "5_acc_password", 
        True
    ),
    (
        "6_acc_username",
        "6_acc_password", 
        False
    ), # The DB can only have 5 user accounts so if we try to create the 6th the create_account function returns false
    
])
def test_create_account(DB, username, password, expected):
    # create_account() create returning true if the account exists and false otherwise
    result = DB.create_account(username, password)
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

# Test function that selects a skill
@pytest.mark.parametrize("selection, expected", 
[
    (0, False),
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, False),
])
def test_skillSelect(selection, expected):
    result = home.selectionScreen(selection)
    assert result == expected

    