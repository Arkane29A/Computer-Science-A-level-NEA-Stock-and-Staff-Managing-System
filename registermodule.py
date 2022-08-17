import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random
import sqlite3

conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
scursor = conn.cursor()

scursor.execute("""SELECT scode FROM UserInfo""")

userscode = scursor.fetchone()
userscode = str(userscode)
userscode = userscode[1:-1]
userscode = userscode.replace(",", "")
userscode = userscode.replace("'", "")

conn.close()


def registerempty():
    checks = [] #this array is used to allow the user to show and hide their password in the password box

    #This function generates a random 4 digit security code
    def generate():
        global scode
        code = [] #Array created
        for x in range(0,4):
            code.append(random.randint(0,9)) #Randomly generates 4 digits and adds them to the array

        code = str(code)[1:-1] #Removes brackets

        scode = code.replace(",", "")
        scode = scode.replace(" ", "") #Removes commas and whitespace

        scodeoutput = Label(registerroot, text=scode, bg="white", font=('helvetica', 20, 'bold'))
        scodeoutput.place(x=120, y=212)
        #Makes final code displayable on screen within the canvas

        print(scode)



    def registration():
        conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
        scursor = conn.cursor()

        #This code will store the contents into the database

        Uname = UnameInput.get()
        Upass = UpassInput.get()

        # scursor.execute('INSERT INTO UserInfo (Username) VALUES (?)', [Uname])
        # scursor.execute('INSERT INTO UserInfo (Password) VALUES (?)', [Upass])
        # scursor.execute('INSERT INTO UserInfo (scode) VALUES (?)', [scode])

        #Username, password and SCODE is updated to the database
        
        scursor.execute('UPDATE UserInfo SET Username=? WHERE Identifier = "ID1" ', [Uname])
        scursor.execute('UPDATE UserInfo SET Password=? WHERE Identifier = "ID1" ', [Upass])
        scursor.execute('UPDATE UserInfo SET SCODE=? WHERE Identifier = "ID1" ', [scode])

        conn.commit()
        conn.close()


        #This section of the code empties the text boxes and covers up the old code
        UnameInput.delete(0, END)
        UpassInput.delete(0, END)
        covercanvas = Canvas(registerroot, width=70, height=32, bg="white", highlightthickness = 0)
        covercanvas.place(x=120, y=212)

        messagebox.showinfo("Confirm", "Registration Successful") #Output message
        registerroot.destroy()

    def show():
        #this module allows the user to show and hide their password

        codelength = len(checks)
        if codelength % 2 ==0:
            UpassInput.config(show="")
            checks.append("a")
        else:
            UpassInput.config(show="*")
            checks.append("a")





    registerroot = Tk()

    # This is the section of code which creates the main window
    registerroot.geometry('365x392')
    registerroot.configure(background='#00B2EE')
    registerroot.title('Register')


    # This is the section of code which creates the label
    Label(registerroot, text='Register profile below', bg='#00B2EE', font=('helvetica', 12, 'bold')).place(x=92, y=47)


    # This is the section of code which creates text input box
    UnameInput=Entry(registerroot, width=30)
    UnameInput.place(x=93, y=118)
    UpassInput=Entry(registerroot, width=30, show="*")
    UpassInput.place(x=93, y=159)


    # This is the section of code which creates labels
    Label(registerroot, text='User:', bg='#00B2EE', font=('helvetica', 8, 'italic bold')).place(x=30, y=119)
    Label(registerroot, text='Pass:', bg='#00B2EE', font=('helvetica', 8, 'italic bold')).place(x=30, y=164)


    # This is the section of code which creates the 'generate' button
    gen = Button(registerroot, text='Generate', bg='#00B2EE', font=('helvetica', 10, 'italic'), command=generate)
    gen.place(x=240, y=215)

    # this code creates a canvas for the generated code to be inputted to
    gencanvas = Canvas(registerroot, width=120, height=60, bg="white")
    gencanvas.place(x=93, y=198)

    #Creates the 'Confirm Registration' button
    creg = Button(registerroot, text="Confirm Registration", bg="#00B2EE", font=("helvetica", 10, "bold"), command=registration)
    creg.place(x=93, y=290)

    bshow = Button(registerroot, text="Show", relief=FLAT, bg='#00B2EE', command=show)
    bshow.place(x=290, y=158)

    registerroot.mainloop()








