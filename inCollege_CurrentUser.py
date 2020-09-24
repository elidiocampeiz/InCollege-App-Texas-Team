#This file contains the class of the user that is currently logged into inCollege

import inCollege_Database as database

class User:
    def __init__(self, username="", db = database.Database()):
        self.email = username
        self.db = db
        self.name = self.getUserName(username)
        # self.isEmpty = True if self.name == "" else False

    #This function assigns the users full name to name attribute
    def getUserName(self, username):
        
        for student in self.db.data["Students"]:
            #looking for user with username
            if student['username'] == username:
                # concatenating first/last name
                return student['firstname'] + " " + student['lastname']
        return ""



# user = User("username")

# ["correct_usernames, fullname",[('usrname1','fullname'),('username2', '')]]

# assert user.getUserName("correct_usernames") == fullname 