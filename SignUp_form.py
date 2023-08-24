# ----- SIGN UP/Registration tkinter form------
from tkinter import *
import tkinter
import os
from tkinter import messagebox
from PIL import ImageTk, Image

top = Tk()
# top.geometry('1000x700')
top.title("SIGN UP")
# f1= tkinter.Frame(top)
# f1.pack()

def login():
    top.destroy()
    os.system("SIGN_IN.py")

def insert():

    k1 = str(e1.get())
    k2 = str(e2.get())
    k3 = str(e3.get())
    k4 = str(e4.get())
    k5 = str(e5.get())
    k6 = str(e6.get())
    k7 = str(e7.get())
    k8 = str(e7.get())

    import pymysql as c
    db = c.connect(host="localhost",
               user="root",
               passwd="Batman",
               database="reg")
    cursor = db.cursor()
    s = "Insert into user values('{}','{}','{}','{}','{}','{}','{}','{}')".format(4,k1, k2, k3, k4, k5, k6, k7, k8)
    result= cursor.execute(s)

    if (result>0):  # Python understand 0 false 1 for true--
        messagebox.showinfo("Welcome", "User Created Successfully")
    else:
        messagebox.showerror("Welcome", "Error")
    db.commit()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)


def remove():
    k1 = str(e1.get())

    import pymysql as c
    db = c.connect(host="localhost",
                   user="root",
                   passwd="Batman",
                   database="reg")
    cursor = db.cursor()
    s = "delete from user where username =%s"
    result = cursor.execute(s, k1)

    if (result > 0):  # Python understand 0 false 1 for true--
        messagebox.showinfo("Welcome", "User Deleted Successfully")
    else:
        messagebox.showwarning("Welcome", "Enter the Correct First Name")
    db.commit()
    e1.delete(0, END)

# ---For image Import------
path = "D:/img1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
l6 = Label(top, image=img)
l6.pack()

l = Label(top, text="SIGN UP FORM", fg='black', bg='white', font=("Arial 50 bold"))
l.place(x=300, y=10)

l1 = Label(top, text="First Name:", fg='black', bg='white', font=("Arial 20 bold"))
l1.place(x=250, y=125)

e1 = Entry(top, font=("Arial 20 bold"))
e1.place(x=550, y=125)

l2 = Label(top, text="Last Name :", fg='black', bg='white', font=("Arial 20 bold"))
l2.place(x=250, y=185)

e2 = Entry(top, font=("Arial 20 bold"))
e2.place(x=550, y=185)

l3 = Label(top, text="Gender :", fg='black', bg='white', font=("Arial 20 bold"))
l3.place(x=250, y=245)

e3 = Entry(top, font=("Arial 20 bold"))
e3.place(x=550, y=245)

l4 = Label(top, text="Contact :", fg='black', bg='white', font=("Arial 20 bold"))
l4.place(x=250, y=305)

e4 = Entry(top, font=("Arial 20 bold"))
e4.place(x=550, y=305)

l5 = Label(top, text="User Name :", fg='black', bg='white', font=("Arial 20 bold"))
l5.place(x=250, y=365)

e5 = Entry(top, font=("Arial 20 bold"))
e5.place(x=550, y=365)

l6 = Label(top, text="Password :", fg='black', bg='white', font=("Arial 20 bold"))
l6.place(x=250, y=425)

e6 = Entry(top, font=("Arial 20 bold"),show="*")
e6.place(x=550, y=425)

l7 = Label(top, text="Verify Password :", fg='black', bg='white', font=("Arial 20 bold"))
l7.place(x=250, y=485)

e7 = Entry(top, font=("Arial 20 bold"))
e7.place(x=550, y=485)


b1 = Button(top, text="CREATE", fg='white', bg='green', font=("Arial 20 bold"),command=insert)
b1.place(x=350, y=560)

b2 = Button(top, text="REMOVE", fg='white', bg='red', font=("Arial 20 bold"),command=remove)
b2.place(x=550, y=560)

b3 = Button(top, text="Go To login Page", fg='white', bg='blue', font=("Arial 15"),command=login)
b3.place(x=430, y=650)

top.mainloop()