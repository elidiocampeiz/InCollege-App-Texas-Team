#Front page
#Displays the selected options (and sub-options, if applies)
#calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database

def skillScreen():
    print("")
    print("1. Python")
    print("2. Java")
    print("3. C++")
    print("4. Teams")
    print("5. Git")
    sel = int(input("Please make a selection. Input any number not listed above to return to main menu: "))
    selectionScreen(sel)

def selectionScreen(val):
    if val in range(1,6):
        print("Under construction.")
        return True
    return False

def mainMenuIntroMessage():
    print("When I was in college, I didn't know what to do with myself.")
    print("I was well on my way to graduation, but I had no experience, no internships lined up, nothing.")
    print("Then a friend pointed me to inCollege and it changed my future forever.")
    print("InCollege is a wonderful tool to connect college hopefuls to one another and to future employers.")
    print("It's easy to use and it gave me results in no time at all.")
    print("I went from having no prospects to an internship at a major company in a matter of weeks!")
    print("It's not an exaggeration to say that I wouldn't have been as successful as I am without inCollege.")
    print("So I can't recommend it enough. Give it a chance and it will change your life for the better!")
    print("--Dick Tracey, Computer Science Graduate from USF, Chief Software Engineer at Microsoft.")
    print("")

    print("Would you like to know more?")
    sel = -1
    sel = int(input("Input 1 to view the video. Input any other number to skip: "))
    if (sel == 1):
        print("Video is now playing.")
    print("")

def main ():
    mainMenuIntroMessage()
    loginStatus = False
    sel = -1
    print("Welcome to InCollege!")
    while (sel != 0):
        if (loginStatus == False):
            print("")
            print("1. Login")
            print("2. Create New Account")
            print("")
            print("3. Job/Internship Search")
            print("4. Find Someone You Know")
            print("5. Learn a New Skill")
            print("")
            sel = int(input("Please make a selection, input 0 to Quit: "))
            print("")
            if (sel == 0):
                print("Goodbye!")
            elif (sel == 1):
                loginStatus = accnt.login()
            elif (sel == 2):
                accnt.create_account()
            elif (sel == 3):
                print("Under construction.")
            elif (sel == 4):
                #The find someone by their name function goes here.
                print("Under construction.")
            elif (sel == 5):
                skillScreen()
            elif (sel == 6):
                accnt.clear_accounts()
            else:
                print("Invalid Selection!")
        else:
            print("")
            print("1. Post a Job")
            print("")
            print("2. Job/Internship Search")
            print("3. Find Someone You Know")
            print("4. Learn a New Skill")
            print("")
            sel = int(input("Please make a selection, input 0 to Quit: "))
            print("")
            if (sel == 0):
                print("Goodbye!")
            elif (sel == 1):
                print("Awaiting Functionality.")
                #The Job Posting Function goes here.
            elif (sel == 2):
                print("Under construction.")                
            elif (sel == 3):
                #The find someone by their name function goes here.
                print("Awaiting Functionality.")
            elif (sel == 4):
                skillScreen()
            elif (sel == 6):
                accnt.clear_accounts()
            else:
                print("Invalid Selection!")

if __name__=='__main__':
    main()
