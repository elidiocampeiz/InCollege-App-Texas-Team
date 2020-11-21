import inCollege_Database as Database
import datetime
import sys
import os
import re
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class API:
    def __init__(self, db=Database.Database()):
        self.db = db
    def load_data(self):
        self.input_training()
        self.input_student_accounts()
        self.input_job_postings()
    
    def input_job_postings(self, filename = 'newJobs.txt'):
        with open(filename) as fp:
            job_postings = []
            file_data = fp.read()
            # print(file_data)
            # split acc data 
            job_postings_data = file_data.split('\n=====\n')
            # print(job_postings_data)
            # split into list of lists with student data 

            job_postings = []#[ re.split("&&&|\n",job) for job in job_postings_data if job != '' ]
            
            for job_posting in job_postings_data:
                if job_posting != '':
                    job_post = job_posting.split('\n')
                    desc_dx = job_post.index('&&&') if '&&&' in job_post else 2
                    
                    title = job_post[0]
                    description =''.join(job_post[1:desc_dx]) 
                    employer = job_post[desc_dx+1]
                    location = job_post[desc_dx+2]
                    salary = job_post[desc_dx+3]
                    # Block print statements here 
                    blockPrint()
                    self.db.create_job_posting(title, description, employer, location, salary, 'inCollenge_admin', 'inCollenge_admin', datetime.datetime.now(), 0)
                    # Enable print statements here 
                    enablePrint()
            
    # TODO:
    def output_job_postings(self, filename = 'MyCollege_jobs.txt'):

        all_jobs = self.db.data['Jobs']
        print(all_jobs)
        data = []

        with open(filename, "w") as fp:
            sep = '=====\n'
            for jobs in all_jobs:
                jobs_list = {
                'title': jobs['title'], 
                'description': jobs['description'], 
                'employer': jobs['employer'],
                'location': jobs['location'], 
                'salary': jobs['salary'],
                    }

                for key, val in jobs_list.items():
                    line = val+'\n'
                    # print(line)
                    fp.write(line)
                fp.write(sep)
        
    
    def output_applied_jobs(self, filename = 'MyCollege_appliedJobs.txt'):
        all_jobs = self.db.data['Jobs']
        # print('all_jobs\n', all_jobs)
        
        with open(filename, "w") as fp:
            sep = '=====\n'

            for job in all_jobs:
                title = job['title']
                fp.write(title + '\n') 
                for application in job['user_applications']:
                # for application in [
                #     {'username': 'username1','graduation_date': datetime.datetime.now(), 'start_date': datetime.datetime.now(), 'why_me': 'why_me User 1'}, 
                #     {'username': 'username2','graduation_date': datetime.datetime.now(), 'start_date': datetime.datetime.now(), 'why_me': 'why_me User 2'}]:
                    fp.write(application['username'] + '\n')
                    fp.write(application['why_me'] + '\n') 

                fp.write(sep)
            
    # TODO
    def output_saved_jobs(self, filename = 'MyCollege_savedJobs.txt'):
        pass

    def input_student_accounts(self, filename='./studentAccouts.txt'):
        with open(filename) as fp:
            student_accounts = []
            file_data = fp.read()
            # print(file_data)
            # split acc data 
            accounts = file_data.split('=====')
            # split into list of lists with student data 
            student_accounts = [acc.split() for acc in accounts]
            # for acc in accounts:
            #     student_accounts.append(acc.split())
            
            # print(accounts)
            # print(student_accounts)
            # reference to main Database
            for account in student_accounts:
                # Block print statements here 
                blockPrint()
                # sleep_time is the time in which the time.sleep() is called (wainint time between function print statements), for the api it should be 0
                self.db.create_account(account[0], account[1], sleep_time=0)
                # Enable print statements here 
                enablePrint()
    def output_student_accounts(self, filename='MyCollege_profiles.txt'):
        
        all_students = self.db.data['Students']
        # print(all_students)
        data = []
        for username, student in all_students.items():
            student_data = {
            'title':student.title,
            'major':student.major,
            'university':student.university,
            'about':student.about,
            'experience':student.experience,
            'education':student.education,
            }

        with open(filename, "w") as fp:
            sep = '=====\n'
            for username, student in all_students.items():
                # print(student.experience, student.education)
                student_data = {
                'Title':student.title,
                'Major':student.major,
                'University':student.university,
                'About':student.about,
                'Experience':student.experience or '', # TODO: check if there is an error when a list is passed
                'Education':student.education or '', # TODO: check if there is an error when a dict is passed
                }

                for key, val in student_data.items():
                    line = key+': '+val+'\n'
                    # print(line)
                    fp.write(line)
                fp.write(sep)
    def input_training(self, filename='./newTraining.txt'):
        
        with open(filename) as fp:
            file_data = fp.read()
            # print(file_data)
            # split jobs data by '\n'
            trainings = file_data.split('\n')
            
            for title in trainings:
                # This should be a database function
                course = {'Name':title, 'users_completed': []}
                self.db.data["Courses"].append(course) 
            self.db.save()

    def output_training(self, filename='MyCollege_training.txt'):

        all_courses = self.db.data['Courses']
        # print('all_courses\n', all_courses)
        training_data = {}
        # group training by users who have completed each course
        for course in all_courses:
            for username in course['users_completed']:
            # for username in ['usr1', 'user2']:
                if not username in training_data:
                    training_data[username] = set()
                training_data[username].add(course['Name'])

        # print(training_data)
        # data = []
        with open(filename, "w") as fp:
            sep = '=====\n'
            for username in training_data:
                # Write username
                fp.write(username + '\n') 
                for course in training_data[username]:
                    # Write courses completed by the respective username
                    fp.write(course + '\n') 
                # Write separator
                fp.write(sep) 

    def output_job_postings(self, filename = 'MyCollege_jobs.txt'):

        all_jobs = self.db.data['Jobs']
        print(all_jobs)
        data = []

        with open(filename, "w") as fp:
            sep = '=====\n'
            for jobs in all_jobs:
                jobs_list = {
                'title': jobs['title'], 
                'description': jobs['description'], 
                'employer': jobs['employer'],
                'location': jobs['location'], 
                'salary': jobs['salary'],
                    }

                for key, val in jobs_list.items():
                    line = val+'\n'
                    # print(line)
                    fp.write(line)
                fp.write(sep)
        
# Testing
api = API()
api.db.clear()
api.load_data()
# api.input_job_postings()
api.output_applied_jobs()
