#Front page
#Displays the selected options (and sub-options, if applies)
#calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database
import inCollege_CurrentUser as user
import time


def skillScreen():
    print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
    print("+--------------------+")
    print("| Master a New Skill |")
    print("+--------------------+")
    print("+-------------------+")
    print("|    1. Python      |")
    print("|    2. Java        |")
    print("|    3. C ++        |")
    print("|    4. HTML        |")
    print("|    5. Git         |")
    print("+-------------------+\n")

    sel = -1
    while sel != "x":
        sel = input("Make a selection: ")
        if sel == "1":
            print("Under construction.")
            return True
        elif sel == "2":
            print("Under construction.")
            return True
        elif sel == "3":
            print("Under construction.")
            return True
        elif sel == "4":
            print("Under construction.")
            return True
        elif sel == "5":
            print("Under construction.")
            return True
        elif sel == 'x': #Go back to main menu
            return False
        else:
            print("Invalid Input")


# def selectionScreen(val):
#     if val in range(1,6):
#         print("Under construction.")
#         return True
#     return False

def mainMenuIntroMessage():
    print("\n\n\n")
    print("                  +/ ==================== \+")
    print("                  |   inCOLLEGE: The App   |")
    print("                  +\ ==================== /+")
    print("+-------------------------------------------------------------+")
    print("|A User Testimonial:                                          |")
    print("|When I was in college, I didn't know what to do with myself. |")
    print("|I was well on my way to graduation, but I had no experience. |")
    print("|Then a friend pointed me to inCollege and it changed my life |")
    print("|InCollege is a wonderful tool.                               |")
    print("|It's easy to use and it gave me results in no time at all.   |")
    print("|I went from nothing to an internship in a matter of weeks!   |")
    print("|I can't recommend it enough.                                 |")
    print("|Give it a chance and it will change your life for the better!|")
    print("|--Dick Tracey, Chief Software Engineer at Microsoft.         |")
    print("+-------------------------------------------------------------+\n")
    print("\n     Want to watch a video to find out more?                       ")

    print("       +-------------------+")
    print("       |  0. Skip Video    |")
    print("       |  1. Watch a Video |")
    print("       +-------------------+")

    sel = '-1'
    played = False
    sel = input("Enter Your Selection:\n")
    while (sel != '0' and sel != '1'):
        sel = input("Invalid Entry. Enter 0 or 1.")

    if (sel == '1'):
        print("\n\n")
        time.sleep(1)
        print("|================================================|")
        print("|---------------------|\-------------------------|")
        print("|---------------------|-\------------------------|")
        print("|---------------------|--\-----------------------|")
        print("|---------------------|---\----------------------|")
        print("|-------------Video is now playing---------------|")
        print("|---------------------|---/----------------------|")
        print("|---------------------|--/-----------------------|")
        print("|---------------------|-/------------------------|")
        print("|---------------------|/-------------------------|")
        print("|================================================|\n")
        time.sleep(1)

        played = True

    return played


def main ():
    # This is the database object
    # maintaining the database for our program
    db = database.Database()

    mainMenuIntroMessage()
    loginStatus = False
    sel = ''

    while (sel != 'x'):

        #This menu is displayed to non-logged in user
        if (loginStatus == False):
            print("\n")
            print("         + ----------- +")
            print("         |  MAIN MENU  |         ")
            print(" +------------------------------+")
            print(" | 1. Login                     |")
            print(" | 2. Create New Account        |")
            print(" | 3. Find Someone You Know     |")
            print(" | 4. Useful Links              |")
            print(" | 5. InCollege Important Links |")
            print(" | x. Quit                      |")
            print(" +------------------------------+")
            sel = input("\nEnter your selection: ")
            print("")
            if (sel == 'x' or sel == '0'):
                print("       + --------- +")
                print("       | GOOD BYE! |")
                print("       + --------- +")
                time.sleep(1)
                # Ignore everything between '=====' (Printing DB results)
                # ========================================================
                # db = database.Database()
                # print("Students in database: ", db.data["Students"])
                # print("Jobs in database: ", db.data["Jobs"])
                # =========================================================
                return 0
            elif sel == '1': #Log In. if log in is successful, the user object is returned. Otherwise, false is returned.
                theUser = accnt.login(db)
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True
            elif sel == '2': #Create an account
                accnt.create_account(db)

            elif sel == '3': #Find Someone You Know
                foundUser = db.search_users() #returns t / f
                theUser = False
                if foundUser == True:
                    print("\nThey are a part of the InCollege system!")
                    time.sleep(1)
                    print("Why don't you join them?\n")
                    time.sleep(1)

                    while sel != '0': #had to change this to zero to fix problem with program exiting if user places x there
                        print("+-------------------------+")
                        print("| 1. Login                |")
                        print("| 2. Create New Account   |")
                        print("| 0. Go Back to Main Menu |")
                        print("+-------------------------+")
                        sel = input("\nEnter Your Selection: ")

                        if sel == '1':
                            theUser = accnt.login(db)
                            if theUser is False:
                                loginStatus = False
                            else:
                                loginStatus = True
                        elif sel == '2':
                            accnt.create_account(db)
                            print("Log in from the Main Menu")
                            break
                        else:
                            time.sleep(1)
                            print("Invalid selection.")
                            time.sleep(1)
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True

            #Erases the database
            elif sel == "-100":
                db.clear()
            else:
                print("...")
                time.sleep(1)
                print("Invalid Selection!")
                time.sleep(1)

        # if User is logged in
        else:

            print("         + ----------- +")
            print("         |  MAIN MENU  |         ")
            print(" +------------------------------+")
            print(" | 1. Login                     |")
            print(" | 2. Create New Account        |")
            print(" | 3. Find Someone You Know     |")
            print(" | 4. Useful Links              |")
            print(" | 5. InCollege Important Links |")
            print(" | x. Quit                      |")
            print(" +------------------------------+")
            print("")
            sel = input("Enter Your Selection: ")
            if sel == 'x':
                print("       + --------- +")
                print("       | GOOD BYE! |")
                print("       + --------- +")
                time.sleep(1)

                # Ignore everything between '====='(Printing DB results)
                # =========================================================
                # db = database.Database()
                # print("Students in database: ", db.data["Students"])
                # print("Jobs in database: ", db.data["Jobs"])
                # =========================================================
                return 0
            elif sel == '1': # Post A Job
                accnt.post_job(theUser.name, db)
            elif sel == '2':
                print("Under construction.")                
            elif sel == '3': # Find someone you know
                db = database.Database()
                foundUser = db.search_users()
                if foundUser is True:
                    print("...")
                    time.sleep(1)
                    print("User found in the inCollege System!")
                    time.sleep(1)
            elif sel == '4': # Learn a New Skill
                skillScreen()
            elif sel == "-100":
                db.clear()
            else:
                print("Invalid Selection!")




if __name__=='__main__':
    main()
