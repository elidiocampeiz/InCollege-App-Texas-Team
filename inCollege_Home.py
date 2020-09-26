#Front page
#Displays the selected options (and sub-options, if applies)
#calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database
import inCollege_CurrentUser as user


def skillScreen():
    print("  *** Type 'x' at any time to go back to main menu ***\n")
    print("+-------------------+")
    print("|   Learn a Skill   |")
    print("+-------------------+")
    print("+-----------------+")
    print("|   1. Python     |")
    print("|   2. Java       |")
    print("|   3. C ++       |")
    print("|   4. HTML       |")
    print("|   5. Git        |")
    print("+-----------------+\n")

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
    print("====================")
    print("|||IN COLLEGE APP|||")
    print("====================")
    print("+---------------------------------------------------------------------------------------------------+")
    print("|When I was in college, I didn't know what to do with myself.                                       |")
    print("|I was well on my way to graduation, but I had no experience, no internships lined up, nothing.     |")
    print("|Then a friend pointed me to inCollege and it changed my future forever.                            |")
    print("|InCollege is a wonderful tool to connect college hopefuls to one another and to future employers.  |")
    print("|It's easy to use and it gave me results in no time at all.                                         |")
    print("|I went from having no prospects to an internship at a major company in a matter of weeks!          |")
    print("|It's not an exaggeration to say that I wouldn't have been as successful as I am without inCollege. |")
    print("|So I can't recommend it enough. Give it a chance and it will change your life for the better!      |")
    print("|--Dick Tracey, Computer Science Graduate from USF, Chief Software Engineer at Microsoft.           |")
    print("+---------------------------------------------------------------------------------------------------+\n")
    print("Would you like to know more?")

    print("+-------------------------+")
    print("|0. Skip Video |")
    print("|1. View Video |")
    print("+-------------------------+")

    sel = '-1'
    played = False
    sel = input("Enter Your Selection:\n")
    while (sel != '0' and sel != '1'):
        sel = input("Invalid Entry. Enter 0 or 1.")

    if (sel == '1'):
        print("Video is now playing.")
        print("|---------------------------------|")
        print("|------------- |\ ----------------|")
        print("|------------- | \ ---------------|")
        print("|------------- |  \ --------------|")
        print("|------------- |  / --------------|")
        print("|------------- | / ---------------|")
        print("|------------- |/ ----------------|")
        print("|---------------------------------|")
        played = True

    return played


def main ():
    # This is the database object
    # maintaining the database for our program
    db = database.Database()

    mainMenuIntroMessage()
    loginStatus = False
    sel = ''
    print("   Welcome to InCollege!")

    while (sel != 'x'):

        #This menu is displayed to non-logged in user
        if (loginStatus == False):
            print("+-------------------------+")
            print("|1. Login                 |")
            print("|2. Create New Account    |")
            print("|3. Find Someone You Know |")
            print("|x. Quit                  |")
            print("+-------------------------+")
            sel = input("Enter your selection:\n")
            print("")
            if (sel == 'x' or sel == '0'):
                print("Goodbye!")
                # Ignore everything between '=====' (Printing DB results)
                # ========================================================
                # db = database.Database()
                # print("Students in database: ", db.data["Students"])
                # print("Jobs in database: ", db.data["Jobs"])
                # =========================================================
                return 0
            elif (sel == '1'): #Log In. if log in is successful, the user object is returned. Otherwise, false is returned.
                theUser = accnt.login(db)
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True
            elif (sel == '2'): #Create an account
                accnt.create_account(db)

            elif (sel == '3'): #Find Someone You Know
                foundUser = db.search_users() #returns t / f
                theUser = False
                if (foundUser == True):
                    print("They are a part of the InCollege system! "
                          "\nWhy don't you join them?")
                    print("+-------------------------+")
                    print("|1. Login                 |")
                    print("|2. Create New Account    |")
                    print("|x. Go To Main Menu       |")
                    print("+-------------------------+")
                    sel = input("Enter your selection:\n")
                    while (sel != 'x'):
                        sel = input("Input 1 to log in. Input 2 to sign up. Input 0 to continue without logging in or signing up: ")
                        if (sel == '1'):
                            theUser = accnt.login(db)
                            return theUser
                            break
                        elif (sel == '2'):
                            accnt.create_account()
                            print("Please log in from the home page!")
                            break
                        else:
                            print(
                                "Invalid selection. Input 1 to log in. Input 2 to sign up. Input 0 to continue without logging in or signing up: ")
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True

            #Erases the database
            elif (sel == "-100"):
                db.clear()
            else:
                print("Invalid Selection!")

        # if User is logged in
        else:

            print("+------------------------------+")
            print("|1. Post a Job                 |")
            print("|2. Job / Internship Search    |")
            print("|3. Find Someone You Know      |")
            print("|4. Learn a New Skill          |")
            print("|x. Quit                       |")
            print("+------------------------------+")
            print("")
            sel = input("Enter Your Selection:\n ")
            if (sel == 'x'):
                print("Goodbye!")
                # Ignore everything between '====='(Printing DB results)
                # =========================================================
                # db = database.Database()
                # print("Students in database: ", db.data["Students"])
                # print("Jobs in database: ", db.data["Jobs"])
                # =========================================================
                return 0
            elif (sel == '1'): # Post A Job
                accnt.post_job(theUser.name, db)
            elif (sel == '2'):
                print("Under construction.")                
            elif (sel == '3'): # Find someone you know
                db = database.Database()
                db.search_users()
            elif (sel == '4'): # Learn a New Skill
                skillScreen()
            elif (sel == "-100"):
                db.clear()
            else:
                print("Invalid Selection!")




if __name__=='__main__':
    main()
