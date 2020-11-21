import pickle
import time
from inCollege_Student import *
# Dictionary data structure. Or set. I don't know.
# Pickle saves the binary data of the python object.


class Database():
    def __init__(self, filename='database'):
        self.filename = filename
        self.reset()
        self.load()

    # Reset data
    def reset(self):
        self.data = {"Students": {}, "Jobs": [], 'Friend Requests': {}, "Courses": []}
        self.accFull = False
        self.jobFull = False
        # self.populate_course_list()
        
        # if the database file doesn't exist uncomment the next line
        # self.save()

    # Clear Database
    def clear(self):
        # Reset data
        self.reset()
        self.save()

    # Load data from file, with the option of usign an alternative file
    def load(self, filename=None):
        if filename != None:
            self.filename = filename

        # Load data from file
        with open(self.filename, 'rb') as database_file:
            self.data = pickle.load(database_file)

        # If DB is empty create a "Students" section
        if "Students" not in self.data:
            self.data["Students"] = {}

        # If DB is empty create a "Jobs" section
        if "Jobs" not in self.data:
            self.data["Jobs"] = []
        
        # If DB is empty create a "Courses" section
        if "Courses" not in self.data:
            self.data["Courses"] = []
            # self.populate_course_list() # this will fill the course list with the requested courses from the professor

        # If there are 10 or more student accounts, the acc DB is full
        if len(self.data["Students"]) > 9:
            self.accFull = True

        # If there are 10 or more jobs posted, the job DB is full.
        if len(self.data["Jobs"]) > 9:
            self.jobFull = True

    # Save data to file
    def save(self):
        with open(self.filename, 'wb') as database_file:
            pickle.dump(self.data, database_file)

    # # Get all data
    # def get_data(self):
    #     # Load data
    #     self.load()
    #     return self.data

    # Create new student account COMIT
    def create_account(self, new_username, new_password, new_firstname='default_firstname', new_lastname='default_lastname', plus=False, sleep_time=1):

        # Load data from file
        self.load()

        # If DB is full return False
        if self.accFull == True:
            print("...")
            time.sleep(sleep_time)
            print('|*| Error: Maximum Number of Accounts Already Taken |*|')
            time.sleep(sleep_time)
            return False

        # New accounts have all guest control turned on
        # guest control is a dict {guest_control_type : boolean}
        guest_control = {"Email": True, "SMS": True,
                         "Targeted Advertising": True}
        # laguage settings
        language = "English"

        settings = {'guest control': guest_control, "language": language}
        # language settings

        # Init new student
        new_student = {'username': new_username, 'password': new_password,
                       'firstname': new_firstname, 'lastname': new_lastname, 'settings': settings,
                       'status': plus}
        my_student = Student(**new_student)
        # Iterate through each student in "Students" section
        # for student in self.data["Students"]:
        #     # If username already exists return false
        #     if student.username == new_username:
        #         print("...")
        #         time.sleep(1)
        #         print('Username already in use')
        #         time.sleep(1)
        #         return False
        my_student.update(finished_profile=False)
        if new_username in self.data["Students"].keys():
            print('Username already in use...')
            time.sleep(sleep_time)
            return False

        # Else append new student to the list
        self.data["Students"][new_username] = my_student

        # Save data to file
        self.save()
        print("\n... \n")
        # added this for effect, makes program wait for second then tells user account was created.
        time.sleep(sleep_time)
        print("Account Succesfully Created!\n")
        time.sleep(sleep_time)
        return True

    def create_job_posting(self, title, description, employer, location, salary, name_of_poster, poster_username, date):

        if title == '' or description == '' or employer == '' or location == '' or salary == '' or name_of_poster == '' or poster_username == '' or date == '':
            return False
        # loading data from file
        self.load()

        if self.jobFull == True:  # If there's already ten jobs posted, it won't let them post more
            print("...")
            time.sleep(1)
            print('|*| Error: Maximum Number of Jobs Already Posted |*|')
            time.sleep(1)
            return False

        # Init new job posting
        new_job = {'title': title, 'description': description, 'employer': employer,
                   'location': location, 'salary': salary, 'name_of_poster': name_of_poster,
                   'users_applied': [],
                   'users_saved': [],
                   'poster_id': poster_username,
                   'date_posted': date}
        # users applied, and saved above will be users who applied to or saved the job posting

        # Appending new job to list
        self.data["Jobs"].append(new_job)

        # Save data to file
        self.save()
        print("...")
        time.sleep(1)
        print("Job Posted Successfully!")
        time.sleep(1)
        return True

    def remove_job_posting(self, job):
        if job in self.data["Jobs"]:
            self.data["Jobs"].remove(job)
            print("Job removed")
            self.save()
            return True
        return False

    # Login function
    def login(self, username, password):

        # Load data
        self.load()

        # if there is no student section there is not student account
        if "Students" not in self.data:
            return False

        # # Iterate through each student in "Students" section
        # for student in self.data["Students"]:
        #     # If username and password match, login succesful return True
        #     if student['username'] == username and student['password'] == password:
        #         print("\n...")
        #         time.sleep(1)
        #         print('Succesful login!\n')
        #         time.sleep(1)
        #         return True
        if self.data["Students"].get(username) != None:
            student = self.data["Students"][username]
            if student.password == password:
                print("\n...")
                time.sleep(1)
                print('Succesful login!\n')
                time.sleep(1)
                return True

        print("|*| No account found with this username and password combination |*|\n")
        return False

    def search_users(self):

        print("|*| NOTE - Enter 'x' at any time to go back |*|\n")
        print("Enter the Following to check if user is in the inCollege Database...\n")
        firstname_search = input("--> First Name: ")
        if firstname_search == 'x':
            return False

        lastname_search = input("--> Last Name: ")
        if lastname_search == 'x':
            return False

        for username, student in self.data["Students"].items():
            # If username already exists return false
            if student.firstname == firstname_search and student.lastname == lastname_search:
                return True

        # if we get to this point, the user was not founf
        print("...")
        time.sleep(1)
        print("They are not yet a part of the InCollege system yet!\n")
        time.sleep(1)
        return False

    # Get Students data return student dict or false
    # Note: to test the function in use an if statement before the assert
    # e.g
    # result = get_student_by_username(username)
    # if result:
    #   assert result.username == username
    # else:
    #    assert result == False
    def get_student_by_username(self, username):
        # Load data
        self.load()
        # Get student by username
        # for student in self.data["Students"]:
        #     # If username already exists return false
        #     # if student['username'] == username:
        #     if student.username == username:
        #         return student
        # return False
        if username in self.data["Students"].keys():
            student = self.data["Students"][username]
            return student
        return False

    # def update_student(self, username, field, value, setting_field=None, guest_control_field=None):
    #     if username == None or field == None or value == None:
    #         return False
    #     data = self.data
    #     # Get student by username
    #     student = self.get_student_by_username(username)
    #     # If student not found return false
    #     if not student:
    #         return False
    #     # index of student
    #     idx = data["Students"].index(student)

    #     # if its a settings update
    #     if field == "settings" and setting_field != None:
    #         # if its a notification
    #         if setting_field == 'guest control':
    #             student[field][setting_field][guest_control_field] = value
    #         # if its a language update
    #         else:
    #             student[field][setting_field] = value
    #     # Else (e.i. if its a username, password, firstname or lastname update)
    #     else:
    #         student[field] = value

    #     data["Students"][idx] = student
    #     # Update self.data
    #     self.data = data
    #     # Save change in DB file
    #     self.save()
    #     return True

    def set_student(self, student):

        if not isinstance(student, Student):
            return False
        if self.data["Students"].get(student.username) == None:
            return False

        self.data["Students"][student.username] = student
        self.save()
        return True

    # def search_by_field(self, field, value):
    #     self.load()
    #     for username, student in self.data['Student']:
    #         if student.__dict__.get(field) and student.__dict__[field] == value:
    #             return student
    #     return False

    def add_friend_request(self, to_username, from_username):
        if to_username == from_username:
            return False
        # All request are stored as key values in self.data['Friend Requests']: {'to_username', {'from_username1', 'from_username2', ...}}
        if self.data['Friend Requests'].get(to_username) == None:
            self.data['Friend Requests'][to_username] = set()
            self.data['Friend Requests'][to_username].add(from_username)
        elif from_username in self.data['Friend Requests'][to_username]:
            # Request already exists return false
            return False
        else:  # add request to DB
            self.data['Friend Requests'][to_username].add(from_username)
        # Save DB
        self.save()
        return True

    # Removes a reqest sent to to_username from from_username
    def remove_friend_request(self, to_username, from_username):
        if to_username == from_username:
            return False
        # All request are stored as key values in self.data['Friend Requests']: {'to_username', {'from_username1', 'from_username2', ...}}
        if self.data['Friend Requests'].get(to_username) == None or from_username not in self.data['Friend Requests'][to_username]:
            # Nothing to remove
            return False
        elif len(self.data['Friend Requests'][to_username]) > 1:  # Remove request from DB
            self.data['Friend Requests'][to_username].remove(from_username)
        else:
            self.data['Friend Requests'].pop(to_username)
            # Save DB
        self.save()
        return True

    def populate_course_list(self, newCourses=[]):
        #users_completed will hold usernames of students who have finished the course
        newCourse1 = {'name': "How to use In College Learning", 'users_completed': []}
        newCourse2 = {'name': "Train the Trainer", 'users_completed': []}
        newCourse3 = {'name': "Gamification of Learning", 'users_completed': []}
        newCourse4 = {'name': "Understanding the Architectual Design Process", 'users_completed': []}
        newCourse5 = {'name': "Project Management Simplified", 'users_completed': []}

        self.data["Courses"].append(newCourse1)
        self.data["Courses"].append(newCourse2)
        self.data["Courses"].append(newCourse3)
        self.data["Courses"].append(newCourse4)
        self.data["Courses"].append(newCourse5)
        # extend a list of new courses
        self.data["Courses"].extend(newCourses)
        #self.save()
        return True
