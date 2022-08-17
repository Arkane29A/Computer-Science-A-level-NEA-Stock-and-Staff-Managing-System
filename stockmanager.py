from tkinter import *
from tkinter import messagebox
import sqlite3
import importlib
from PIL import ImageTk, Image
import random
from tkinter import ttk
from staffmanager import * 






def stockmanager():

    def options():
        def backgroundchange(event):
            x = backgrounds.get()

            if x == "Red":
                root.config(bg="Red")

            elif x == "Blue":
                root.config(bg="Blue")

            elif x == "Yellow":
                root.config(bg="Yellow")

            elif x == "Green":
                root.config(bg="Green")


        bgs = ["Red", "Blue", "Yellow", "Green"]
        fnts = ['Helvetica', 'Arial', 'MS Serif', 'MS Sans Serif']
        
        optionroot = Tk()
        optionroot.geometry("300x300")
        optionroot.title("Options")


        Label(optionroot, text="Manage Backgrounds", font=("Helvetica", 12, 'bold')).pack()
        backgrounds = ttk.Combobox(optionroot, values=bgs, width=45)
        backgrounds.pack()
        backgrounds.bind('<Return>', backgroundchange)

        optionroot.mainloop()

    counter = 0


    def shipment():

        def shipmentextended(event): 

            def update(event):
                checknewval = newval.get() #gets the value from the drop down menu
                if checknewval.isdigit() == True: #if the entered character is a number character, convert to integer
                    checknewval = int(checknewval)

                    scursor.execute('UPDATE StockInfo SET Quantity=?', [checknewval])
                    messagebox.showinfo("Successful", "Item quantity successfully updated")


                else:
                    messagebox.showinfo("Error", "Please enter a number") #Validation to exclude any incorrect characters



            dropdownval = item.get() #gets the value from the drop down menu and stores in a variable

            Label(shipmentroot, text="Input new shipment amount", bg='#00B2EE', font=('Helvetica', 13, 'bold')).place(x=70, y=110) #Creates the label

            newval = Entry(shipmentroot, width=49) #Creates the entry widget to update the quantity attribute
            newval.place(x=30, y=140)
            newval.bind('<Return>', update) #Binds to enter button




        #count variable used to index through the database data
        countdrop = 0

        #Output array
        itemdropdown = []
        scursor.execute("""SELECT * FROM StockInfo""")
        stockinfodata = scursor.fetchall()
        stockinfodata = list(stockinfodata)

        for x in range(0, len(stockinfodata)):
            stockinfodata = list(stockinfodata) #creates a list which is appendable based on index
            x = list(stockinfodata[countdrop]) 
            x.pop(0) #Pops identifier
            x = x[2]
            itemdropdown.append(x)
            countdrop +=1

        shipmentroot = Tk()
        shipmentroot.title("Shipment")
        shipmentroot.geometry("350x300")
        shipmentroot.config(bg='#00B2EE')

        item = ttk.Combobox(shipmentroot, values=itemdropdown, width=45)
        item.place(x=30, y=60)
        item.bind('<Return>', shipmentextended) #Enter button binded to search command
        Label(shipmentroot, text="Select Item below", font=('Helvetica', 13, 'bold'), bg='#00B2EE').place(x=100, y=20)

        shipmentroot.mainloop()



    def EditStock():

        def callback():

            def delete():
                scursor.execute("DELETE FROM StockInfo WHERE Item=?", (selecteditem,))
                conn.commit()
                messagebox.showinfo("Succesful", "Record Deleted")
                editstockroot.destroy()
                root.destroy()
                stockmanager()

            def update():
                
                #Selects the item selected from the drop down menu to update
                scursor.execute("SELECT ItemID FROM StockInfo WHERE Item=?", (selecteditem,))
                cc = scursor.fetchall()
                cc = str(cc)[1:-1] 
                #Formates the item into readable format
                checker = cc.replace(",", "")
                checker = checker.replace(" ", "") #Removes commas and whitespace
                checker = checker.replace(" ", "") #Removes brackets
    
                #updates the inputted values into the database


                numbervalidation = [(newquanentry.get()).isdigit(), (newpriceentry.get()).isdigit(), (newsoldentry.get()).isdigit()]

                for x in range(0, len(numbervalidation)):
                    if numbervalidation[x] != False:
                        pass
                    else:
                        messagebox.showinfo("Error", "Please enter valid data")



                scursor.execute('UPDATE StockInfo SET Item=? WHERE ItemID =? ', [newitementry.get(), cc])
                scursor.execute('UPDATE StockInfo SET Category=? WHERE ItemID =? ', [newcatentry.get(), cc])
                scursor.execute('UPDATE StockInfo SET Supplier=? WHERE ItemID =? ', [newsupentry.get(), cc])
                scursor.execute('UPDATE StockInfo SET Quantity=? WHERE ItemID =? ', [newquanentry.get(), cc])
                scursor.execute('UPDATE StockInfo SET Price=? WHERE ItemID =? ', [newpriceentry.get(), cc])
                scursor.execute('UPDATE StockInfo SET Sold=? WHERE ItemID =? ', [newsoldentry.get(), cc])

                conn.commit()
                conn.close()

            def submit():
  
                randid = [] #Array created
                for x in range(0,3):
                    randid.append(random.randint(0,9)) #Randomly generates 3 digits and adds them to the array for use as an identifier

                randid = str(randid)[1:-1] #Removes brackets

                randomID = randid.replace(",", "")
                randomID = randomID.replace(" ", "") #Removes commas and whitespace
                randomID = "A" + randomID #Fully formates for use as ItemId

                conn = sqlite3.connect("SoftwareData.db") #connection to database is created
                scursor = conn.cursor()

                #All user inputted data is stored in the database 

                scursor.execute("insert into StockInfo (ItemId, Category, Supplier, Item, Quantity, Price, Sold) values (?, ?, ?, ?, ?, ?, ?)",
                            (randomID, newcatentry.get(), newsupentry.get(), newitementry.get(), newquanentry.get(),newpriceentry.get(), newsoldentry.get() ))

                conn.commit()             

                messagebox.showinfo("Successful", "New Item Added")

                editstockroot.destroy()
                root.destroy()
                stockmanager()


            

            if firstdropdown.get() == "": #If a selection from the dropdown is empty, print empty selection
                print("empty selection")

            elif firstdropdown.get() == "New Item": #if selection is 'New Item', run condition
                coverup = Canvas(editstockroot, width=400, height=600, bg="#00B2EE")
                coverup.pack()
                Label(editstockroot, text="Create New Item", font=('Helvetica', 20, 'bold'), bg='#00B2EE', fg="#9b9e9c").place(x=80, y=20) #creates label

                print("New item selected")

                #This section of code creates all relevant entry widgets for the user to add their item
                newitementry = Entry(editstockroot, width=55)
                newitementry.place(x=30, y=100)
                Label(editstockroot, text="Item", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=65)
                newcatentry = Entry(editstockroot, width=55)
                newcatentry.place(x=30, y=170)
                Label(editstockroot, text="Category", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=135)
                newsupentry = Entry(editstockroot, width=55)
                newsupentry.place(x=30, y=240)
                Label(editstockroot, text="Supplier", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=205)
                newquanentry = Entry(editstockroot, width=55)
                newquanentry.place(x=30, y=310)
                Label(editstockroot, text="Quantity", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=275)
                newpriceentry = Entry(editstockroot, width=55)
                newpriceentry.place(x=30, y=380)
                Label(editstockroot, text="Price", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=345)
                newsoldentry = Entry(editstockroot, width=55)
                newsoldentry.place(x=30, y=450)
                Label(editstockroot, text="Sold", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=415)

                Button(editstockroot, text="Submit", command=submit, bg='#00B2EE', relief=FLAT, font=('Helvetica', 15, 'bold')).place(x=150, y=500) #Submit button


            else:

                selecteditem = firstdropdown.get()

                coverup = Canvas(editstockroot, width=400, height=600, bg="#00B2EE")
                coverup.pack()
                Label(editstockroot, text="Edit Item Below", font=('Helvetica', 20, 'bold'), bg='#00B2EE', fg="#9b9e9c").place(x=65, y=20)
                                
                conn = sqlite3.connect("SoftwareData.db")
                scursor = conn.cursor()

                scursor.execute("SELECT * FROM StockInfo WHERE Item=?", (selecteditem,))
                edititem = scursor.fetchall()

                updateditem= []

                newitementry = Entry(editstockroot, width=55)
                newitementry.place(x=30, y=100)
                Label(editstockroot, text="Item", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=65)
                newcatentry = Entry(editstockroot, width=55)
                newcatentry.place(x=30, y=170)
                Label(editstockroot, text="Category", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=135)
                newsupentry = Entry(editstockroot, width=55)
                newsupentry.place(x=30, y=240)
                Label(editstockroot, text="Supplier", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=205)
                newquanentry = Entry(editstockroot, width=55)
                newquanentry.place(x=30, y=310)
                Label(editstockroot, text="Quantity", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=275)
                newpriceentry = Entry(editstockroot, width=55)
                newpriceentry.place(x=30, y=380)
                Label(editstockroot, text="Price", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=345)
                newsoldentry = Entry(editstockroot, width=55)
                newsoldentry.place(x=30, y=450)
                Label(editstockroot, text="Sold", font=('Helvetica', 10, 'bold'), bg='#00B2EE').place(x=25, y=415)

                Button(editstockroot, text="Update", command=update, bg='#00B2EE', relief=FLAT, font=('Helvetica', 15, 'bold')).place(x=150, y=500)
                Button(editstockroot, text="Delete", command=delete, bg='#00B2EE', relief=FLAT, font=('Helvetica', 15, 'bold')).place(x=150, y=550)

        countdrop = 0 #Count variable used in for loop
        fdropdown = [] #Contents of the second drop down window

        scursor.execute("""SELECT * FROM StockInfo""") #selects all data from StockInfo
        stockinfodata = scursor.fetchall() #Stores in variable
        stockinfodata = list(stockinfodata) #Converts into a list
        
        editstockroot = Tk() #window created and definmed
        editstockroot.title("Edit Stock")
        editstockroot.config(bg="#00B2EE")

        editstockroot.geometry("400x600")

        Label(editstockroot, text="Edit stock below", font=('Helvetica', 20, 'bold'), bg='#00B2EE', fg="#9b9e9c").place(x=85, y=20)
        Label(editstockroot, text="Item", font=('Helvetica', 15, 'bold'), bg='#00B2EE').place(x=160, y=70)


        for x in range(0, len(stockinfodata)):
            stockinfodata = list(stockinfodata)
            x = list(stockinfodata[countdrop]) #creates a list which is appendable based on index
            x.pop(0) #pops identifer from list
            x = x[2]
            fdropdown.append(x)
            countdrop +=1
        fdropdown.append("New Item") #Final option to allow user to add new item

        firstdropdown = ttk.Combobox(editstockroot, values=fdropdown, width=45)
        firstdropdown.place(x=40, y=115)

        confirmbutton = Button(editstockroot, text="confirm", command=callback, bg='#00B2EE', relief=FLAT, font=('Helvetica', 8, 'bold'))
        confirmbutton.place(x=335, y=115) #Confirm button attached to callback function

        editstockroot.mainloop()



    def sm():
        root.destroy()
        staffmanager()



    def takeanote():
        pass


    #This section of code creates the window and sets its size, colour and further options.
    root = Tk()
    root.geometry("1200x488")
    root.title("Stock Manager")
    root.config(bg="#00B2EE")
    root.resizable(False, False) #Prevents the window from being resized.


    #This whole section consists of me utilising canvas and lines to create the overall gui.
    #Here I create a canvas for the data to be outputted to.


    layer2 = Canvas(root, width=950, height=450, bg="white", highlightbackground="black")
    layer2.place(x=20, y=20)
        
    layer2.create_line(80, 20, 80, 480, fill="black", width=2)


    layer2.create_line(260, 20, 260, 480, fill="black", width=2)
    layer2.create_line(430, 20, 430, 480, fill="black", width=2)
    layer2.create_line(600, 20, 600, 480, fill="black", width=2)
    layer2.create_line(780, 20, 780, 480, fill="black", width=2)
    
    layer3 = Canvas(root, width=950, height=27, bg="#adeded", highlightbackground ="black")
    layer3.place(x=20, y=20)

    scroll = Scrollbar(layer2, orient=VERTICAL, command=layer2.yview)
    scroll.place()





    Label(root, text="Item", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=28, y=23)
    Label(root, text="Category", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=109, y=23)
    Label(root, text="Quantity", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=290, y=23)
    Label(root, text="Price", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=460, y=23)
    Label(root, text="Supplier", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=630, y=23)
    Label(root, text="Sold", bg="#adeded", fg="black", font=('helvetica', 13, 'bold')).place(x=800, y=23)





    b1 = Button(root, text="Edit Stock", command=EditStock, font=('helvetica', 20, 'bold'), bg="#1a8cff", fg="white", padx=23)
    b1.place(x=985, y=60)

    b2 = Button(root, text="Staff Manager", command=sm, font=('helvetica', 20, 'bold'), bg="#1a8cff", fg="white")
    b2.place(x=985, y=180)

    b3 = Button(root, text="Take a Note", command=takeanote, font=('helvetica', 20, 'bold'), bg="#1a8cff", fg="white", padx=14)
    b3.place(x=985, y=300)



    mbar = Menu(root)
    root.config(menu=mbar)

    filemenu = Menu(mbar, tearoff=False)
    mbar.add_cascade(label="File", menu=filemenu)
    filemenu.add_cascade(label="Manage Options", command=options)


    shipmentoption = Menu(mbar, tearoff= FALSE)
    mbar.add_cascade(label="Shipment", menu=shipmentoption)
    shipmentoption.add_cascade(label="Create Shipment", command=shipment)






    #Creates a connection to the database and stores all contents of StockInfo in a variable
    conn = sqlite3.connect("SoftwareData.db")
    scursor = conn.cursor()
    scursor.execute("""SELECT * FROM StockInfo""")
    stockinfodata = scursor.fetchall()



    xpos = 20 #Base x position
    ypos = 60 #Base y position


    for x in range (0, (len(stockinfodata))): #For loop in terms of length of stockinfodata
        SO = list(stockinfodata[counter]) #Made into a list and goes through every row using counter
        SO.pop(0) #Pops the identifier

        SOorder = [2, 0, 3, 4, 1, 5] 
        SO = [SO[i] for i in SOorder] #Reorders the list for display

        #Displays the row
        layer2.create_text(xpos,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[0], anchor=W)
        layer2.create_text(xpos+120,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[1], anchor=W)
        layer2.create_text(xpos+305,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[2], anchor=W)
        layer2.create_text(xpos+470,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[3], anchor=W)
        layer2.create_text(xpos+620,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[4], anchor=W)
        layer2.create_text(xpos+830,ypos,fill="black",font=('helvetica', 13, 'bold'),text=SO[5], anchor=W)



        counter += 1 #goes to the next row
        ypos +=60 #moves the next item down by 60

    root.mainloop()



