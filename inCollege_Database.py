import pickle
import time 

#Dictionary data structure. Or set. I don't know.
#Pickle saves the binary data of the python object.

class Database():
    def __init__(self, filename='database'):
        self.filename = filename
        self.reset()
        self.load()

    # Reset data
    def reset(self):
        self.data = {"Students":[], "Jobs":[]}
        self.isFull = False
        # if the database file doesn't exist uncomment the next line
        # self.save()            
        
    # Clear Database
    def clear(self):
        # Reset data
        self.reset()
        # Clear file
        self.save()

    # Load data from file, with the option of usign an alternative file
    def load(self, filename=None):
        if filename!=None: 
            self.filename = filename
        
        # Load data from file
        with open(self.filename, 'rb') as database_file:
            self.data = pickle.load(database_file)
        
        # If DB is empty create a "Students" section
        if "Students" not in self.data:
            self.data["Students"] = []

        # If DB is empty create a "Jobs" section
        if "Jobs" not in self.data:
            self.data["Jobs"] = []
        
        # If there are 5 or more student accounts, the DB is full
        if len(self.data["Students"]) > 4:
                self.isFull = True
        
    # Save data to file
    def save(self):
        with open(self.filename, 'wb') as database_file:
            pickle.dump(self.data, database_file)
    
    # # Get all data
    # def get_data(self):
    #     # Load data
    #     self.load()
    #     return self.data


    # Create new student account
    def create_account(self, new_username, new_password, new_firstname, new_lastname):
        
        # Load data from file
        self.load()

        # If DB is full return False
        if self.isFull == True:
            print("...")
            time.sleep(1)
            print('|*| Error: Maximum Number of Accounts Already Taken |*|')
            time.sleep(1)
            return False

        # New accounts have all guest control turned on
        # guest control is a dict {guest_control_type : boolean}
        guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
        # laguage settings
        language = "English"

        settings = {'guest control' : guest_control, "language" : language} 
        # language settings

        # Init new student 
        new_student = {'username':new_username, 'password':new_password,'firstname':new_firstname, 'lastname':new_lastname, 'settings': settings}
        
        # Iterate through each student in "Students" section
        for student in self.data["Students"]:
            # If username already exists return false
            if student['username'] == new_username:
                print("...")
                time.sleep(1)
                print('Username already in use')
                time.sleep(1)
                return False
        
        # Else append new student to the list
        self.data["Students"].append(new_student)
            
        # Save data to file
        self.save()
        print("\n... \n")
        time.sleep(1) #added this for effect, makes program wait for second then tells user account was created.
        print("Account Succesfully Created!")
        time.sleep(1)
        return True

    def create_job_posting(self, title, description, employer, location, salary, name_of_poster):

        if title == '' or description == '' or employer == '' or location == '' or salary == '' or salary == '' or name_of_poster == '':
            return False
        #loading data from file
        self.load()

        # Init new job posting
        new_job = {'title': title, 'description': description, 'employer': employer,
                       'location': location, 'salary': salary, 'name_of_poster': name_of_poster}

        #Appending new job to list
        self.data["Jobs"].append(new_job)

        # Save data to file
        self.save()
        print("...")
        time.sleep(1)
        print("Job Posted Successfully!")
        time.sleep(1)
        return True

    # Login function
    def login(self, username, password):
        
        # Load data
        self.load()

        # if there is no student section there is not student account
        if "Students" not in self.data:
            return False
        
        # Iterate through each student in "Students" section
        for student in self.data["Students"]:
            # If username and password match, login succesful return True
            if student['username'] == username and student['password'] == password:
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

        for student in self.data["Students"]:
            # If username already exists return false
            if student['firstname'] == firstname_search and student['lastname'] == lastname_search:
                return True

        #if we get to this point, the user was not founf
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
        for student in self.data["Students"]:
            # If username already exists return false
            if student['username'] == username:
                return student
        return False
    


    def update_student(self, username, field, value, setting_field=None, guest_control_field=None):
        if username == None or field ==None or value ==None:
            return False
        data = self.data
        # Get student by username
        student = self.get_student_by_username(username)
        # If student not found return false
        if not student:
            return False
        # index of student
        idx = data["Students"].index(student)

        # if its a settings update
        if field == "settings" and setting_field != None:
            # if its a notification
            if setting_field == 'guest control':
                student[field][setting_field][guest_control_field] = value
            # if its a language update
            else:
                student[field][setting_field] = value
        # Else (e.i. if its a username, password, firstname or lastname update)
        else:
            student[field] = value
        
        data["Students"][idx] = student
        # Update self.data
        self.data = data 
        # Save change in DB file
        self.save()
        return True
