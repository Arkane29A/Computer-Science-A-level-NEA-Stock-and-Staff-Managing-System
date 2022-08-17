from tkinter import *

root = Tk()

root.geometry("500x500")

root.config(background='#00B2EE')
position = [70, 150, 220]

class notes:
    def __init__(self, master, note, notex, notey):
        
        def xbutton():
            self.click.destroy()
            self.display.destroy()
            position.pop()
            print(position)

        self.note = "Note: " + note
        self.notex = notex
        self.notey = notey


        self.click = Button(root, text="X", command=xbutton)
        self.click.place(x=notex-25, y=notey)

        self.display = Label(root, text=self.note, bg='#00B2EE')
        self.display.place(x=notex, y=notey)




note1 = notes(root, "doggy", 50, position[0])
note2= notes(root, "ass cunt", 50, position[1])
note3= notes(root, "take out the dog", 50, position[2])



root.mainloop()
