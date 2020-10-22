import inCollege_Accnt as accnt
import inCollege_Database as database
import inCollege_CurrentUser as user
import time


def jobMenu(fullname, DB):
    print("         + ----------- +")
    print("         |   JOB MENU  |         ")
    print(" +------------------------------+")
    print(" | 1. Post Job                  |")
    print(" | 2. Remove Job                |")
    print(" | 3. Apply for Job             |")
    print(" | 4. See all Jobs              |")
    print(" | 5. View my Applied Jobs      |")
    print(" | 6. View all Unapplied Jobs   |")
    print(" | 7. View my Saved Jobs        |")
    print(" | x. Quit                      |")
    print(" +------------------------------+")
    print("")
    sel = input("Enter Your Selection: ")

    if sel == '1':  # Post Job function
        accnt.post_job(fullname, DB)

    if sel == '2':  # Remove Job function
        # placeholder
        print("Under construction \n")

    if sel == '3':  # Apply for Job function
        # placeholder
        print("Under construction \n")

    if sel == '4':  # View all jobs
        # placeholder
        print("Under construction \n")

    if sel == '5':  # View all jobs that the student has applied to
        # placeholder
        print("Under construction \n")

    if sel == '6':  # View all jobs the student has NOT applied to
        # placeholder
        print("Under construction \n")

    if sel == '7':  # View all jobs the student has saved
        # placeholder
        print("Under construction \n")

    if sel == 'x':
        print("       + --------- +")
        print("       | Good Bye! |")
        print("       + --------- +")
        time.sleep(1)
        return False
