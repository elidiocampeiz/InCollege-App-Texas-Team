import pickle

#Dictionary data structure. Or set. I don't know.
#Pickle saves the binary data of the python object.

class Database():
    def __init__(self, filename='database'):
        self.filename = filename
        self.reset()
        self.load()

    # Reset data
    def reset(self):
        self.data = {"Students":[]}
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
        if filename==None:
            filename = self.filename
        else: 
            self.filename = filename
        
        # Load data from file
        with open(filename, 'rb') as database_file:
            self.data = pickle.load(database_file)
        
        # If DB is empty create a "Students" section
        if "Students" not in self.data:
            self.data["Students"] = []
        
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

    # # Get Students data
    # def get_students(self):
    #     # Load data
    #     self.load()
    #     return self.data["Students"] 

    # Create new student account
    def create_account(self, new_username, new_password):
        
        # Load data from file
        self.load()

        # If DB is full return False
        if self.isFull == True:
            print('Maximum number of accounts accounts have been created. Please come back later.')
            return False

        # Init new student 
        new_student = {'username':new_username, 'password':new_password}
        
        # Iterate through each student in "Students" section
        for student in self.data["Students"]:
            # If username already exists return false
            if student['username'] == new_username:
                print('Username already in use')
                return False
        
        # Else append new student to the list
        self.data["Students"].append(new_student)
            
        # Save data to file
        self.save()
        print("Account created")
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
                print('Succesful login')
                return True
        
        print("No account found with this username and password combination")
        return False

# DB = Database()
# # DB.clear()
# a = DB.create_account("u","p")
# a = DB.create_account("a","p")
# a = DB.create_account("b","p")
# a = DB.create_account("c","p")
# a = DB.create_account("d","p")
# a = DB.create_account("g","p")



# a = DB.login("u","p")
# a = DB.login("a","p")
