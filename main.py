import tkinter
from tkinter import *
from tkinter import messagebox
from captcha.image import *
import mysql.connector
import random
from PIL import Image, ImageTk


mydb = mysql.connector.connect(
 host='localhost',
 user="root",
 passwd="password@mysql",
 auth_plugin="mysql_native_password",
 database="login_authenticator"
)
mycursor = mydb.cursor()


def createCapcha():
    secretInt = random.randint(1000, 9999)
    secret = ImageCaptcha(width=200, height=60)
    secretText = str(secretInt)
    source = secret.generate(secretText)
    secret.write(secretText, 'captcha1.png')
    return secretText


#returns everything back the main menu page
def returnToMainMenu(master):
 master.destroy()
 mainMenu()


#Used for encrypting the password at the time of singing up
def ceasarEncrypt(text, shift):
 output = ""
 for c in text:
     output = output + (chr(ord(c) + shift))
 return output


#Used for entering the new user details in the database
def newUser(master, email, name, password, confPassword, securityQuestion, enteredCaptcha, realCaptcha):
 if(email == "" or name == "" or password == "" or securityQuestion== "" or enteredCaptcha == ""):
     messagebox.showinfo("Failure :(", "Message: One or more fields are empty")
 else:
         existingEmail = ""
         try:
             sql = "SELECT * FROM login_authenticator.user_data WHERE email = %s"
             mycursor.execute(sql, (email,))
             myresult = mycursor.fetchall()
             existingEmail = myresult[0][0]
         except:
             print("")
         if(existingEmail != email):
             if(password == confPassword):
                 if(realCaptcha == enteredCaptcha):
                       try:
                         sqlFormula = "INSERT INTO user_data (email, name, password, security_question) VALUES(%s, %s, %s, %s)"
                         encryptedPassword = ceasarEncrypt(password, 3)
                         user1 = (email, name, encryptedPassword, securityQuestion)
                         mycursor.execute(sqlFormula, user1)
                         mydb.commit()
                         messagebox.showinfo("Success!", "User data saved successfully!")
                         returnToMainMenu(master)
                       except:
                         messagebox.showinfo("Failure :(","Message: Username already exists!! please try logging in instead!")
                         returnToMainMenu(master)
                 else:
                     messagebox.showinfo("Failure :(", "Captcha does not match!")
             else:
                 messagebox.showinfo("Failure :(", "Passwords do not match!")
         else:
             messagebox.showinfo("Failure :(","Message: Email already exists!! please try logging in instead!")


#Used for deleting user information from the database
def deleteUser(master, searchEmail, enteredPassword, enteredPrompt, enteredCaptcha, realCaptcha):
 if (searchEmail == "" or enteredPassword == "" or enteredPrompt == "" or enteredCaptcha == ""):
    messagebox.showinfo("Failure :(", "Message: One or more fields are empty")
 else:
    if(enteredPrompt == "CONFIRM"):
        if(enteredCaptcha == realCaptcha):
            try:
               sql = "SELECT * FROM login_authenticator.user_data WHERE email = %s"
               mycursor.execute(sql, (searchEmail,))
               myresult = mycursor.fetchall()
               decryptedPassword = ceasarDecrypt(myresult[0][2], 3)
               if (enteredPassword == decryptedPassword):
                   sqlFormula = "DELETE FROM user_data WHERE Email = %s"
                   mycursor.execute(sqlFormula, (searchEmail,))
                   mydb.commit()
                   messagebox.showinfo("Success!", "Your account has been deleted successfully!")
                   returnToMainMenu(master)
               else:
                   messagebox.showinfo("Failure :(","Invalid Password.\nTry again!")
            except:
               messagebox.showinfo("Failure :(", "Email does not exist.")
        else:
            messagebox.showinfo("Failure :(", "Captcha does not match!")
    else:
        messagebox.showinfo("Failure :(", "Incorrect Prompt.\nPlease enter the prompt correctly.")


#Used for Decrypting the password at the time of loging in
def ceasarDecrypt(text, shift):
 output = ""
 for c in text:
    output = output + (chr(ord(c) - shift))
 return output


