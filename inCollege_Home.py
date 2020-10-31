# Front page 
# Displays the selected options (and sub-options, if applies)
# calls the relevant functions correlating to user input
import inCollege_Accnt as accnt
import inCollege_Database as database
#import inCollege_CurrentUser as user
import time

# Note - When going back, and when an error occurs, the program sleeps for 1 second for added effecT
#     - The @ symbol means we are navigating back through menu to create a new account


def mainMenuIntroMessage():
    print("\n\n\n")
    print("                   +/ ==================== \+")
    print("                   |   inCOLLEGE: The App   |")
    print("                   +\ ==================== /+")
    print("+--------------------------------------------------------------+")
    print("| A User Testimonial:                                          |")
    print("| When I was in college, I didn't know what to do with myself. |")
    print("| I was well on my way to graduation, but I had no experience. |")
    print("| Then a friend pointed me to inCollege and it changed my life |")
    print("| InCollege is a wonderful tool.                               |")
    print("| It's easy to use and it gave me results in no time at all.   |")
    print("| I went from nothing to an internship in a matter of weeks!   |")
    print("| I can't recommend it enough.                                 |")
    print("| Give it a chance and it will change your life for the better!|")
    print("|     --Dick Tracey, Chief Software Engineer at Microsoft.     |")
    print("+--------------------------------------------------------------+\n")
    print("\n     Want to watch a video to find out more?                       ")
    # test
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


