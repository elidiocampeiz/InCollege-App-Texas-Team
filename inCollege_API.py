import inCollege_Database as Database
import datetime
import sys
import os
import re

# Disable PRINT
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore PRINT
def enablePrint():
    sys.stdout = sys.__stdout__

class API:
    def __init__(self, db=Database.Database()):
        self.db = db
    def load_data(self):
        self.input_training()
        self.input_student_accounts()
        self.input_job_postings()
        self.output_profiles()
        self.output_training()
        self.output_job_postings()
        self.output_applied_jobs()
        self.output_saved_jobs()
        
    
    def input_job_postings(self, filename = 'newJobs.txt'):
        
        
        with open(filename) as fp:
            job_postings = []
            file_data = fp.read()
            # print(file_data)
            # split acc data 
            job_postings_data = file_data.split('\n=====\n')
            # print(job_postings_data)
            # split into list of lists with student data 

            job_postings = [] 
            
            # NOTE: Not sure about this requirement 
            # Not allowing jobs with same title and same employer (duplicates)
            existing_jobs = set([job['title'] for job in self.db.data["Jobs"]])
            
            for job_posting in job_postings_data:
                if job_posting != '':
                    job_post = job_posting.split('\n')
                    desc_dx = job_post.index('&&&') if '&&&' in job_post else 2
                    
                    title = job_post[0]
                    description =''.join(job_post[1:desc_dx]) 
                    employer = job_post[desc_dx+1]
                    location = job_post[desc_dx+2]
                    salary = job_post[desc_dx+3]
                    if not title in existing_jobs:
                        # Block print statements here 
                        blockPrint()
                        # try to create job posting 
                        result = self.db.create_job_posting(title, description, employer, location, salary, 'inCollenge_admin', 'inCollenge_admin', datetime.datetime.now(), 0)
                        # if success add title to job postings and to existing_jobs
                        if result:
                            job_postings.append(title)
                            existing_jobs.add(title)
                        # Enable print statements here 
                        enablePrint()
                        
            
            return job_postings
    
    def output_job_postings(self, filename = 'MyCollege_jobs.txt'):

        all_jobs = self.db.data['Jobs']
        # print(all_jobs)

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
        all_jobs = self.db.data['Jobs']
        # print('all_jobs\n', all_jobs)
        job_saved_data = {}
        # group training by users who have completed each course
        for job in all_jobs:
            for username in job['users_saved']:
            # for username in ['usr1', 'user2']:
                if not username in job_saved_data:
                    job_saved_data[username] = set()
                job_saved_data[username].add(job['title'])
        
        with open(filename, "w") as fp:
            sep = '=====\n'
            for username in job_saved_data:
                # Write username
                fp.write(username + '\n') 
                for course in job_saved_data[username]:
                    # Write courses completed by the respective username
                    fp.write(course + '\n') 
                # Write separator
                fp.write(sep) 

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
            created_accounts = []
            # print(accounts)
            # print(student_accounts)
            # reference to main Database
            for account in student_accounts:
                # Block print statements here 
                blockPrint()
                # sleep_time is the time in which the time.sleep() is called (wainint time between function print statements), for the api it should be 0
                result = self.db.create_account(account[0], account[1], sleep_time=0)
                if result:
                    created_accounts.append(account[0]) # append new username
                # Enable print statements here 
                enablePrint()
            return created_accounts
    def output_profiles(self, filename='MyCollege_profiles.txt'):
        
        all_students = self.db.data['Students']
        # print(all_students)
        with open(filename, "w") as fp:
            sep = '=====\n'
            for username, student in all_students.items():
                # print(student.experience, student.education)
                education_string = ' '.join([student.get_education('university'), student.get_education('major'), student.get_education('year')])
                expereince_list = []
                for exp in student.experience:
                    
                    title = exp['title']
                    employer = exp['employer']
                    start_date = exp['start_date']
                    end_date = exp['end_date']
                    location = exp['location']
                    description = exp['description']
                    exp_listing = [ employer, start_date, end_date, location, description]
                    string = title
                    for s in exp_listing:
                        if s != '':
                            string += '-'+s 
                    # string = title + '-' + employer + '-' + start_date + '-' + end_date + '-' + location + '-' + description 
                    expereince_list.append(string)
                
                expereince_string = '\n'.join(expereince_list) 
                # print(education_string)
                student_data = {
                'Title':student.title,
                'Major':student.get_education('major'),
                'University':student.get_education('university'),
                'About':student.about,
                'Experience':expereince_string or '', # TODO: check if there is an error when a list is passed
                'Education': education_string or '', # TODO: check if there is an error when a dict is passed
                }
                line = ''
                for key, val in student_data.items():
                    if val.strip() != '':
                        line += val+'\n'
                        # print(line)
                fp.write(line)
                
                fp.write(sep)
    # TODO: output_users 
    
    def input_training(self, filename='./newTraining.txt'):
        
        with open(filename) as fp:
            file_data = fp.read()
            # print(file_data)
            # split jobs data by '\n'
            trainings = file_data.split('\n')
            existing_courses = set(course['name'] for course in self.db.data["Courses"])
            for title in trainings:
                # This should be a database function
                if not title in existing_courses:
                    course = {'name':title, 'users_completed': []}
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
        # print(all_jobs)
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
        
# # Testing
# api = API()
# api.db.clear()
# api.load_data()
# api.input_job_postings()
# api.output_applied_jobs()