#Compares the serverside password and the password entered by the user at the time of login
def fetchPassword(master, searchEmail, enteredPassword):
 if (searchEmail == "" or enteredPassword == ""):
    messagebox.showinfo("Failure :(", "Message: One or more fields are empty")

 else:
    try:
       sql = "SELECT * FROM login_authenticator.user_data WHERE email = %s"
       mycursor.execute(sql, (searchEmail,))
       myresult = mycursor.fetchall()
       decryptedPassword = ceasarDecrypt(myresult[0][2], 3)
       if (enteredPassword == decryptedPassword):
           messagebox.showinfo("Success!", "The entered details and the details on the server match!\nLogin Successful!")
       else:
           messagebox.showinfo("Failure :(","Invalid Password.\nLogin Unsuccessful!")
    except:
       messagebox.showinfo("Failure :(", "Email does not exist.")
    returnToMainMenu(master)


#Used for updating the password in the database at the time of forgot password
def updatePassword(master, searchEmailForReset, enteredAnswer, newPassword, confNewPassword, enteredCaptcha, realCaptcha):
 if (searchEmailForReset == "" or enteredAnswer == "" or newPassword == "" or enteredCaptcha == ""):
    messagebox.showinfo("Failure :(", "Message: One or more fields are empty")
 else:
    if(realCaptcha == enteredCaptcha):
        if(newPassword == confNewPassword):
            try:
               sql = "SELECT * FROM login_authenticator.user_data WHERE email = %s"
               mycursor.execute(sql, (searchEmailForReset,))
               myresult = mycursor.fetchall()
               serverSideAnswer = myresult[0][3]
               newEncryptedPassword = ceasarEncrypt(newPassword, 3)
               if (enteredAnswer == serverSideAnswer):
                   sql = "UPDATE user_data SET password = %s WHERE email = %s"
                   mycursor.execute(sql, (newEncryptedPassword, searchEmailForReset,))
                   mydb.commit()
                   messagebox.showinfo("Success!", "The password had been updated successfully!")
               else:
                   messagebox.showinfo("Failure :(","Please validate your answer and try again!")
            except:
               messagebox.showinfo("Failure :(", "Email does not exist.")
            returnToMainMenu(master)
        else:
            messagebox.showinfo("Failure :(", "Passwords do not match!")
    else:
        messagebox.showinfo("Failure :(", "Captcha does not match!")


#Used for verifying the user's security answer (for forgot password)
def checkAnswer(master, searchEmailForReset, enteredAnswer):
 if (searchEmailForReset == "" or enteredAnswer == ""):
    messagebox.showinfo("Failure :(", "Message: One or more fields are empty")

 else:
    try:
       sql = "SELECT * FROM login_authenticator.user_data WHERE email = %s"
       mycursor.execute(sql, (searchEmailForReset,))
       myresult = mycursor.fetchall()
       serverSideAnswer = myresult[0][3]
       if (enteredAnswer == serverSideAnswer):
           messagebox.showinfo("Success!", "The entered security answer and the security answer on the server match! Click OK to proceed!!")
       else:
           messagebox.showinfo("Failure :(","The entered security answer and the answer on the server match do not match. try again!")
    except:
       messagebox.showinfo("Failure :(", "Email does not exist.")


