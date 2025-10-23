from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')


upload = Image.open("img. jpg")

upload = upload.resize((300, 300))

image = ImageTk. PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root,
text="Hey User! Welcome to Denomination Counter Application.",
bg='light blue')
label1.place(x=180, y=340)
label1 = Label(root,
text="Hey User! Welcome to Denomination Counter Application.",
bg='light blue')
label1.place(x=180, y=340)


def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()


button1 = Button(root,
text="Let's get started!",
command=msg,
bg='brown',
fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350")

label = Label(top, text="Enter total amount", bg='light grey')
entry = Entry(top)
1bl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

11 = Label(top, text="2000", bg='light grey' )

Centering waeets ii the Top Rindae
label.place(a-200, y-5a)
entry.place(x=200, y-b)
bn.place(s=248, y=129)
1b1.place(w=140, y-179)

11.place(m-180, y-209)
12.placa(m-180, y=23)
13.place(m=388, y=26)

t1.place( == 278, y=209)
t2.place(w-270, y-220)
t3.place(x=270, y=200)

top.matnLoop<]

root.mainloog()