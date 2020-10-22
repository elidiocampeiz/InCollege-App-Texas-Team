
#Call whatever you believe student should have
# Either get a value or an empty string and this is accomplished by 
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
        
    #self.__dict__ classes in python have dictionaries underneath their variables
    #Takes the key args 
    # print(aStudent.__dict__) would give {'i_var': 2}
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
    def add_job_experience(self, title, employer, start_date, end_date, location, description):
        
        new_job = {
            'title' :title,
            'employer' :employer,
            'start_date' :start_date,
            'end_date' :end_date,
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
    
    # Get 1st job , 2 job, 3 job, all Jobs, or None
    # Test for return value 
    def get_experience(self, index=None):
        # return full expereince object
        if index == None or index < 0:
            return self.experience 
        # return job at index
        if index < len(self.experience):
            return self.experience[index]
        # Out of range
        return False
    # Test for Effect 
    def set_education(self, university, major, year):
        education = {
            'university':university, 
            'major':major, 
            'year':year
            }
        self.education.update(**education)
        
    # # get education 
    def get_education(self, field=None):
        # if no field is specified return full dict object
        if field==None:
            return self.education
        # if field is a key in dict return its value
        elif self.education.get(field) != None:
            return self.education[field]
        # else return empty string
        else:
            return ''
    
    # # set friends by passing a list of Student Objects 
    # def set_friends(self, friend_List):
    #     self.friends=friends 
    
    def add_dummy_friends(self):
        student_friend_1 = Student(username='JohnSmith',firstname='John', lastname='Smith',title='Research Assistant at Harvard', about='Machine Learning Researcher')
        student_friend_1.set_education('Harvard University', 'Computer Science', 'Junior')
        student_friend_1.add_job_experience('job_title1', 'employer1', 'start_date1', 'end_date1', 'location1', 'description1')
        self.add_friend(student_friend_1)

        student_friend_2 = Student(username='JaneDoe',firstname='Jane', lastname='Doe',title='Software Engineering Intern at Google')
        student_friend_2.set_education('Stanford University', 'Software Engineering', 'Senior')
        student_friend_2.add_job_experience('Software Engineering Intern', 'Google', '05/01/2020', '08/01/2020', 'Bay Area, LA, CA', 'Developed really cool Software at Google')
        self.add_friend(student_friend_2)
        
        

    def add_friend(self, friend):
        self.friends.append(friend)