#Gui for the forgot password page (Calls the updatePassword and the checkAnswer function)
def forgotPassword(master):
 master.destroy()
 realCaptcha = createCapcha()
 fpwn = Tk()
 fpwn.geometry("850x630")
 fpwn.title("Forgot Password")
 fpwn.configure(bg="lightsteelblue1", cursor="icon")
 fr1 = Frame(fpwn)
 l_title = Message(fpwn, text="Forgot Password", width=1500, padx=500, pady=45, justify="center",
                   anchor="center", background='azure1')
 l_title.config(font=("Book Antiqua", "42"))
 l_title.pack(side="top")
 l1 = Label(fpwn, text="Enter Email: ", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold") )
 l1.place(x=95, y=165)
 e1 = Entry(fpwn, width = 50, bd = 7, cursor="icon",)
 e1.place(x=50, y=220)
 l2 = Label(fpwn, text="Enter security answer: ", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l2.place(x=555, y=165)
 l7 = Label(fpwn, text="Where were you born?", bg='lightsteelblue1',
            font=("Book Antiqua", "8", "bold"))
 l7.place(x=598, y=196)
 e2 = Entry(fpwn, width = 50, bd = 5, cursor="icon",)
 e2.place(x=500, y=220)
 l6 = Label(fpwn, text="Please enter your email and security answer and click 'validate' to proceed.", bg='lightsteelblue1', width=70,
            font=("Book Antiqua", "11", "bold"))
 l6.place(x=80, y=260)
 validate = Button(fpwn, text="Validate Answer",
            command= lambda: checkAnswer(fpwn, e1.get().strip(), e2.get().strip()),
            width=15, height=2,  font=("Book Antiqua","11", "bold"), activebackground="skyblue",
            bg="deepskyblue2", cursor="icon",bd = 2 ).place(x=360, y=300)

 fpwn.bind("<Return>", lambda x: checkAnswer(fpwn, e1.get().strip(), e2.get().strip(),))
 l3 = Label(fpwn, text="Enter new Password:", bg='lightsteelblue1', height=2, width=20,font=("Book Antiqua","11", "bold"))
 l3.place(x=100, y=350)
 e3 = Entry(fpwn, width= 50, bd = 5, cursor="icon", show="*")
 e3.place(x=50, y=400)
 l4 = Label(fpwn, text="Confirm password:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua", "11", "bold"))
 l4.place(x=95, y=435)
 e4 = Entry(fpwn, width=50, bd=5, cursor="icon", show="*")
 e4.place(x=50, y=485)

 image1 = Image.open("captcha1.png")
 test = ImageTk.PhotoImage(image1)
 label1 = tkinter.Label(image=test)
 label1.image = test
 label1.place(x=550, y=375)

 l5 = Label(fpwn, text="Enter Captcha:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l5.place(x=550, y=435)
 e5 = Entry(fpwn, width= 50, bd = 5, cursor="icon",)
 e5.place(x=500, y=485)

 next = Button(fpwn, text="Next >",
            command= lambda: updatePassword(fpwn, e1.get().strip(), e2.get().strip(), e3.get().strip(), e4.get().strip(), e5.get().strip(), realCaptcha),
            width=15, height=2,  font=("Book Antiqua","11", "bold"), activebackground="palegreen3",
            bg="palegreen1", cursor="icon",bd = 2 ).place(x=640, y=550)
 fpwn.bind("<Return>", lambda x: updatePassword(fpwn, e1.get().strip(), e2.get().strip(),  e3.get().strip(), e4.get().strip(), e5.get().strip(), realCaptcha))

 back = Button(fpwn, text ="< Back", command = lambda: loginMenu(fpwn), width=15, height=2,  font=("Book Antiqua","11", "bold"),
               activebackground="coral3", bg="coral1", cursor="icon",bd = 2 ).place(x=50, y=550)
 return



def deleteUserMenu(master):
    master.destroy()
    realCaptcha = createCapcha()
    duwn = Tk()
    duwn.geometry("850x630")
    duwn.title("Delete User Menu")
    duwn.configure(bg="lightsteelblue1", cursor="icon")
    fr1 = Frame(duwn)
    l_title = Message(duwn, text="Delete User", width=1500, padx=500, pady=45, justify="center",
                      anchor="center", background='azure1')
    l_title.config(font=("Book Antiqua", "42"))
    l_title.pack(side="top")
    l1 = Label(duwn, text="Enter Email: ", bg='lightsteelblue1', height=2, width=20,
               font=("Book Antiqua", "13", "bold"))
    l1.place(x=90, y=195)
    e1 = Entry(duwn, width=50, bd=5, cursor="icon", )
    e1.place(x=50, y=245)
    l2 = Label(duwn, text="Enter Password:", bg='lightsteelblue1', height=2, width=20,
               font=("Book Antiqua", "13", "bold"))
    l2.place(x=90, y=295)
    e2 = Entry(duwn, width=50, bd=5, cursor="icon", show="*")
    e2.place(x=50, y=345)
    l3 = Label(duwn, text="Enter 'CONFIRM' to proceed:", bg='lightsteelblue1', height=2, width=20,
               font=("Book Antiqua", "13", "bold"))
    l3.place(x=90, y=395)
    e3 = Entry(duwn, width=50, bd=5, cursor="icon")
    e3.place(x=50, y=445)

    image1 = Image.open("captcha1.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=530, y=320)

    l4 = Label(duwn, text="Enter Captcha:", bg='lightsteelblue1', height=2, width=20,
               font=("Book Antiqua", "11", "bold"))
    l4.place(x=535, y=395)
    e4 = Entry(duwn, width=50, bd=5, cursor="icon", )
    e4.place(x=483, y=445)

    submit = Button(duwn, text="Submit >",
                    command=lambda: deleteUser(duwn, e1.get().strip(), e2.get().strip(), e3.get().strip(),
                                               e4.get().strip(), realCaptcha),
                    width=15, height=2, font=("Book Antiqua", "13", "bold"), activebackground="palegreen3",
                    bg="palegreen1", cursor="icon", bd=2).place(x=620, y=550)
    duwn.bind("<Return>",
              lambda x: deleteUser(duwn, e1.get().strip(), e2.get().strip(), e3.get().strip(), e4.get().strip(),
                                   realCaptcha))

    back = Button(duwn, text="< Main Menu", command=lambda: returnToMainMenu(duwn), width=15, height=2,
                  font=("Book Antiqua", "13", "bold"),
                  activebackground="coral3", bg="coral1", cursor="icon", bd=2).place(x=50, y=550)
    return


#GUI for the login page (calls the fetchPassword function and the forgotPassword funtion)
def loginMenu(master):
 master.destroy()
 loginwn = Tk()
 loginwn.geometry("850x630")
 loginwn.title("Login Menu")
 loginwn.configure(bg="lightsteelblue1", cursor="icon")
 fr1 = Frame(loginwn)
 l_title = Message(loginwn, text="Login", width=1500, padx=500, pady=45, justify="center",
                   anchor="center", background='azure1')
 l_title.config(font=("Book Antiqua", "42"))
 l_title.pack(side="top")
 l1 = Label(loginwn, text="Enter Email: ", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","13", "bold") )
 l1.pack(side="top")
 e1 = Entry(loginwn, width = 50, bd = 5, cursor="icon",)
 e1.pack(side="top")
 l2 = Label(loginwn, text="Enter Password:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua", "13", "bold"))
 l2.pack(side="top")
 e2 = Entry(loginwn, width=50, bd=5, cursor="icon", show = "*")
 e2.pack(side="top")

 submit = Button(loginwn, text="Submit >",
            command= lambda: fetchPassword(loginwn, e1.get().strip(), e2.get().strip()),
            width=15, height=2,  font=("Book Antiqua","13", "bold"), activebackground="palegreen3",
            bg="palegreen1", cursor="icon",bd = 2 ).place(x=620, y=550)
 loginwn.bind("<Return>", lambda x: fetchPassword(loginwn, e1.get().strip(), e2.get().strip()))

 forgot = Button(loginwn, text="Forgot password", command=lambda: forgotPassword(loginwn), width=15, height=2,
               font=("Book Antiqua", "13", "bold"),
               activebackground="skyblue", bg="deepskyblue2", cursor="icon", bd=2).place(x=340, y=350)

 back = Button(loginwn, text ="< Main Menu", command = lambda: returnToMainMenu(loginwn), width=15, height=2,  font=("Book Antiqua","13", "bold"),
               activebackground="coral3", bg="coral1", cursor="icon",bd = 2 ).place(x=50, y=550)
 return


#GUI for the sign up page (calls the newUser funtion)
def createUser(master):
 master.destroy()
 realCaptcha =  createCapcha()
 crwn = Tk()
 crwn.geometry("850x630")
 crwn.title("Sign Up")
 crwn.configure(bg="lightsteelblue1", cursor="icon")
 fr1 = Frame(crwn)
 l_title = Message(crwn, text="Sign Up", width=1500, padx=500, pady=45, justify="center",
                   anchor="center", background='azure1')
 l_title.config(font=("Book Antiqua", "42"))
 l_title.pack(side="top")
 l1 = Label(crwn, text="Enter Email: ", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold") )
 l1.place(x=95, y=165)
 e1 = Entry(crwn, width = 50, bd = 5, cursor="icon",)
 e1.place(x=50, y=215)
 l2 = Label(crwn, text="Enter Name:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l2.place(x=95, y=250)
 e2 = Entry(crwn, width = 50, bd = 5, cursor="icon",)
 e2.place(x=50, y=300)
 l3 = Label(crwn, text="Enter desired Password:", bg='lightsteelblue1', height=2, width=20,font=("Book Antiqua","11", "bold"))
 l3.place(x=95, y=335)
 e3 = Entry(crwn, width= 50, bd = 5, cursor="icon", show="*")
 e3.place(x=50, y=385)
 l4 = Label(crwn, text="Confirm Password:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l4.place(x=95, y=410)
 e4 = Entry(crwn, width= 50, bd = 5, cursor="icon", show="*")
 e4.place(x=50, y=460)
 l5 = Label(crwn, text="Security Question: \n Where were you born?", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l5.place(x=555, y=165)
 e5 = Entry(crwn, width= 50, bd = 5, cursor="icon",)
 e5.place(x=500, y=215)

 image1 = Image.open("captcha1.png")
 test = ImageTk.PhotoImage(image1)
 label1 = tkinter.Label(image=test)
 label1.image = test
 label1.place(x=550, y=320)

 l6 = Label(crwn, text="Enter Captcha:", bg='lightsteelblue1', height=2, width=20, font=("Book Antiqua","11", "bold"))
 l6.place(x=550, y=410)
 e6 = Entry(crwn, width= 50, bd = 5, cursor="icon",)
 e6.place(x=500, y=460)

 submit = Button(crwn, text="Next >",
            command= lambda: newUser(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip(), e4.get().strip(), e5.get().strip(), e6.get().strip(), realCaptcha),
            width=15, height=2,  font=("Book Antiqua","11", "bold"), activebackground="palegreen3",
            bg="palegreen1", cursor="icon",bd = 2 ).place(x=640, y=550)
 crwn.bind("<Return>", lambda x: newUser(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip(), e4.get().strip(), e5.get().strip(), e6.get().strip(), realCaptcha))
 back = Button(crwn, text ="< Back", command = lambda: returnToMainMenu(crwn), width=15, height=2,  font=("Book Antiqua","11", "bold"),
               activebackground="coral3", bg="coral1", cursor="icon",bd = 2 ).place(x=50, y=550)
 return


#GUI for the main menu(calls the createUser funtion, login function and the exit funtion)
def mainMenu():
 rootwn = Tk()
 rootwn.geometry("850x630")
 rootwn.title("Login Authenticator")
 rootwn.configure(background='lightsteelblue1', cursor = "icon")
 fr1 = Frame(rootwn)
 fr1.pack(side="top")

 l_title = Message(text="Login Authenticator", width=1500, padx=500, pady=60, justify="center",
                   anchor="center", background='azure1')
 l_title.config(font=("Book Antiqua", "42"))
 l_title.pack(side="top")

 login_button = Button(rootwn, text="Login", command=lambda: loginMenu(rootwn), width=20, height=2, font=("Book Antiqua","13", "bold"), bd=2,
                       activebackground="Lightblue", bg="azure1", ).place(x=106, y=300)

 signup_button = Button(rootwn, text="Sign Up", command=lambda: createUser(rootwn), width=20, height=2, font=("Book Antiqua","13", "bold"), bd=2,
                        activebackground="Lightblue", bg="azure1", ).place(x=106, y=400)
 rootwn.bind("<Return>", lambda x: createUser(rootwn))

 delete_button = Button(rootwn, text="Delete Account", command=lambda: deleteUserMenu(rootwn), width=20, height=2, font=("Book Antiqua", "13", "bold"), bd=2,
                      activebackground="Lightblue", bg="azure1").place(x=509, y=300)

 exit_button = Button(rootwn, text="Exit", command= rootwn.destroy, width=20, height=2, font=("Book Antiqua","13", "bold"), bd=2,
                        activebackground="Lightblue", bg="azure1", cursor="x_cursor" ).place(x=509, y=400)
 rootwn.mainloop()


mainMenu()