def main():
    # This is the database object
    # maintaining the database for our program
    db = database.Database()

    # Default Settings
    # guest control is a dict {guest_control_type : boolean}
    guest_control = {"Email": True, "SMS": True,  "Targeted Advertising": True}
    # laguage settings
    language = "English"
    settings = {'guest control': guest_control, "language": language}

    mainMenuIntroMessage()
    loginStatus = False
    sel = ''
    # theUser = user.User()
    while (sel != 'x'):

        # This menu is displayed to non-logged in user
        if (loginStatus == False):

            # in this case we navigated from somewhere else to create a new account
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

            # Log In. if log in is successful, the user object is returned. Otherwise, false is returned.
            elif sel == '1':
                # theUser = accnt.login(db)
                theStudent = accnt.login(db)
                if theStudent is False:
                    loginStatus = False
                else:
                    # Update global settings
                    # settings = theUser.student_data['settings']
                    settings = theStudent.settings
                    loginStatus = True

            # Create an account
            elif sel == '2':
                accnt.create_account(db)
            # Find Someone You Know
            elif sel == '3':
                foundUser = db.search_users()  # returns t / f
                isStudentLoggedIn = False
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
                            isStudentLoggedin = accnt.login(db)
                            if isStudentLoggedin is False:
                                print("...\n")
                                time.sleep(1)
                                loginStatus = False
                            else:
                                loginStatus = True
                        elif sel == '2':
                            isAccount = accnt.create_account(db)

                            # If the account was made without the use selecting to go back
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

                    sel = ''  # resetting from 'x' to fix problem where programming was exitting
                if isStudentLoggedin is False:
                    loginStatus = False
                else:
                    loginStatus = True

            # Useful Links
            elif sel == '4':
                # This will control the loop for Useul Links, when we want to exit the loop the flag will be flipped
                flag = True
                while flag is True:

                    if sel == "@":  # in this case we are going back to main menu
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

                    # General
                    elif sel == '1':
                        flag2 = True
                        while flag2 is True:

                            if sel == "@":  # in this case we are navigating back to main
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
                                        # Whenever "@" shows up in this program it is in reference to accessing another spot in menu
                                        sel = "@"
                                        flag3 = False
                                    elif sel == "x":
                                        flag3 = False
                                        print("...Going back")
                                        time.sleep(1)
                                    else:
                                        print("...Invalid Input")
                                        time.sleep(1)
                                if sel == "@":  # "@" indicates we are going back to main to sign in
                                    sel = "@"
                                else:
                                    sel = ""  # resetting

                            elif sel == "2":
                                print("\n                 + ----------- +")
                                print("                 | HELP CENTER |")
                                print(
                                    "+-------------------------------------------------+")
                                print(
                                    "|              Welcome to In College,             |")
                                print(
                                    "| the world's largest college student network     |")
                                print(
                                    "| with users in several countries and territories |")
                                print(
                                    "|                    World Wide                   |")
                                print(
                                    "+-------------------------------------------------+\n")
                            elif sel == "3":
                                print()
                                print("+========================+")
                                print("|*| Our About Goes Here |*|")
                                print("+========================+\n")

                            elif sel == "4":
                                print()
                                print("+---------------------------+")
                                print("|  In College Pressroom:    |")
                                print("| Stay on top of the latest |")
                                print("| news, updates, and reports|")
                                print("+---------------------------+\n")

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

                        if sel == "@":  # This means we are navigating back to create an account
                            print()
                        else:
                            sel = ""  # resetting sel

                    # Browse inCollege
                    elif sel == '2':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Business Solutions
                    elif sel == '3':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Directories
                    elif sel == '4':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Go Back
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
                    sel = ""  # resetting sel

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
                        print("The contents of this website, including but not limited to all, all written materials, images, photos, and code are protected under international copyright and trademark laws. You may not in any circumstances copy, reproduce, modify, republish and transmit or distribute an material from this site without express written permission.\nInCollege reserves the right, however, to make changes at its discretion affecting policies, fee or other matters announced on this site.")
                    elif sel == "2":
                        print("This application is designed to allow college students to create personal accounts, upload profile information, search for and apply for jobs, and connect with other students both at their college and at other colleges. These specifications are designed to lay out the functionality that will be provided by an alpha version of this program. The intended functionality is just enough to be able to demo to groups of investors as we attempt to spark their interest in the project and get them to commit to funding future versions of the software.")

                    elif sel == "3":
                        print("InCollege has utilized guidelines to implement functional improvements to InCollege. We are working to ensure that all contents on the InCollege site meet the level AA success criteria set forth in WCAG 2.0.\nIf you have any question or comments, please contact our professor Dr. James Anderson.")

                    elif sel == "4":
                        useragreement = """
                                This Website User Agreement and the Privacy Policy lays out the terms and conditions and rules, as maybe amended and supplemented, from time to time (hereinafter referred to as the “Agreement”) which shall be applicable to the access and use of the website of inCollege by you, the visitor/ user (“User”) of the Website. 
                                
                                1. ACCEPTANCE OF TERMS AND MODIFICATION THEREOF  
                                1.1	Access of the Website by the User constitutes an acknowledgement and acceptance in full, of all the terms, conditions and notices as stated in this Agreement and without any modification and/or exception by the User of this Agreement. If the User does not agree with any part of such terms, conditions and notices as stated in this Agreement in any manner, the User must not access the Website.  
                                1.2	inCollege reserves the right to change the terms, conditions and notices pursuant to which the Website is accessed by the User, without any notice or intimation of such change.  
                                
                                2. LIMITED USER
                                2.1 The User agrees that given the nature of the Internet, even though the Website is targeted to Indian Residents only, it may be accessed in other parts of the world. The material/information on this Website is not intended for use by persons located in, or residents in countries that restrict the distribution of such material/information or by any person in any jurisdiction where distribution or use of such material/information or usage or access of Website will be contrary to law or any regulation. It shall be the responsibility of every User to be aware of and fully observe the applicable laws and regulations of the jurisdiction which User is subject of.  If the User is not an Indian resident and yet uses this Website, he acknowledges, understands and agrees that he is doing so on his own initiative and at his own risk and inCollege shall not be liable for violation/breach of any of the laws applicable to usage of the Website. The Website is not to be and should not be construed as purporting to offer or inviting to offer any information to residents of countries where inCollege is not licensed or authorized to perform activities related to its objective.  
                                2.2 The User further agrees and undertakes not to reverse engineer, modify, copy, distribute, transmit, display, perform, reproduce, publish, license, create derivative works from, transfer, or sell any information, software, products, services or intellectual property obtained from the Website in any manner whatsoever.   Reproduction, copying of the content for commercial or non‐commercial purposes and unwarranted modification of data and information within the content of the Website is strictly not permitted without prior written consent from inCollege and/or third party owners. However, some of the content of our services or other files may be made available for download from the website which is  permitted to be copied and/or used only for personal purposes of the User.   The User and/or any third party is prohibited from running or displaying this Website and /or information displayed on this Website on any other Website or frames , without prior written consent from inCollege.
                                
                                3. DISCLAIMER OF WARRANTIES  
                                3.1 INCOLLEGE has endeavored to ensure that all the information provided by it on this Website is correct, but INCOLLEGE neither warrants nor makes any representations regarding the quality, accuracy or completeness of any data or information displayed on this Website and INCOLLEGE shall not be, in any manner liable for inaccuracy/error if any. INCOLLEGE makes no warranty, express or implied, concerning the Website and/or its contents and disclaims all warranties of fitness for a particular purpose and warranties of merchantability in respect of information displayed and communicated through or on the Website, including any liability, responsibility or any other claim, whatsoever, in respect of any loss, whether direct or consequential, to any User or any other person, arising out of or from the use of any such information as is displayed or communicated through or on the Website or the provision of the Services. 
                                3.2   INCOLLEGE shall not be held responsible for non‐availability of the Website at any point in time for any reason whatsoever. The User understands and agrees that any material and/or data downloaded or otherwise obtained from INCOLLEGE through the Website is done entirely at his discretion and risk and he will be solely responsible for any damage to his computer systems or any other loss that results from such material and/or data
                                
                                4.       LINKS TO THIRD PARTY SITES   
                                4.1 The Website may contain links to other websites or may contain features of any nature of other websites on the Website ("Linked Sites"). The Linked Sites are not under the control of INCOLLEGE or the Website and INCOLLEGE is not responsible for the contents of any Linked Site, including without limitation any link or advertisement contained in a Linked Site, or any changes or updates to a Linked Site. INCOLLEGE is not responsible for any form of transmission, whatsoever, received by the User from any Linked Site.  The inclusion of any link does not imply endorsement of any nature by INCOLLEGE or the Website of the Linked Sites or any association with its operators or owners.   
                                4.2   INCOLLEGE is not responsible for any errors, inclusions, omissions or representations on any Linked Site, or on any link contained in a Linked Site.    The User is requested to verify the accuracy of all information on his own before undertaking any reliance on such information of such products/ services that they believe may benefit the User. 
                                
                                5. USER'S OBLIGATIONS   
                                5.1 As a condition of access and use of the Website, the User warrants that he will not use the Website for any purpose that is unlawful or illegal under any law for the time being in force within or outside India or prohibited by this Agreement. In addition, the Website shall not be used in any manner, which could damage, disable, overburden or impair it or interfere with any other party's use and/or 
                                
                                6.   CONTACT US FEATURE 
                                6.1 The Users will be provided with Contact Us features on the Website. The Users will be able to provide their contact details to enable INCOLLEGE to contact them. 
                                6.2 The Users may further be provided with features to contact INCOLLEGE, raise queries, comments or interact with INCOLLEGE. However INCOLLEGE shall be at its sole discretion and be within its rights to answer, reply or opt not to reply to any such queries or comments. 
                                6.3 By using the said features, User permits INCOLLEGE to contact them on their registered details, for any clarification or to offer any other service from time to time.          
                                
                                7. BREACH 
                                7.1 Without prejudice to the other remedies available to INCOLLEGE under this Agreement or under applicable law, INCOLLEGE may limit the User's activity, warn other Users of the User's actions, immediately temporarily / indefinitely suspend or terminate the User’s use of the Website, and/or refuse to provide the User with access to the Website if the User is in breach of this Agreement.      
                                
                                8. OWNERSHIP AND PROPRIETARY RIGHTS
                                8.1 The content of the Website and all copyrights, patents, trademarks, service marks, trade names and all other intellectual property rights therein are owned by INCOLLEGE or validly  licensed to INCOLLEGE  and are protected by applicable USA and international copyright and other intellectual property law. The User acknowledges, understands and agrees that he shall not have, nor be entitled to claim, any rights in and to the Website content and/or any portion thereof. 
                                8.2 Some of the content on the Website have been permitted by the third party/ies to be used by INCOLLEGE in such form and manner as may be desired by INCOLLEGE and INCOLLEGE will makes its best endeavors to give credit to such third party/ies during publication of such content on its Website. If at any point in time any dispute is raised with respect to publication of such content, by any third party, INCOLLEGE shall be in its rights to remove such content or procure requisite consents from third party/ies.    
                                8.3 Any copyrighted or other proprietary content distributed on or through the Website with the consent of the owner must contain the appropriate copyright or other proprietary rights notice. The unauthorized submission or distribution of copyrighted or other proprietary content is illegal and could subject the User to personal liability or criminal prosecution.
                                
                                9. LIMITATION OF LIABILITY   
                                9.1 The user understands and expressly agrees that to the extent permitted under applicable laws, in no event will the incollege or any of its affiliates or parent company or any of their respective officers, employees, directors, shareholders, agents, or licensors be liable to the user or anyone else under any theory of liability (whether in contract, tort, statutory, or otherwise) for any direct, indirect, incidental, special, consequential or exemplary damages, including but not limited to, damages for loss of revenues, profits, goodwill, use, data or other intangible losses (even if such parties were advised of, knew of or should have known of the possibility of such damages), resulting from the user’s use  of or inability to use the website or any parts thereof. 
                                
                                10. INDEMNIFICATION 
                                10.1 The User agrees to indemnify, defend and hold harmless INCOLLEGE, its affiliates, group companies and their directors, officers, employees, agents, third party service providers, and any other third   party providing any service to INCOLLEGE in relation to the Website  whether directly or indirectly, from and against any and all losses, liabilities, claims, damages, costs and expenses (including legal fees and disbursements in connection therewith and interest chargeable thereon) asserted against or incurred by INCOLLEGE that arise out of, result from, or may be payable by virtue of, any breach or non‐performance of any terms of this Agreement including any representation, warranty, covenant or agreement made or obligation to be performed by the User pursuant to this Agreement. 
                                
                                11. SEVERABILITY 
                                11.1 If any provision of this Agreement is determined to be invalid or unenforceable in whole or in part, such invalidity or unenforceability shall attach only to such provision or part of such provision and the remaining part of such provision and all other provisions of this Agreement shall continue to be in full force and effect.     
                                
                                12. GOVERNING LAW   
                                12.1 This Agreement shall be governed by and constructed in accordance with the laws of United States of America without reference to conflict of laws principles. In the event any dispute in relation hereto is brought by the User, it shall be subject to the exclusive jurisdiction of the courts of United States of America.  
                                """
                        print(useragreement)

                    elif sel == "5":
                        print(" +-------------------------+")
                        print(" |     Privacy Policy      |")
                        print(" +-------------------------+\n")
                        print("For policy in Pirvacy, please refer back to the User agreement \n")
                        flag2 = True
                        while flag2 is True:
                            targeted_advertising = "ON" if settings['guest control']['Targeted Advertising'] == True else "OFF"
                            SMS = "ON" if settings['guest control']['SMS'] == True else "OFF"
                            email = "ON" if settings['guest control']['Email'] == True else "OFF"
                            print("+--------------------------+")
                            print("| Default Guest Controls:  |")
                            print("+--------------------------+")
                            # the Menu is Aligned 
                            print(f"| Email:       {email}          |")
                            print(f"| SMS:         {SMS}          |")
                            print(f"| Advertising: {targeted_advertising}          |")
                            print("| x. Go Back               |")
                            print("+--------------------------+\n")
                            sel = input("Enter Your Selection: ")

                            # if sel == "1":
                            #     print("Editing Guest Controls")

                            if sel == "x":
                                flag2 = False
                                print("... Going Back")
                                time.sleep(1)

                            else:
                                print("... Invalid Input")
                                time.sleep(1)

                        sel = ""  # resetting

                    elif sel == "6":
                        cookieprivacy = """
                        \nWhat are cookies?
                        Cookies are simple text files that are stored on your computer or mobile device by a website’s server. Each cookie is unique to your web browser. It will contain some anonymous information such as a unique identifier, website’s domain name, and some digits and numbers.
                        
                        \nWhat types of cookies do we use?
                        Necessary cookies
                        Necessary cookies allow us to offer you the best possible experience when accessing and navigating through our website and using its features. For example, these cookies let us recognize that you have created an account and have logged into that account to access the content.
                        
                        \nFunctionality cookies
                        Functionality cookies let us operate the site in accordance with the choices you make. For example, we will recognize your username and remember how you customized the site during future visits.
                        
                        \nAnalytical cookies
                        These cookies enable us and third-party services to collect aggregated data for statistical purposes on how our visitors use the website. These cookies do not contain personal information such as names and email addresses and are used to help us improve your user experience of the website.
                       
                        \nHow to delete cookies?
                        If you want to restrict or block the cookies that are set by our website, you can do so through your browser setting. Alternatively, you can visit www.internetcookies.org, which contains comprehensive information on how to do this on a wide variety of browsers and devices. You will find general information about cookies and details on how to delete cookies from your device.

                        \nContacting us
                        If you have any questions about this cookie policy or our use of cookies, please contact us.
                        """
                        print(cookieprivacy)


                    elif sel == "7":
                        print("For policy in brands, please refer back to the User agreement ")

                    elif sel == "8":
                        flag2 = True
                        while flag2 is True:
                            language = settings['language']
                            print("+----------------------------+")
                            print("|      Language Settings:    |")
                            print("+----------------------------+")
                            #"English" or "Spanish"
                            print(f"| Language:     {language}      |")
                            print("| x. Go Back                 |")
                            print("+----------------------------+\n")
                            sel = input("Enter Your Selection: ")

                            # if sel == "1":
                            #     print("Change the Settings")
                            if sel == "x":
                                flag2 = False
                                print("... Going Back\n")
                                time.sleep(1)

                        sel = ""  # resetting sel

                    elif sel == "x":
                        flag = False
                        print("... Going Back\n")
                        time.sleep(1)

                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                sel = ""  # resetting

            # Erases the database
            elif sel == "-100":
                db.clear()
            else:
                print("...")
                time.sleep(1)
                print("Invalid Input")
                time.sleep(1)

        # if User is logged in
        else:

            #Displaying friend requests
            while(accnt.diplay_friend_request_list(db, theStudent)):
                pass

            #Printing out how many messages are in the users inbox    
            isMessage = accnt.display_number_in_inbox(theStudent)


            print("         + ----------- +")
            print("         |  MAIN MENU  |         ")
            print(" +------------------------------+")
            print(" | 1. Jobs                      |")
            print(" | 2. Find Someone You Know     |")
            print(" | 3. Skill Screen              |")
            print(" | 4. Useful Links              |")
            print(" | 5. InCollege Important Links |")
            print(" | 6. View Profile              |")
            print(" | 7. View Friends              |")
            print(" | 8. Find Friends              |")
            print(" | 9. Messaging                 |")
            print(" | x. Quit                      |")
            print(" +------------------------------+")
            print("")
            sel = input("Enter Your Selection: ")

            # Jobs
            if sel == '1':
                print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                flag = True
                while flag is True:
                    print("            +--------+")
                    print("            |  Jobs  |         ")
                    print(" +------------------------------+")
                    print(" | 1. Post a Job                |")
                    print(" | 2. See Job Listing           |")
                    print(" | 3. Jobs Already Applied For  |")
                    print(" | 4. Jobs Not Yet Applied For  |")
                    print(" | 5. Saved (Maybe Apply Later) |")
                    print(" | 6. Remove a Job You Posted   |")
                    print(" | x. Go Back                   |")
                    print(" +------------------------------+")

                    sel = input("Make a selection: ")

                    # Post a job
                    if sel == '1':
                        accnt.post_job(
                            theStudent.firstname+" "+theStudent.lastname, theStudent.username, db)

                    # See Job Listing
                    elif sel == "2":
                        print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                        flag2 = True
                        while flag2 is True:
                            print("          +---------------+")
                            print("          |  Job Listing  |         ")
                            print("+----------------------------------+")
                            print("|      Job Titles Listed Below     |")
                            print("+----------------------------------+")
                            for jobs in db.data["Jobs"]:
                                indication = ""
                                for vals in jobs['users_applied']:
                                    # means user has already applied
                                    if vals['username'] == theStudent.username:
                                        indication = "(Applied)"
                                print("|----> ", jobs['title'], indication)

                            print("+----------------------------------+")
                            print("| To see more about a specific job,|")
                            print("| type out the Job Title below;    |")
                            print("| or type x to go back.            |")
                            print("+----------------------------------+")
                            jobTitle = input("Type Here: ")

                            # If user doesn't enter
                            if jobTitle == "x":
                                flag2 = False
                            else:
                                # displays info, return true if job is real false if not found
                                isFound = accnt.display_job_info(db, jobTitle)
                                if isFound:
                                    print("+-----------------------------+")
                                    print("|1. Apply for the job         |")
                                    print("|2. Save the job for later    |")
                                    print("|x. Niether                   |")
                                    print("+-----------------------------+")

                                    sel = input("Make a selection: ")

                                    # Apply for job
                                    if sel == "1":
                                        # returns true if applied successfully, false otherwise
                                        hasApplied = accnt.apply_for_job(
                                            db, jobTitle, theStudent.username)

                                        if hasApplied is True:
                                            print("Successfully Applied!")
                                        else:
                                            print("Application Error")

                                    # Save Job
                                    elif sel == "2":
                                        # returns true if saved succesfully, false otherwise
                                        hasSaved = accnt.save_job(
                                            db, jobTitle, theStudent.username)

                                        if hasSaved:
                                            print("Successfully Saved!")
                                        else:
                                            print("Error saving job...")
                                # Job was not found
                                else:
                                    print(
                                        "Job title does not exist in the database.")

                        sel = ""  # resetting

                    # Jobs Already Applied For
                    elif sel == "3":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                        # Need to show jobs
                        # Press Job to expand it
                        print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                        flag2 = True
                        while flag2 is True:
                            print("   +---------------------------+")
                            print("   |  Job Already Applied For  |   ")
                            print("+----------------------------------+")
                            print("|      Job Titles Listed Below     |")
                            print("+----------------------------------+")
                            for jobs in db.data["Jobs"]:
                                for vals in jobs['users_applied']:
                                    # if the user saved the job
                                    # means user has already applied
                                    if vals['username'] == theStudent.username:
                                        print("|----> ", jobs['title'])

                            print("+----------------------------------+")
                            print("| To see more about a specific job,|")
                            print("| type out the Job Title below;    |")
                            print("| or type x to go back.            |")
                            print("+----------------------------------+")
                            jobTitle = input("Type Here: ")

                            # If user doesn't enter
                            if jobTitle == "x":
                                flag2 = False
                            else:
                                # displays info, return true if job is real false if not found
                                isFound = accnt.display_job_info(db, jobTitle)
                                if isFound:
                                    print("+-----------------------------+")
                                    print("|1. Apply for the job         |")
                                    print("|2. Save the job for later    |")
                                    print("|x. Niether                   |")
                                    print("+-----------------------------+")

                                    sel = input("Make a selection: ")

                                    # Apply for job
                                    if sel == "1":
                                        # returns true if applied successfully, false otherwise
                                        hasApplied = accnt.apply_for_job(
                                            db, jobTitle, theStudent.username)

                                        if hasApplied is True:
                                            print("Successfully Applied!")
                                        else:
                                            print("Application Error")

                                    # Save Job
                                    elif sel == "2":
                                        # returns true if saved succesfully, false otherwise
                                        hasSaved = accnt.save_job(
                                            db, jobTitle, theStudent.username)

                                        if hasSaved:
                                            print("Successfully Saved!")
                                        else:
                                            print("Error saving job...")
                                # Job was not found
                                else:
                                    print(
                                        "Job title does not exist in the database.")

                        sel = ""  # resetting

                    # Jobs Not Yet Applied For
                    elif sel == "4":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                        # expand
                        # option to save / apply
                        print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                        flag2 = True
                        while flag2 is True:
                            print("   +-----------------------------+")
                            print("   |  Jobs: Not Yet Applied For  | ")
                            print("+-----------------------------------+")
                            print("|      Job Titles Listed Below      |")
                            print("+-----------------------------------+")
                            for jobs in db.data["Jobs"]:
                                theFlag = True
                                for vals in jobs['users_applied']:
                                    # if the user saved the job
                                    # means user has already applied
                                    if vals['username'] == theStudent.username:
                                        theFlag = False
                                if theFlag:
                                    print("|----> ", jobs['title'])

                            print("+----------------------------------+")
                            print("| To see more about a specific job,|")
                            print("| type out the Job Title below;    |")
                            print("| or type x to go back.            |")
                            print("+----------------------------------+")
                            jobTitle = input("Type Here: ")

                            # If user doesn't enter
                            if jobTitle == "x":
                                flag2 = False
                            else:
                                # displays info, return true if job is real false if not found
                                isFound = accnt.display_job_info(db, jobTitle)
                                if isFound:
                                    print("+-----------------------------+")
                                    print("|1. Apply for the job         |")
                                    print("|2. Save the job for later    |")
                                    print("|x. Niether                   |")
                                    print("+-----------------------------+")

                                    sel = input("Make a selection: ")

                                    # Apply for job
                                    if sel == "1":
                                        # returns true if applied successfully, false otherwise
                                        hasApplied = accnt.apply_for_job(
                                            db, jobTitle, theStudent.username)

                                        if hasApplied is True:
                                            print("Successfully Applied!")
                                        else:
                                            print("Application Error")

                                    # Save Job
                                    elif sel == "2":
                                        # returns true if saved succesfully, false otherwise
                                        hasSaved = accnt.save_job(
                                            db, jobTitle, theStudent.username)

                                        if hasSaved:
                                            print("Successfully Saved!")
                                        else:
                                            print("Error saving job...")
                                # Job was not found
                                else:
                                    print(
                                        "Job title does not exist in the database.")

                        sel = ""  # resetting

                    # Saved Jobs
                    elif sel == "5":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                        # expand
                        # option to apply for the job
                        print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                        flag2 = True
                        while flag2 is True:
                            print("          +---------------+")
                            print("          |  Jobs Saved  |         ")
                            print("+---------------------------------------+")
                            print("|     Saved Job Titles Listed Below     |")
                            print("+---------------------------------------+")
                            for jobs in db.data["Jobs"]:
                                for val in jobs['users_saved']:
                                    # if the user saved the job
                                    if val == theStudent.username:
                                        print("|----> ", jobs['title'])

                            print("+----------------------------------+")
                            print("| To see more about a saved job,   |")
                            print("| type out the Job Title below;    |")
                            print("| or type x to go back.            |")
                            print("+----------------------------------+")
                            jobTitle = input("Type Here: ")

                            # If user doesn't enter
                            if jobTitle == "x":
                                flag2 = False
                            else:
                                # displays info, return true if job is real false if not found
                                isFound = accnt.display_job_info(db, jobTitle)
                                if isFound:
                                    print("+-----------------------------+")
                                    print("|1. Apply for the job         |")
                                    print("|x. Continue without applying |")
                                    print("+-----------------------------+")

                                    sel = input("Make a selection: ")

                                    # Apply for job
                                    if sel == "1":
                                        # returns true if applied successfully, false otherwise
                                        hasApplied = accnt.apply_for_job(
                                            db, jobTitle, theStudent.username)

                                        if hasApplied is True:
                                            print("Successfully Applied!")
                                        else:
                                            print("Application Error")

                                    # Save Job

                                # Job was not found
                                else:
                                    print(
                                        "Job title does not exist in the database.")

                        sel = ""  # resetting

                    elif sel == "6":
                        print("          +---------------+")
                        print("          |  Job Listing  |         ")
                        print("+----------------------------------+")
                        print("|      Job Titles Listed Below     |")
                        print("+----------------------------------+")
                        for jobs in db.data["Jobs"]:
                            indication = ""
                            for vals in jobs['users_applied']:
                                # means user has already applied
                                if vals['username'] == theStudent.username:
                                    indication = "(Applied)"
                            print("|----> ", jobs['title'], indication)

                        print("+----------------------------------+")
                        print("| To see more about a specific job,|")
                        print("| type out the Job Title below;    |")
                        print("| or type x to go back.            |")
                        print("+----------------------------------+")
                        print("")
                        jobTitle = input(
                            "Please select a job to remove by inputting its full title: ")
                        accnt.remove_job(theStudent.username, jobTitle, db)

                    elif sel == 'x':
                        flag = False
                        print("... Going Back")
                        time.sleep(1)
                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                sel = ""  # resetting

            # Find someone you know
            elif sel == '2':
                db = database.Database()
                foundUser = db.search_users()
                if foundUser is True:
                    print("... User found in the inCollege System!")
                    time.sleep(1)

            # Learn a New Skill
            elif sel == '3':
                print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                flag = True
                while flag is True:
                    print("+--------------------+")
                    print("| Master a New Skill |")
                    print("+--------------------+")
                    print("+-------------------+")
                    print("|    1. Python      |")
                    print("|    2. Java        |")
                    print("|    3. C ++        |")
                    print("|    4. HTML        |")
                    print("|    5. Git         |")
                    print("|    x. Go Back     |")
                    print("+-------------------+\n")

                    sel = input("Make a selection: ")

                    if sel == "1":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    elif sel == "2":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    elif sel == "3":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    elif sel == "4":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    elif sel == "5":
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    elif sel == 'x':
                        flag = False
                        print("... Going Back")
                        time.sleep(1)
                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                sel = ""  # resetting

            elif sel == '4':
                # This will control the loop for Useul Links, when we want to exit the loop the flag will be flipped
                flag = True
                while flag is True:

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

                    # General
                    if sel == '1':
                        flag2 = True
                        while flag2 is True:

                            print("    + --------- +")
                            print("    |  GENERAL  |")
                            print(" +------------------+")
                            print(" | 1. Help Center   |")
                            print(" | 2. About         |")
                            print(" | 3. Press         |")
                            print(" | 4. Blog          |")
                            print(" | 5. Careers       |")
                            print(" | 6. Developers    |")
                            print(" | x. Go Back       |")
                            print(" +------------------+")

                            sel = input("\nEnter Your Selection: ")

                            if sel == "1":
                                print("\n                 + ----------- +")
                                print("                 | HELP CENTER |")
                                print(
                                    "+-------------------------------------------------+")
                                print(
                                    "|              Welcome to In College,             |")
                                print(
                                    "| the world's largest college student network     |")
                                print(
                                    "| with users in several countries and territories |")
                                print(
                                    "|                    World Wide                   |")
                                print(
                                    "+-------------------------------------------------+\n")
                            elif sel == "2":
                                print()
                                print("+========================+")
                                print("|*| Our About Goes Here |*|")
                                print("+========================+\n")

                            elif sel == "3":
                                print("\n+---------------------------+")
                                print("|  In College Pressroom:    |")
                                print("| Stay on top of the latest |")
                                print("| news, updates, and reports|")
                                print("+---------------------------+\n")

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

                            elif sel == "x":
                                flag2 = False
                                print("... Going Back")
                                time.sleep(1)

                            else:
                                print("...Invalid Input")
                                time.sleep(1)

                        sel = ""  # resetting sel

                    # Browse inCollege
                    elif sel == '2':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Business Solutions
                    elif sel == '3':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Directories
                    elif sel == '4':
                        print()
                        print("+========================+")
                        print("|*| Under Construction |*|")
                        print("+========================+\n")
                    # Go Back
                    elif sel == 'x':
                        flag = False
                        print("... Going Back")
                        time.sleep(1)

                    else:
                        print("...Invalid Input")
                        time.sleep(1)

                sel = ""  # resetting sel

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
                            targeted_advertising = "ON" if settings['guest control']['Targeted Advertising'] == True else "OFF"
                            SMS = "ON" if settings['guest control']['SMS'] == True else "OFF"
                            email = "ON" if settings['guest control']['Email'] == True else "OFF"
                            # the Menu is Aligned 
                            print("+------------------------------+")
                            print("|    Current Guest Controls:   |")
                            print(f"| Email:       {email}              |")
                            print(f"| SMS:         {SMS}              |")
                            print(f"| Advertising: {targeted_advertising}              |")
                            print("+------------------------------+")
                            print("|     Edit Guest Controls?     |")
                            print("+------------------------------+")
                            print("| 1. Yes                       |")
                            print("| x. Go Back                   |")
                            print("+------------------------------+")
                            sel = input("Enter Your Selection: ")

                            if sel == "1":
                                # print("Editing Guest Controls")
                                guest_control_flag = True
                                while guest_control_flag:
                                    print("+-----------------------------------+")
                                    print("|    Choose Which Guest Control     |")
                                    print("+-----------------------------------+")
                                    print("| 1. Email                          |")
                                    print("| 2. SMS                            |")
                                    print("| 3. Advertising                    |")
                                    print("| x. Go Back                        |")
                                    print("+-----------------------------------+")
                                    selection = input("Enter Your Selection: ")
                                    guest_control_field = ""
                                    if selection == 'x':
                                        guest_control_flag = False
                                        print("... Going Back")
                                        time.sleep(1)
                                        break
                                    elif selection == '1':
                                        guest_control_field = 'Email'
                                    
                                    elif selection == '2':
                                        guest_control_field = 'SMS'
                                        
                                    elif selection == '3':
                                        guest_control_field = 'Targeted Advertising'

                                    else:
                                        print("...Invalid Input")
                                        time.sleep(1)
                                        continue
                                    value_update_flag = True
                                    while value_update_flag:
                                        print("+------------------------------------+")
                                        print("|   Choose New Guest Control Value   |")
                                        print("+------------------------------------+")
                                        print("| 1. ON                              |")
                                        print("| 2. OFF                             |")
                                        print("| x. Go Back                         |")
                                        print("+------------------------------------+")
                                        new_selected_value = input("Enter Your Selection: ")
                                        new_value = True
                                        if new_selected_value == 'x':
                                            value_update_flag = False
                                            print("... Going Back")
                                            time.sleep(1)
                                            break
                                        elif new_selected_value != '1' and new_selected_value != '2':
                                            print("...Invalid Input")
                                            time.sleep(1)
                                            continue
                                        elif new_selected_value == '1':
                                            new_value = True
                                            # db.update_student(theStudent.username, 'settings', True, 'guest control', guest_control_field)
                                        elif new_selected_value == '2':
                                            # db.update_student(theStudent.username, 'settings', False, 'guest control', guest_control_field)
                                            new_value = False
                                        # Get shallow copy of current settings
                                        new_settings = settings.copy()
                                        # Get new guest controls 
                                        new_guest_control = new_settings['guest control']
                                        # Update new guest controls
                                        new_guest_control[guest_control_field] = new_value
                                        # Update new settings
                                        new_settings['guest control'] = new_guest_control
                                        # Update user object
                                        theStudent.update(settings=new_settings)
                                        # Update Student in DB
                                        db.set_student(theStudent)
                                        # Update Stundet Object
                                        theStudent = db.get_student_by_username(theStudent.username)
                                        # Update settings
                                        settings = theStudent.settings
                                        # Update Global Setings 
                                        # print(settings)
                                        # set flags to false
                                        value_update_flag = False
                                        guest_control_flag = False

                                    
                            elif sel == "x":
                                flag2 = False
                                print("... Going Back")
                                time.sleep(1)

                            else:
                                print("... Invalid Input")
                                time.sleep(1)

                        sel = ""  # resetting

                    elif sel == "6":
                        print("Our Cookie Policy goes here")

                    elif sel == "7":
                        print("Our Brand Policy goes here")

                    elif sel == "8":
                        flag2 = True
                        while flag2 is True:
                            language = settings['language']
                            print("+--------------------------------+")
                            print("|   Current Language Setting:    |")
                            print("+--------------------------------+")
                            print(f"| Language:         {language}      |")
                            print("+--------------------------------+")
                            print("| Edit Language Settings?        |")
                            print("+--------------------------------+")
                            print("| 1. Yes                         |")
                            print("| x. Go Back                     |")
                            print("+--------------------------------+\n")
                            sel = input("Enter Your Selection: ")

                            if sel == "1":
                                language_update_flag = True
                                while language_update_flag:
                                    print("+---------------------------------+")
                                    print("|   Choose New Language Option    |")
                                    print("+---------------------------------+")
                                    print("| 1. English                      |")
                                    print("| 2. Spanish                      |")
                                    print("| x. Go Back                      |")
                                    print("+---------------------------------+")
                                    new_language_selection = input("Enter Your Selection: ")
                                    if new_language_selection == 'x':
                                        print("... Going Back")
                                        time.sleep(1)
                                        break
                                    elif new_language_selection == '1':
                                        new_language = 'English'
                                        # db.update_student(theStudent.username, 'settings', 'English', 'language')
                                    elif new_language_selection == '2':
                                        new_language = 'Spanish'
                                        # db.update_student(theStudent.username, 'settings', 'Spanish', 'language')
                                    else:
                                        print("... Invalid Input")
                                        time.sleep(1)
                                        continue
                                    # Get shallow copy of current settings
                                    new_settings = settings.copy()
                                    # Update new settings
                                    new_settings['language'] = new_language
                                    # Update Student Object
                                    theStudent.update(settings=new_settings)
                                    # Update Student in DB
                                    db.set_student(theStudent)
                                    # Update Stundet Object
                                    theStudent = db.get_student_by_username(theStudent.username)
                                    # Update settings
                                    settings = theStudent.settings
                                    # updated_user = user.User(theUser.username)
                                    # Update Global Setings 
                                    language_update_flag = False
                            elif sel == "x":
                                flag2 = False
                                print("... Going Back\n")
                                time.sleep(1)
                            else:
                                print("... Invalid Input")
                                time.sleep(1)
                                continue

                        sel = ""  # resetting sel

                    elif sel == "x":
                        flag = False
                        print("... Going Back\n")
                        time.sleep(1)

                    else:
                        print("...Invalid Input")
                        time.sleep(1)
                sel = "" #resetting
            elif sel == "6":
                # loop while 
                accnt.display_profile(theStudent)

                while accnt.edit_profile_menu(theStudent):
                    accnt.display_profile(theStudent)
                    pass
                
            elif sel == "7":
                while accnt.diplay_friend_list(theStudent):
                    pass

            elif sel == "8":
                print("          + ------------ +")
                print("          | FIND FRIENDS |         ")
                print(" +----------------------------------+")
                print(" | Search For friends by            |")
                print(" | last name, university, or major  |")
                print(" +----------------------------------+")
                #search DB for student by various fields (calls search_by_field)
                #check if student is not already in friend list
                #call add student request
                #display success or fail message
                # db = database.Database()
                foundFriend = accnt.send_friend_request_menu(db,theStudent)
                if foundFriend is True:
                    print("... User found in the inCollege System!")
                    time.sleep(1)

            # Messaging
            elif sel == "9":
                print("\n|*| NOTE - Enter 'x' at any time to go back |*|\n")
                flag = True
                while flag is True:
                    print("          +-------------+")
                    print("          |  Messaging  |         ")
                    print(" +------------------------------+")
                    print(" | 1. Send Message              |")
                    print(" | 2. Inbox                     |")
                    print(" | x. Go Back                   |")
                    print(" +------------------------------+")

                    sel = input("Make a selection: ")

                    # Send Message
                    if sel == '1':
                        if theStudent.status == True:
                            accnt.diplay_sendMessage_list_plus(db, theStudent)
                        else:
                            accnt.diplay_sendMessage_list(db, theStudent)

                    # Inbox
                    elif sel == "2":      
                        while accnt.diplay_inbox(theStudent, db):
                            pass
                    elif sel == 'x':
                        flag = False
                        print("... Going Back")
                        time.sleep(1)
                    else:
                        print("...Invalid Input")
                        time.sleep(1)

                sel = ""  # resetting

            elif sel == 'x':
                print("       + --------- +")
                print("       | Good Bye! |")
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


if __name__ == '__main__':
    main()
