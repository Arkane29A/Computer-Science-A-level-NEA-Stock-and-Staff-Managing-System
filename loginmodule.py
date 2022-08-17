import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
from stockmanager import *
from registermodule import *

attempt = 3

def loginoverall():

    conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
    scursor = conn.cursor()

    #This whole section of code involves extracting the information from the database.

    scursor.execute("SELECT Username FROM UserInfo") #This extracts username from the database.
    conn.commit() #Commits database transaction
    Uname = scursor.fetchone()
    Uname = str(Uname) # Converted Tuple to String
    #This section of code removes any unneccessary punctuation from the string.
    Uname = Uname.replace("(", "")
    Uname = Uname.replace(")", "")
    Uname = Uname.replace("'", "")
    Uname = Uname.replace(",", "")

    scursor.execute("SELECT Password FROM UserInfo") #This extracts password from the database.
    conn.commit() #Commits database transaction
    Upass = scursor.fetchone()
    Upass = str(Upass) # Converted Tuple to String
    #This section of code removes any unneccessary punctuation from the string.
    Upass = Upass.replace("(", "")
    Upass = Upass.replace(")", "")
    Upass = Upass.replace("'", "")
    Upass = Upass.replace(",", "")


    scursor.execute("SELECT SCODE FROM UserInfo")
    lol = scursor.fetchone()

    scursor.execute("SELECT Identifier FROM UserInfo")
    lol2 = scursor.fetchone()

    print(Uname, Upass, lol, lol2)


    sclicks = []

    def registeropen():

        scursor.execute("""SELECT Username FROM UserInfo WHERE Identifier = 'ID1' """)
        uis1 = scursor.fetchone()
        uis1 = str(uis1)[1:-1]
        uis1 = uis1.replace(",","")

        if uis1 == "None":
            root.destroy
            registerempty()
        elif uis1 != "None":
            root.destroy()
            register()
      



    def show():
        licks = len(sclicks)

        if licks % 2 ==0: 
            UpassInput.config(show="")
            sclicks.append("1")
        else:
            UpassInput.config(show="*")
            sclicks.append("2")


    def quit():
        check = messagebox.askyesno("Warning", "Are you sure you wish to exit?")
        if check == 1:
            root.destroy()
        else:
            pass

    def login():

        global attempt  

        #First overall condition checks if the database is empty or not.
        if Uname == 'None' and Upass == 'None':
            messagebox.showinfo("Error", "Database empty, Please Register.")

        elif Uname != "None" and Upass == 'None':
            messagebox.showinfo("Error", "No password stored.")

        elif Uname == "None" and Upass != "None":
            messagebox.showinfo("Error", "No Username stored")

        else:
                
            uni = UnameInput.get() #Data Extracted from the username input box
            upi = UpassInput.get() #Data extracted from the password input box.
            uni = str(uni) #Type check
            upi = str(upi) #Type check
            lengthuni = len(uni) #Length of username
            lengthupi = len(upi) #length of password

            #This condition is used to check if the user has exceeded login attempts
            if attempt != 1: #If the login attempts haven't exceeded, code will continue.
                if lengthuni == 0:
                    print("Please enter your username")
                    messagebox.showinfo("Error", "Please enter your username")
                    
                        
                elif lengthupi ==0:
                    print("Please enter your password")
                    messagebox.showinfo("Error", "Please enter your password")
                    
                elif lengthuni == 0 and lengthupi == 0:
                    print("Please enter something")


                else:
                    #if both the username and password of the database match user input, program proceeds.
                    if uni ==  Uname and upi == Upass:
                        print("Authorised")
                        messagebox.showinfo("Granted", "Access Granted")
                        root.destroy()
                        conn.close()
                        stockmanager()
                    
                    #if username is correct but password isnt, error message displays and 1 is taken from attempts variable.
                    elif uni == Uname and upi != Upass:
                        print("Incorrect password")
                        messagebox.showinfo("Error", "Incorrect Password")
                        attempt -= 1
                        UnameInput.delete(0, END)
                        UpassInput.delete(0, END)
                        attemptlabel.config(text="Attempts remaining: " +  str(attempt), fg="black")

                    #if username amd password is incorrect, error message displays and 1 is taken from attempts variable.
                    elif uni != Uname and upi != Upass:
                        print("Incorrect Information")
                        messagebox.showinfo("Error", "Incorrect data")
                        attempt -= 1
                        UnameInput.delete(0, END)
                        UpassInput.delete(0, END)
                        attemptlabel.config(text="Attempts remaining: " +  str(attempt), fg="black")

                    #if incoherant data is entered which does not match the top conditions, the program will output the following error.
                    else:
                        print("Please try again")
                        messagebox.showinfo("Error", "Please try again.")

            elif attempt == 1: #If the attempts variable equals 1, then the program will exist.
                messagebox.showinfo("Error", "Maximum ammount of attempts exceeded")
                root.destroy()


    # This is the section of code which creates the main window

    root = Tk() #First, we create the window
    root.geometry('490x272') #Set Window Size
    root.configure(background='#FFFFFF') #Set background colour
    root.title('Login Page') #Sets window title
    root.resizable(False, False) #Prevents the window from being resized


    # This is the section of code which creates the main label
    Label(root, text='Please login below to gain access.', bg='#FFFFFF', font=('helvetica', 12, 'normal', "bold")).place(x=112, y=58)


    # This section creates the section for the user to input their username
    UnameInput=Entry(root, width=50, borderwidth=1.5) #Text Field created
    UnameInput.place(x=110, y=118) # Textfield is placed
    Label(root, text='User:', bg='#FFFFFF', font=('helvetica', 8, 'normal', "italic")).place(x=50, y=119) #User Label


    # This section creates the section for the user to input their password
    UpassInput=Entry(root, width=50, show="*", borderwidth=1.5) #textfield, show feature replaces the onscreen display with * 
    UpassInput.place(x=110, y=155) #Textfield is placed
    Label(root, text='Pass:', bg='#FFFFFF', font=('helvetica', 8, 'normal', "italic")).place(x=50, y=158) #Password Label



    attemptlabel = Label(root, text="" +  str(attempt), bg="#FFFFFF", fg="#FFFFFF")
    attemptlabel.place(x=10, y=240)



    #This section creates the submit button
    b1=Button(root, text='Submit', bg='#FFFFFF', font=('helvetica', 10, 'normal', "bold"), command=login) #Sets the command to the function login
    b1.place(x=360, y=197) #Button is placed

    #this section creates a 'show password' button

    b2 = Button(root, text="Show", bg='#FFFFFF', font=('helvetica', 6, 'italic'), command=show, relief= FLAT) #Sets the command to the function show
    b2.place(x=420, y=155) #Button is placed


    #This section creates an interactable menubar

    mbar = Menu(root) #Creating the menubar
    root.config(menu=mbar)

    filemenu = Menu(mbar, tearoff=False) #Creating drop down menu
    mbar.add_cascade(label="File", menu=filemenu) #Creating file option
    filemenu.add_command(label="Register", command=registeropen) #Creating Register Option
    filemenu.add_command(label="Exit", command=quit) #Creating Register Option




    root.mainloop()



    conn.close()
    
loginoverall()
