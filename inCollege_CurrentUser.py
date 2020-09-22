#This file contains the class of the user that is currently logged into inCollege

import inCollege_Database as database

class User:
    def __init__(self, username):
        self.email = username
        self.name = self.getUserName(username)


    #This function assigns the users full name to name attribute
    def getUserName(self, username):
        db = database.Database()
        for student in db.data["Students"]:
            #looking for user with username
            if student['username'] == username:
                # concatenating first/last name
                return student['firstname'] + " " + student['lastname']