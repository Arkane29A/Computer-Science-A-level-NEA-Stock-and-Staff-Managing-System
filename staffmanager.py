from tkinter import *
import importlib
import sqlite3
import re
from tkinter import messagebox
from tkinter import ttk
from stockmanager import * 

def staffmanager():

    def editshift():

        def shift(event):

            def shiftedit(event):

                #gets all User submitted and stores them in database
                newval = change.get()
                check = item.get()
                dayget = daysdrop.get()

                if check == '9:30-11:30':
                    
                    #Stores in column T1
                    scursor.execute('UPDATE StaffInfo SET T1=? WHERE Day=?', [newval, dayget])
                    conn.commit()
                    messagebox.showinfo("Successful", "Updated")
                    conn.close()
                    editshiftroot.destroy()
                    staffmanager()

                elif check == '11:30-13:30':

                    #Stores in column T2

                    scursor.execute('UPDATE StaffInfo SET T2=? WHERE Day=?', [newval, dayget])
                    conn.commit()
                    messagebox.showinfo("Successful", "Updated")
                    conn.close()
                    editshiftroot.destroy()
                    staffmanager()
        

                elif check == '13:30-15:30':
                    #Stores in column T3

                    scursor.execute('UPDATE StaffInfo SET T3=? WHERE Day=?', [newval, dayget])
                    conn.commit()
                    messagebox.showinfo("Successful", "Updated")
                    conn.close()
                    editshiftroot.destroy()
                    staffmanager()
                
                elif check == '15:30-17:30':
                    #Stores in column T4

                    scursor.execute('UPDATE StaffInfo SET T4=? WHERE Day=?', [newval, dayget])
                    conn.commit()
                    messagebox.showinfo("Successful", "Updated")
                    conn.close()
                    editshiftroot.destroy()
                    staffmanager()

                if check == '17:30-19:30':
                    #Stores in column T5

                    scursor.execute('UPDATE StaffInfo SET T5=? WHERE Day=?', [newval, dayget])
                    conn.commit()
                    messagebox.showinfo("Successful", "Updated")
                    conn.close()
                    editshiftroot.destroy()
                    staffmanager()

            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #array containing all days
            daysdrop = ttk.Combobox(editshiftroot, values=days, width=45) #Creates drop down menu with days values in it
            daysdrop.place(x=30, y=100)

            change = Entry(editshiftroot, width=45) #Here we create the search entry box
            change.place(x=30, y=160)
            change.bind('<Return>', shiftedit) #binds to the next inbuilt subroutine





        output = ['9:30-11:30', '11:30-13:30', '13:30-15:30', '15:30-17:30', '17:30-19:30']
        editshiftroot = Tk()
        editshiftroot.title("Edit Shift")
        editshiftroot.geometry("350x300")
        editshiftroot.config(bg='#00B2EE')

        item = ttk.Combobox(editshiftroot, values=output, width=45)
        item.place(x=30, y=60)
        item.bind('<Return>', shift)
        Label(editshiftroot, text="Select Time below below", font=('Helvetica', 13, 'bold'), bg='#00B2EE').place(x=60, y=20)

        editshiftroot.mainloop()
        







    def editstaff():

        def staffmemberdelete(event):
            selection = item.get() #gets user selection
            final = "None" #Database final content

            #Replaces all of the fields where the member's name is 
            scursor.execute('UPDATE StaffInfo SET T1=? WHERE T1=?', [final, selection])
            conn.commit()
            scursor.execute('UPDATE StaffInfo SET T1=? WHERE T2=?', [final, selection])
            conn.commit()
            scursor.execute('UPDATE StaffInfo SET T1=? WHERE T3=?', [final, selection])
            conn.commit()
            scursor.execute('UPDATE StaffInfo SET T1=? WHERE T4=?', [final, selection])
            conn.commit()
            scursor.execute('UPDATE StaffInfo SET T1=? WHERE T5=?', [final, selection])
            conn.commit()

            #output message
            messagebox.showinfo("Successful", "Staff Deleted")


        output = []
        count = 0 #Variable used to count days
        scursor.execute("""SELECT * FROM StaffInfo""") # Selects all from staffinfo
        databasetotal = scursor.fetchall() #fetches
        databasetotal = ( ", ".join( repr(e) for e in databasetotal ) ) #removes square brackets


        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #array containing all days

        #while loop counts through each day, checking if they are in the variable before removing them

        while count != 7: 

            if days[count] in databasetotal:
                databasetotal = databasetotal.replace(days[count], "")
                count += 1
                print(databasetotal)
            else:

                count +=1

        databasetotal = databasetotal.replace("'", "")
        databasetotal = databasetotal.replace("(", "")
        databasetotal = databasetotal.replace(")", "")
        databasetotal = databasetotal.replace(",", "")


        databasetotal = databasetotal.split()

        output = [i for j, i in enumerate(databasetotal) if i not in databasetotal[:j]] #removes duplicate values

        editstaffroot = Tk() #creates window
        editstaffroot.geometry("350x300") #defines size
        editstaffroot.config(bg='#00B2EE') #defines bg colour
        editstaffroot.title("Edit Staff Member")
        item = ttk.Combobox(editstaffroot, values=output, width=45) #creates drop down menu
        item.place(x=30, y=60)
        item.bind('<Return>', staffmemberdelete) #Enter button binded to search command
        Label(editstaffroot, text="Select Member below below", font=('Helvetica', 13, 'bold'), bg='#00B2EE').place(x=60, y=20) #Creates display label

        editstaffroot.mainloop()



    conn = sqlite3.connect("SoftwareData.db")
    scursor = conn.cursor()

    counter = 0

    def search(*args):
        names = []
        output = []
        output2 = []
        x = staffsearch.get()
        print(x)
        staffsearch.delete(0, END)

        scursor.execute("""SELECT * FROM StaffInfo""")

        names.append(scursor.fetchall())

        names = str(names)

        print(names)

        if x in names:
            print("Found")
            scursor.execute("SELECT * FROM StaffInfo WHERE T1=?", (x,))
            output.append(scursor.fetchone())

            scursor.execute("SELECT * FROM StaffInfo WHERE T2=?", (x,))
            output.append(scursor.fetchone())


            scursor.execute("SELECT * FROM StaffInfo WHERE T3=?", (x,))
            output.append(scursor.fetchone())

            scursor.execute("SELECT * FROM StaffInfo WHERE T4=?", (x,))
            output.append(scursor.fetchone())

            scursor.execute("SELECT * FROM StaffInfo WHERE T5=?", (X,))
            output.append(scursor.fetchone())

            output = str(output)
            output = output.replace("None", "")
            output = output.replace(",", "")
            output = output.replace("[", "")
            output = output.replace("]", "")

            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            for x in range(0, len(days)):

                if days[x] in output:
                    print("Yes")
                    output2.append(days[x])
                else:
                    pass



            print(output2)
            output2 = str(output2)
            output2.replace("[", "")
            output2.replace("]", "")
            print(output2)

            output2 = "This member has shifts on " + output2
            outputwindow = Tk()
            outputwindow.title("Search")
            outputwindow.geometry("400x300")

            Label(outputwindow, text=output2, font=('Helvetica', 15, 'bold')).pack()
        else:
            messagebox.showinfo("Error", "Name not found")


    def stm():
        staffroot.destroy()
        stockmanager()


    def liststaff():
        output = [] #Output array created
        count = 0 #Variable used to count days
        appendcount = 0 #used as a condition meeter

        scursor.execute("""SELECT * FROM StaffInfo""") # Selects all from staffinfo

        databasetotal = scursor.fetchall() #fetches and stores
        
        databasetotal = ( ", ".join( repr(e) for e in databasetotal ) ) #removes square brackets

        print(databasetotal)

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] #array containing all days

        #while loop counts through each day, checking if they are in the variable before removing them

        while count != 7: 

            if days[count] in databasetotal:
                databasetotal = databasetotal.replace(days[count], "")
                count += 1
            else:

                count +=1


        print(databasetotal)


        #Removes any items classed as 'None'
        if 'None' in databasetotal:
            databasetotal = databasetotal.replace('None', '')

        else:
            pass
        #Creates the string into a list
        databasetotal = databasetotal.split()
        print(len(databasetotal))

        #iterates through the length of the databasetotal, appending to output array if not in there.
        for x in range (len(databasetotal)):

            if databasetotal[appendcount] not in output:
                output.append(databasetotal[appendcount])
                appendcount +=1
                print(output)
            else:
                print("Duplicate")
                pass

        #Converts to a list
        output = list(output)
        output.pop(0) #Pops empty item
        print(output)
        

        listdisplay = Tk() #Creates the window
        listdisplay.geometry("400x500") #Defines size
        listdisplay.title("List of Staff Members") #Defines name
        listdisplay.config(bg="#00B2EE") # Defines bg colour
        listdisplay.resizable(False, False)


        displaycount = 0 #condition for the for loop to iterate
        yval = 30 #Base y position
        for x in range (len(output)):
            Label(listdisplay, text=output[displaycount], font=('Helvetica', 20, 'bold'), bg='#00B2EE').place(x=100, y=yval) #Places indexed item on screen
            displaycount +=1 #Moves to next item
            yval +=60 #moves down by 60

        listdisplay.mainloop()

    def temp():
        print("Hello")

    staffroot = Tk()
    staffroot.geometry("1200x488")
    staffroot.title("Staff Manager")
    staffroot.config(bg="#00B2EE")
    staffroot.resizable(False, False)


    #This whole section consists of me utilising canvas and lines to create the overall gui.
    layer2 = Canvas(staffroot, width=900, height=380, bg="white", highlightbackground="black")
    layer2.place(x=20, y=20)
    layer2.create_line(80, 20, 80, 480, fill="black", width=2)
    layer2.create_line(260, 20, 260, 480, fill="black", width=2)
    layer2.create_line(430, 20, 430, 480, fill="black", width=2)
    layer2.create_line(600, 20, 600, 480, fill="black", width=2)
    layer2.create_line(780, 20, 780, 480, fill="black", width=2)
    layer3 = Canvas(staffroot, width=900, height=27, bg="#adeded", highlightbackground ="black")
    layer3.place(x=20, y=20)



    staffsearch = Entry(staffroot, width=45) #Here we create the search entry box
    staffsearch.bind('<Return>', search) #Enter button binded to search command
    staffsearch.place(x=100, y=429, height=30) #Entry box is placed
    searchdata = Label(staffroot, text="Search:", bg="#00B2EE", fg="black", font=('helvetica', 13, 'bold'), relief=FLAT)
    searchdata.place(x=20, y=429)

    #Label indicating the position of the entry button is created and placed


    stafflist = Button(staffroot, text="Staff List", fg="black", bg='#00B2EE', font=('Helvetica', 15), command=liststaff)
    stafflist.place(x=390, y=425)

    #Staff list button is created and placed

    nextweek = Button(staffroot, text="Next Week", fg="black", bg="#00B2EE", font=('Helvetica', 9, 'italic', 'bold'), relief=SUNKEN, borderwidth=0, command=temp)
    nextweek.place(x=858, y=410)

    #Next week button is created

    #In this section of code, all four main action buttons are created.

    b1 = Button(staffroot, text="Edit Shift", font=('helvetica', 20, 'bold'), command=editshift, bg="#1a8cff", fg="white", padx=28)
    b1.place(x=965, y=20)
    b2 = Button(staffroot, text="Edit Staff", font=('helvetica', 20, 'bold'),command=editstaff, bg="#1a8cff", fg="white", padx=28)
    b2.place(x=965, y=120)
    b3 = Button(staffroot, text="Stock \n Manager", font=('helvetica', 20, 'bold'), bg="#1a8cff", fg="white", padx=29, command=stm)
    b3.place(x=965, y=220)
    b4 = Button(staffroot, text="Take a Note", font=('helvetica', 20, 'bold'), bg="#1a8cff", fg="white", padx=12)
    b4.place(x=965, y=345)


    #This code creates all the relevant labels needed to for the table
    Label(staffroot, text="Week1", font=("Helvetica", 10, "italic"), bg="#00B2EE", fg="white").place(x=1140,y=460)
    Label(staffroot, text="Day", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=35, y=25)
    Label(staffroot, text="9:30-11:30", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=150, y=25)
    Label(staffroot, text="11:30-13:30", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=320, y=25)
    Label(staffroot, text="13:30-15:30", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=500, y=25)
    Label(staffroot, text="15:30-17:30", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=670, y=25)
    Label(staffroot, text="17:30-19:30", font=("Helvetica", 10, "bold"), bg="#adeded").place(x=815, y=25)
    mbar = Menu(staffroot)
    staffroot.config(menu=mbar)
    filemenu = Menu(mbar, tearoff=False)
    mbar.add_cascade(label="File", menu=filemenu)
    mbar.add_cascade(label="Options", menu=filemenu)





    scursor.execute("""SELECT * FROM StaffInfo""")
    staffinfodata = scursor.fetchall()
    xpos = 135
    ypos = 60

    for x in range (0, (len(staffinfodata))):
 
        SO = list(staffinfodata[counter])
        SO.pop(0)



        layer2.create_text(13,60,fill="black",font=('helvetica', 13, 'bold'),text="Monday", anchor=W)
        layer2.create_text(11,120,fill="black",font=('helvetica', 12, 'bold'),text="Tuesday", anchor=W)
        layer2.create_text(11,180,fill="black",font=('helvetica', 8, 'bold'),text="Wednesday", anchor=W)
        layer2.create_text(10,240,fill="black",font=('helvetica', 9, 'bold'),text="Thursday", anchor=W)
        layer2.create_text(13,300,fill="black",font=('helvetica', 13, 'bold'),text="Friday", anchor=W)
        layer2.create_text(11,360,fill="black",font=('helvetica', 12, 'bold'),text="Saturday", anchor=W)
        layer2.create_text(13,420,fill="black",font=('helvetica', 9, 'bold'),text="Sunday", anchor=W)


        layer2.create_text(xpos,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[0], anchor=W)
        layer2.create_text(xpos+180,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[1], anchor=W)
        layer2.create_text(xpos+350,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[2], anchor=W)
        layer2.create_text(xpos+530,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[3], anchor=W)
        layer2.create_text(xpos+670,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[4], anchor=W)

        # Label(layer2, text=sso, font=('helvetica', 15, 'bold'), bg='white').place(x=xpos,y=ypos)


        counter += 1
  
        ypos +=60

    staffroot.mainloop()


