#Front page
#Displays the selected options (and sub-options, if applies)
#calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database
import inCollege_CurrentUser as user
import time

#Note - When going back, and when an error occurs, the program sleeps for 1 second for added effect


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
            print("... Going Back")
            time.sleep(1)
            return False
        else:
            print("...Invalid Input")
            time.sleep(1)


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
        print("... Invalid Entry")
        time.sleep(1)
        sel = input("Enter Your Selection: ")


    if (sel == '1'):
        print("\n\n")
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

        #This menu is displayed to non-logged in user. 
        if (loginStatus == False):

            #in this case we navigated from somewhere else to create a new account
            if sel == "@": 
                sel = "2"
            else:
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
                # Ignore everything between '=====' (Printing DB results), Do Not Delete*
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

            #Create an account
            elif sel == '2': 
                accnt.create_account(db)

            #Find Someone You Know
            elif sel == '3': 
                foundUser = db.search_users() #returns t / f
                theUser = False
                if foundUser == True:
                    print("\nThey are a part of the InCollege system!")
                    print("Why don't you join them?\n")
                    time.sleep(1)

                    while sel != 'x': 
                        print("+-------------------------+")
                        print("| 1. Login                |")
                        print("| 2. Create New Account   |")
                        print("| x. Go Back to Main Menu |")
                        print("+-------------------------+")
                        sel = input("\nEnter Your Selection: ")

                        if sel == '1':
                            theUser = accnt.login(db)
                            if theUser is False:
                                print("...\n")
                                time.sleep(1)
                                loginStatus = False
                            else:
                                loginStatus = True
                        elif sel == '2':
                            isAccount = accnt.create_account(db)

                            #If the account was made without the use selecting to go back
                            if isAccount is True:
                                print("Log in from the Main Menu")
                                break

                            elif isAccount is False:
                                print("...\n")
                                time.sleep(1)

                        elif sel == 'x':
                            print("...\n")
                            time.sleep(1)
                        else:
                            print("... Invalid Input")
                            time.sleep(1)

                    sel = '' #resetting from 'x' to fix problem where programming was exitting 
                if theUser is False:
                    loginStatus = False
                else:
                    loginStatus = True

            # Useful Links
            elif sel == '4':
                #This will control the loop for Useul Links, when we want to exit the loop the flag will be flipped
                flag = True
                while flag is True:

                    if sel == "@": # in this case we are going back to main menu
                        sel = "@"

                    else:
                        print("       + -------------- +")
                        print("       |  USEFUL LINKS  |         ")
                        print(" +------------------------------+")
                        print(" | 1. General                   |")
                        print(" | 2. Browse inCollege          |")
                        print(" | 3. Business Solutions        |")
                        print(" | 4. Directories               |")
                        print(" | x. Go Back                   |")
                        print(" +------------------------------+")

                        sel = input("\nEnter Your Selection: ")

                    if sel == "@":
                        flag = False
                    
                    #General
                    elif sel == '1':
                        flag2 = True
                        while flag2 is True:

                            if sel == "@": #in this case we are navigating back to main
                                sel = "@"
                            else:
                                print("    + --------- +")
                                print("    |  GENERAL  |")
                                print(" +------------------+")
                                print(" | 1. Sign Up       |")
                                print(" | 2. Help Center   |")
                                print(" | 3. About         |")
                                print(" | 4. Press         |")
                                print(" | 5. Blog          |")
                                print(" | 6. Careers       |")
                                print(" | 7. Developers    |")
                                print(" | x. Go Back       |")
                                print(" +------------------+")
                                
                                sel = input("\nEnter Your Selection: ")


                            if sel == "@":
                                flag2 = False

                            elif sel == "1":
                                flag3 = True
                                while flag3 is True:
                                    print("+----------------------------+")
                                    print("|   Sign Up For inCollege?   |")
                                    print("+----------------------------+")
                                    print("| 1. Yes                     |")
                                    print("| x. Go Back                 |")
                                    print("+----------------------------+\n\n")
                                    sel = input("Enter Your Selection: ")
                                    if sel == "1":
                                        #Whenever "@" shows up in this program it is in reference to accessing another spot in menu
                                        sel = "@"
                                        flag3 = False
                                    elif sel == "x":
                                        flag3 = False
                                        print("...Going back")
                                        time.sleep(1)
                                    else:
                                        print("...Invalid Input")
                                        time.sleep(1)
                                if sel == "@": #"@" indicates we are going back to main to sign in
                                    sel="@"
                                else:
                                    sel = "" #resetting


                            elif sel == "2":
                                print()
                                print("+========================+")
                                print("|*| We're Here to Help |*|")
                                print("+========================+\n")
                            elif sel == "3":
                                print()
                                print("+========================+")
                                print("|*| Our About Goes Here |*|")
                                print("+========================+\n")

                            elif sel == "4": 
                                print()
                                print("+========================+")
                                print("|*| Under Construction |*|")
                                print("+========================+\n")

                            elif sel == "5":
                                print()
                                print("+========================+")
                                print("|*| Under Construction |*|")
                                print("+========================+\n")

                            elif sel == "6":
                                print()
                                print("+========================+")
                                print("|*| Under Construction |*|")
                                print("+========================+\n")

                            elif sel == "7":
                                print()
                                print("+========================+")
                                print("|*| Under Construction |*|")
                                print("+========================+\n")

                            elif sel == "x":
                                flag2 = False
                                print("... Going Back")
                                time.sleep(1)

                            else:
                                print("...Invalid Input")
                                time.sleep(1)

                        if sel == "@": #This means we are navigating back to create an account
                            print()
                        else:
                            sel = "" #resetting sel


                    #Browse inCollege
                    elif sel == '2':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    #Business Solutions
                    elif sel == '3': 
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")                    
                    #Directories
                    elif sel == '4':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")                    
                    #Go Back
                    elif sel == 'x':
                        flag = False
                        print("... Going Back")
                        time.sleep(1)

                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                
                if sel == "@":
                    sel = "@"
                else:
                    sel = "" #resetting sel

            # inCollege Important Links
            elif sel == '5':
                flag = True
                while flag is True:
                    print("+---------------------------+")
                    print("| inCollege Important Links |")
                    print("+---------------------------+")
                    print("| 1. Copyright Notice       |")
                    print("| 2. About                  |")
                    print("| 3. Accessibility          |")
                    print("| 4. User Agreement         |")
                    print("| 5. Privacy Policy         |")
                    print("| 6. Cookie Policy          |")
                    print("| 7. Brand Policy           |")
                    print("| 8. Languages              |")
                    print("| x. Go Back                |")
                    print("+---------------------------+\n")

                    sel = input("Enter Your Selection: ")

                    if sel == "1":
                        print("Our Copyright notice goes here")
                    elif sel == "2":
                        print("Our About goes here")

                    elif sel == "3":
                        print("Our Accessibility goes here")

                    elif sel == "4":
                        print("Our User Agreement goes here")

                    elif sel == "5":
                        print(" +-------------------------+")
                        print(" |     Privacy Policy      |")
                        print(" +-------------------------+\n")
                        print("Our Privacy Policy is written here...\n")
                        flag2 = True
                        while flag2 is True:
                            print("+--------------------------+")
                            print("|   Edit Guest Controls?   |")
                            print("+--------------------------+")
                            print("| 1. Yes                   |")
                            print("| x. Go Back               |")
                            print("+--------------------------+\n")
                            sel = input("Enter Your Selection: ")

                            if sel == "1":
                                print("Editing Guest Controls")

                            elif sel == "x":
                                flag2 = False
                                print("... Going Back")
                                time.sleep(1)

                            else:
                                print("... Invalid Input")
                                time.sleep(1)

                        sel = "" #resetting
                
                    elif sel == "5":
                        print("Our Privacy Policy goes here")

                    elif sel == "6":
                        print("Our Cookie Policy goes here")


                    elif sel == "7":
                        print("Our Brand Policy goes here")

                    elif sel == "8":
                        flag2 = True
                        while flag2 is True:
                            print("+---------------------------------------+")
                            print("|   Language Settings Guest Controls?   |")
                            print("+---------------------------------------+")
                            print("| 1. Change Settings                    |")
                            print("| x. Go Back                            |")
                            print("+---------------------------------------+\n")
                            sel = input("Enter Your Selection: ")

                            if sel == "1":
                                print("Change the Settings")
                            elif sel == "x":
                                flag2 = False
                                print("... Going Back\n")
                                time.sleep(1)

                        sel = "" #resetting sel

                    elif sel == "x":
                        flag = False
                        print("... Going Back\n")
                        time.sleep(1)

                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                sel = "" #resetting

            #Erases the database
            elif sel == "-100":
                db.clear()
            else:
                print("...")
                time.sleep(1)
                print("Invalid Input")
                time.sleep(1)

        # if User is logged in
        else:

            print("         + ----------- +")
            print("         |  MAIN MENU  |         ")
            print(" +------------------------------+")
            print(" | 1. Post a New Job            |")
            print(" | 2. Find Someone You Know     |")
            print(" | 3. Skill Screen              |")
            print(" | 5. Useful Links              |")
            print(" | 6. InCollege Important Links |")
            print(" | x. Quit                      |")
            print(" +------------------------------+")
            print("")
            sel = input("Enter Your Selection: ")
            
            # Post A Job
            if sel == '1': 
                accnt.post_job(theUser.name, db)

            # Find someone you know
            elif sel == '2': 
                db = database.Database()
                foundUser = db.search_users()
                if foundUser is True:
                    print("... User found in the inCollege System!")
                    time.sleep(1)
                    
            # Learn a New Skill        
            elif sel == '3': 
                skillScreen()

            #Exit Program    
            elif sel == 'x':
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
            elif sel == "-100":
                db.clear()
            else:
                print("...Invalid Input")
                time.sleep(1)




if __name__=='__main__':
    main()
