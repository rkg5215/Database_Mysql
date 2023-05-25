# ----- SIGN IN /LOGIN tkinter form------
from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk, Image
top = Tk()
top.geometry('1000x600')
top.title("SIGN IN")
# G
def login():
    import pymysql as c
    db = c.connect(host="localhost",
               user="root",
               passwd="Batman",
               db="reg")
    cur = db.cursor()
    cur.execute("Select * from user where Username=%s and Password=%s", (e1.get(),e2.get()))
    row = cur.fetchone()

    if row==None:
        messagebox.showinfo("Error", "Invalid Username and Password")
    else:
        top.destroy()
        os.system("dashboard.py")

def signup():
    top.destroy()
    os.system("SignUp_form.py")

# ---For image Import------
path = "D:/img1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
l6 = Label(top, image=img)
l6.pack()

l1 = Label(top, text="LOGIN", fg='black', bg='white', font=("Arial 50 bold"))
l1.place(x=450, y=50)

l1 = Label(top, text="Username:", fg='black', bg='white', font=("Arial 25 bold"))
l1.place(x=350, y=250)

e1 = Entry(top, font=("Arial 25 bold"))
e1.place(x=550, y=250)

l2 = Label(top, text="Password :", fg='black', bg='white', font=("Arial 25 bold"))
l2.place(x=350, y=350)

e2 = Entry(top, font=("Arial 25 bold"))
e2.place(x=550, y=350)


b1 = Button(top, text="LOGIN", fg='white', bg='green', font=("Arial 25 bold"),command=login)
b1.place(x=470, y=450)

b2 = Button(top, text="Sign Up", fg='white', bg='blue', font=("Arial 15"),command=signup)
b2.place(x=500, y=530)

top.mainloop()