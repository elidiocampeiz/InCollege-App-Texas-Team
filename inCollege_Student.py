class Student():
    # def __init__(self, username, password, firstname='', lastname=''):
    def __init__(self, **kwargs):
        self.update(**kwargs)
        # Class params
        # self.student_data['username']=username
        # self.student_data['password']=password
        # self.student_data['firstname']=firstname
        # self.student_data['lastname']=lastname
        self.experience=[] # List of Jobs 3 Dicts with 
        self.education={} # Dict school name, degree, and years attended.
        self.friends = []
    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        if self.__dict__.get(name) != None:
            return self[name]
        return ''
    def __getstate__(self):
        return self.__dict__
    def __setstate__(self,d):
        self.__dict__.update(d)
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
    def get_settings(self, field=None, guest_control_field=None):
        if field==None:
            return self.settings
        elif guest_control_field==None:
            return self.settings[field]
        else:
            return self.settings[field][guest_control_field]
    
    # def set_settings(self, settings):
    #     self.settings = settings

    def update_settings(self, field, value, guest_control_field=None):
        if guest_control_field == None:
            self.settings[field] = value
        else:
            self.settings[field][guest_control_field] = value

    # # Getters & Setters
    # def set_title(self, title):
    #     self.title=title
    # def get_title(self):
    #     return self.title 
    
    # def set_about(self, about):
    #     self.about=about
    # def get_about(self):
    #     return self.about 
    
    # 3 consecutive test expecting True
    # 4th consecutive test expect False
    def add_job_experience(self, title, employer, started, ended, location, description):
        
        new_job = {
            'title' :title,
            'employer' :employer,
            'started' :started,
            'ended' :ended,
            'location' :location,
            'description':description,
        }
        if len(self.experience) < 3:
            self.experience.append(new_job)
            return True
        else:
            return False
    
    # def set_experience(self, experience):
    #     self.experience=experience 
    
    # # Get 1st job , 2 job, 3 job, all Jobs, or None
    def get_experience(self, index=None):
        if index==None:
            return self.experience 
        if index< len(self.experience):
            return self.experience[index]
        return False

    def set_education(self, school_name, degree, years):
        education1 = {
            'university':school_name.captilize(), 
            'major':degree.captilize(), 
            'years':years
            }
        self.education.update(**education1)
        
    # # get education 
    # def get_education(self):
    #     return self.education
    
    # # set friends by passing a list of Student Objects 
    # def set_friends(self, friend_List):
    #     self.friends=friends 
    
    # def get_friends(self):
    #     return self.friends

    def add_friend(self, friend):
        self.friends.append(friend)

    # def getter(self, field):
    #     return self.data[field]
# class MyStudent(dict):

#     def __getattr__(self, name):
#         return self[name] if not isinstance(self[name], dict) \
#             else MyStudent(self[name])

#     def update_settings(self, field, value, guest_control_field=None):
#         if guest_control_field == None:
#             self.settings[field] = value
#         else:
#             self.settings[field][guest_control_field] = value

# new_username='word'
# new_password='word'
# new_firstname='word'
# new_lastname='word'

# guest_control = {"Email" : True, "SMS" : True,  "Targeted Advertising" : True}
#         # laguage settings
# language = "English"

# settings = {'guest control' : guest_control, "language" : language} 
# # language settings

# # Init new student 
# new_student = {'username':new_username, 'password':new_password,'firstname':new_firstname, 'lastname':new_lastname, 'settings': settings}

# myStudent = Student(**new_student)
# # the_title = input("title: ")
# # myStudent.title = the_title
# print('username: ',myStudent.username)

# print('Title: ',myStudent.title)
# myStudent.update(username='new_username', experience='expereince')
# print('username: ',myStudent.username)

# myStudent.friends = []
# myStudent.add_friend('my title2')
# print('Experience ',myStudent.experience)
# print('Title: ',myStudent.education)

# myStudent.set_education('a','b','c')
# print('Title: ',myStudent.education)

