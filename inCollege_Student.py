class Student():
    # def __init__(self, username, password, firstname='', lastname=''):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        # Class params
        # self.student_data['username']=username
        # self.student_data['password']=password
        # self.student_data['firstname']=firstname
        # self.student_data['lastname']=lastname
    
    def __getattribute__(self, name):
        return self[name]
    
        # # Class settings
        # # Guest control is a dict {guest_control_type : boolean}
        # guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
        # # Laguage settings
        # language = "English"
        # default_settings = {'guest control' : guest_control, "language" : language} 
        
        # self.student_data['settings'] = default_settings

        # # Profile
        # self.student_data['title'] =''
        # self.student_data['about'] =''
        # self.student_data['experience']=[] # List of Jobs 3 Dicts with 
        # self.student_data['education']={} # Dict school name, degree, and years attended.

        # # list of friends
        # self.student_data['friends'] = [] # List of Student
    
    # get all settings, 
    # get field specific (guest_control, language) settings, 
    # get guest control specific (Email, SMS, Advertizing) settings
    # def get_settings(self, field=None, guest_control_field=None):
    #     if field==None:
    #         return self.settings
    #     elif guest_control_field==None:
    #         return self.settings[field]
    #     else:
    #         return self.settings[field][guest_control_field]
    
    # def set_settings(self, settings):
    #     self.settings = settings

    # def update_settings(self, field, value, guest_control_field=None):
    #     if guest_control_field == None:
    #         self.settings[field] = value
    #     else:
    #         self.settings[field][guest_control_field] = value

    # # Getters & Setters
    # def set_title(self, title):
    #     self.title=title
    # def get_title(self):
    #     return self.title 
    
    # def set_about(self, about):
    #     self.about=about
    # def get_about(self):
    #     return self.about 
    
    # def add_job(self, title, employer, started, ended, location, description):
    #     new_job = {
    #         'title' :title,
    #         'employer' :employer,
    #         'started' :started,
    #         'ended' :ended,
    #         'location' :location,
    #         'description':description,
    #     }
    #     if len(self.experience) < 3:
    #         self.experience.append(new_job)
    #         return True
    #     else:
    #         return False
    
    # def set_experience(self, experience):
    #     self.experience=experience 
    
    # # Get 1st job , 2 job, 3 job, all Jobs, or None
    # def get_experience(self, index=None):
    #     if index==None:
    #         return self.experience 
    #     if index< len(self.experience):
    #         return self.experience[index]
    #     return None

    # def set_education(self, school_name, degree, years):
    #     education = {'School Name':school_name, 'degree':degree, 'years':years}
    #     self.education=education
    
    # # get education 
    # def get_education(self):
    #     return self.education
    
    # # set friends by passing a list of Student Objects 
    # def set_friends(self, friend_List):
    #     self.friends=friends 
    
    # def get_friends(self):
    #     return self.friends

    # def add_friend(self, friend):
    #     self.friends.append(friend)

    # def getter(self, field):
    #     return self.data[field]
new_username='word'
new_password='word'
new_firstname='word'
new_lastname='word'

guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
        # laguage settings
language = "English"

settings = {'guest control' : guest_control, "language" : language} 
# language settings

# Init new student 
new_student = {'username':new_username, 'password':new_password,'firstname':new_firstname, 'lastname':new_lastname, 'settings': settings}

myStudent = Student(**new_student)

print(myStudent.settings)
