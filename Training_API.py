import inCollege_Database as Database

class TrainingApi:
    def __init__(self, db=Database.Database()):
        self.db = db
    def input_training(self, filename='./newTraining.txt'):
        training = []
        with open('./newTraining.txt') as fp:
            file_data = fp.read()
            print(file_data)
            # split jobs data 
            program = file_data.split('=====')
            # split into list of lists with student data 
            newTraining = [n_t.split() for n_t in program]
            # for acc in accounts:
            #     student_accounts.append(acc.split())
            
            # print(accounts)
            # print(student_accounts)
            # reference to main Database
            for course in training:
                # sleep_time is the time in which the time.sleep() is called (wainint time between function print statements), for the api it should be 0
                self.db["Courses"] = []
                self.populate_course_list()
    
    def output_MyCollege_training(self, filename = ' MyCollege_training.txt'):
         