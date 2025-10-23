from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('500x500')

def msg():
    messagebox.showwarning("a;ert there is a virus")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=50, y=80)


root.mainloop()
