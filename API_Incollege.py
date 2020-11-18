import inCollege_Accnt as accnt
import inCollege_Database as database
#import inCollege_CurrentUser as user
import time
import datetime
import pickle
import time
from inCollege_Student import *

# This is the database object
# maintaining the database for our program
db = database.Database()

#Import information from studentAccount.txt to create a new account
def create_acct():
    #f = open("studentAccounts.txt", "r")
    #if f.mode == "r":
        #contents = f.read()
        #print(contents)
        #accnt.create_account(contents.db)
    path_to_file = "studentAccounts.txt"
    with open(path_to_file, "r") as file:
        for line in file.readlines():
            account = accnt.create_account(line.db)


    #print(content)

#Import information from newJobs.txt to create a new job listing 
def new_jobs():
    path_to_file = "newJobs.txt"
    with open(path_to_file, "r") as file:
        for line in file.readlines():
            account = accnt.post_job(line.db)

#Import information from newtraining.txt to create a new training course 
def new_training():
    f = open("newtraining.txt", "r")
    if f.mode == "r":
        contents = f.read()
    f.closed

def MyCollege_jobs():
    f = open("MyCollege_jobs.txt", "a")
    

    f.close()
def MyCollege_profiles():
    f = open("MyCollege_profiles.txt", "a")
    

    f.close()

def MyCollege_users():
    f = open("MyCollege_users.txt", "a")
   

    f.close()

def MyCollege_training():
    f = open("MyCollege_training.txt", "a")
    
    f.close()

def MyCollege_appliedjobs():
    f = open("MyCollege_appliedjobs.txt", "a")
    for jobs in db.data["Jobs"]:
        indication = ""
        for vals in jobs['users_applied']:
            # means user has already applied
            if vals['username'] == theStudent.username:
                indication = "(Applied)"
        print("|----> ", jobs['title'], indication)

    f.close()

def MyCollege_savedjobs():
    f = open("MyCollege_savedjobs.txt", "a")
    for jobs in db.data["Jobs"]:
        indication = ""
        print("|----> ", jobs['title'], indication)

    f.close()
if __name__ == "__main__":
    create_acct()
