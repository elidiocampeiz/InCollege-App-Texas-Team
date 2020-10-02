#This file contains the class of the user that is currently logged into inCollege

import inCollege_Database as database

class User:
    def __init__(self, username="", db = database.Database()):
        self.username = username
        self.db = db
        self.name = self.getUserName(username)
        # self.isEmpty = True if self.name == "" else False

    #This function assigns the users full name to name attribute
    def getUserName(self, username):
        self.db.load()
        for student in self.db.data["Students"]:
            #looking for user with username
            if student['username'] == username:
                self.student_data = student
                # concatenating first/last name
                return student['firstname'] + " " + student['lastname']
        return ""