def register():
    print(userscode)



    def accountoptions():



        def Cuser():
            
            def updatedata():
                conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
                scursor = conn.cursor()
                updateusername = newuser.get()
                scursor.execute('UPDATE UserInfo SET Username=?', [updateusername])




                
                conn.commit()
                conn.close()

                messagebox.showinfo("Confirmed", "Username Update Successful.", parent=root4)
                root4.destroy()

            root4 = Tk()
            root4.geometry('436x151')
            root4.configure(background='#7EC0EE')
            root4.title('Change Username')


            # This is the section of code which creates the a label
            Label(root4, text='Change Username Below:', bg='#7EC0EE', font=('arial', 12, 'bold')).place(x=26, y=19)


            # This is the section of code which creates a text input box
            newuser=Entry(root4)
            newuser.place(x=28, y=62)


            # This is the section of code which creates a button
            Button(root4, text='Submit', bg='#7EC0EE', font=('arial', 12, 'bold'), command=updatedata).place(x=29, y=97)


            root4.mainloop()

        def Cpass():
            def updatedata():
                conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
                scursor = conn.cursor()
                updatepassword = newpass.get()

                scursor.execute('UPDATE UserInfo SET Password=?', [updatepassword])
                conn.commit()



                conn.close()

                messagebox.showinfo("Confirmed", "Password Update Successful.", parent=root5)
                root5.destroy()

            root5 = Tk()
            root5.geometry('436x151')
            root5.configure(background='#7EC0EE')
            root5.title('Change Password')


            # This is the section of code which creates the a label
            Label(root5, text='Change Password Below:', bg='#7EC0EE', font=('arial', 12, 'bold')).place(x=26, y=19)


            # This is the section of code which creates a text input box
            newpass=Entry(root5)
            newpass.place(x=28, y=62)


            # This is the section of code which creates a button
            Button(root5, text='Submit', bg='#7EC0EE', font=('arial', 12, 'bold'), command=updatedata).place(x=29, y=97)


            root5.mainloop()

        def resetprofile():
            conn = sqlite3.connect("SoftwareData.db") # This creates a connection with our local database
            scursor = conn.cursor()

            reset = messagebox.askyesno("Warning", "Are you sure? All Data will be lost")
            if reset == True:
                scursor.execute("""DELETE FROM UserInfo""")
                conn.commit()
                temp = "ID1"
                scursor.execute('INSERT INTO UserInfo (Identifier) VALUES (?)', [temp])
                conn.commit()
                conn.close()
                messagebox.showinfo("Successful", "Account deleted")

            else:
                pass

        root2.destroy()
        root3 = Tk()
        root3.geometry('367x422')
        root3.configure(background='#6CA6CD')
        root3.title('Account Options')

        #This code below creates three buttons for the user to interact with, which each open their own defined modules and GUIS

        Label(root3, text='Please look below for further options:', bg='#6CA6CD', font=('helvetica', 12, 'bold')).place(x=49, y=22)

        b1 = Button(root3, text='Change Username', bg='#6CA6CD', font=('helvetica', 15, 'bold'), command=Cuser, width=20)
        b1.place(x=65, y=77)

        b2 = Button(root3, text='Change Password', bg='#6CA6CD', font=('helvetica', 15, 'bold'), command=Cpass, width=20)
        b2.place(x=65, y=179)

        b3 = Button(root3, text='Reset Profile', bg='#6CA6CD', font=('helvetica', 15, 'bold'), command=resetprofile, width=20)
        b3.place(x=65, y=276)

        root3.mainloop()




    def scodeconfirm():
        scode = scodecheck.get() #Gets user inputted information from entry widget

        if len(scode) >4: #lengthcheck, if it goes above 4 characters, it is denied.
            messagebox.showinfo("Error", "Please input a 4 digit security code")
            scodecheck.delete(0,END)
        else:
            if scode == userscode: #if scode equals usercode, then the accountoptions() module is ran
                messagebox.showinfo("Success", "Access Granted")
                scodecheck.delete(0, END)
                accountoptions()
            else:
                messagebox.showinfo("Error", "Incorrect Code") #if incorrect, user is denied, entry box is cleared.
                scodecheck.delete(0, END)



    root2 = Tk()

    # This is the section of code which creates the main window
    root2.geometry('365x392')
    root2.configure(background='#00B2EE')
    root2.title('Register')
    root2.resizable(False, False)


    Label(text="For further actions, please input your 6-", bg='#00B2EE', font=('Helvetica', 10, 'bold')).place(x=60, y=20) #Creates the main label
    Label(text="digit security code", bg='#00B2EE', font=('Helvetica', 10, 'bold')).place(x=120, y=50)

    scodecheck = Entry(root2, font=('Helvetica', 30)) #Creates the entry used to check the security code from the database
    scodecheck.place(x=118, y=90, width=120, height=90)



    b1 = Button(root2, text="Submit", font=('helvetica', 10, 'bold'), command=scodeconfirm)
    b1.place(x=148, y=200)

    root2.mainloop()


