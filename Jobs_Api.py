import inCollege_Database as Database

class newJobsApi:
    def __init__(self, db=Database.Database()):
        self.db = db
    def input_newjobs(self, filename='./newJobs.txt'):
        njobs = []
        with open('./newJobs.txt') as fp:
            file_data = fp.read()
            print(file_data)
            # split jobs data 
            jobs = file_data.split('=====')
            # split into list of lists with student data 
            newJobs = [n_j.split() for n_j in jobs]
            # for acc in accounts:
            #     student_accounts.append(acc.split())
            
            # print(accounts)
            # print(student_accounts)
            # reference to main Database
            for job in njobs:
                # sleep_time is the time in which the time.sleep() is called (wainint time between function print statements), for the api it should be 0
                self.db.create_job_posting(job[0], job[1], sleep_time=0)
    
    def output_MyCollege_jobs(self, filename = 'MyCollege_jobs.txt'):
        all_jobs = self.db.data['Jobs']
        print(all_jobs)

        data = []
        for jobs in all_jobs.items():
            job_data = {
                'Title':jobs.title,
                'Description':jobs.description,
                'Employer':jobs.employer,
                'Location':jobs.location,
                'Salary':jobs.salary,
            }
        #TODO : created job goes here
        #TODO : If job gets deleted, then the job gets deleted here too  
        with open(filename ,"w") as fp:
            sep = '=====\n'
            for jobs in all_jobs.items():
            job_data = {
                'Title':jobs.title,
                'Description':jobs.description,
                'Employer':jobs.employer,
                'Location':jobs.location,
                'Salary':jobs.salary,
            }
        for key, val in job_data.items():
            line = key + ': ' + val + '\n'
            print(line)
            fp.write(line)
        fp.write(sep)
    
    def output_MyCollege_appliedjobs(self, filename = 'MyCollege_appliedjobs.txt'):

    def output_MyCollege_savedjobs(self, filename = 'MyCollege_savedjobs.txt'):
    
api = Jobs_Api()
api.output_MyCollege_jobs()