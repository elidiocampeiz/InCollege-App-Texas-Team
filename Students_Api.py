import inCollege_Database as Database

class StudentAccountsApi:
    def __init__(self, db=Database.Database()):
        self.db = db
    def input_student_accounts(self, filename='./studentAccouts.txt'):
        student_accounts = []
        with open('./studentAccouts.txt') as fp:
            file_data = fp.read()
            print(file_data)
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
                # sleep_time is the time in which the time.sleep() is called (wainint time between function print statements), for the api it should be 0
                self.db.create_account(account[0], account[1], sleep_time=0)
    
    def output_student_accounts(self, filename='MyCollege_profiles.txt'):
        all_students = self.db.data['Students']
        print(all_students)
        # TODO: populate each profile field: a title, a major, university name, about, experience, and education
        # TODO: write to the file using '=====' as a separator
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
                    print(line)
                    fp.write(line)
                fp.write(sep)
                
    def output_users(self, filename = 'MyCollege_users.txt'):
        
        
api = StudentAccountsApi()
api.output_student_accounts()