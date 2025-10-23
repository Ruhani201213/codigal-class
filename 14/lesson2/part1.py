from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('500x500')

upload = Image.open("img.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=450, width=400)
label.place(x=50, y=0)
labe12 = Label(root, text="This is how you add an image in Tkinter Window")
labe12.place(x=50, y=420)

root.mainloop()