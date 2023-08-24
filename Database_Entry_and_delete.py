# ----- Database Connectivity using tkinter form------
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

top = Tk()
top.geometry('1000x600')
top.title("Database Entry Form")

def insert():

    k1 = int(e1.get())
    k2 = str(e2.get())
    k3 = str(e3.get())
    import pymysql as c
    db = c.connect(host="localhost",
               user="root",
               passwd="Batman",
               database="noida")
    cursor = db.cursor()
    s = "Insert into emp values({},'{}','{}')".format(k1, k2, k3)  #--Second way-----s = "Insert into emp values('%s','%s','%s')"%(k1, k2, k3)
    result= cursor.execute(s)

    if (result>0):  # Python understand 0 false 1 for true--
        messagebox.showinfo("Welcome", "Data Inserted Successfully")
    else:
        messagebox.showerror("Welcome", "Error")
    db.commit()

def delete():
    k1=int(e1.get())

    import pymysql as c
    db = c.connect(host="localhost",
                   user="root",
                   passwd="Batman",
                   database="noida")
    cursor = db.cursor()
    s = "delete from emp where id ='%s'"
    result = cursor.execute(s,k1)

    if (result > 0):  # Python understand 0 false 1 for true--
        messagebox.showinfo("Welcome", "Successfully Deleted")
    else:
        messagebox.showwarning("Welcome", "Enter the Correct Id")
    db.commit()

# ---For image Import------
# path = "E:/img1.jpg"
# img = ImageTk.PhotoImage(Image.open(path))
# l6 = Label(top, image=img)
# l6.pack()

l1 = Label(top, text="ID:", fg='black', bg='white', font=("Arial 25 bold"))
l1.place(x=450, y=200)

e1 = Entry(top, font=("Arial 25 bold"))
e1.place(x=550, y=200)

l2 = Label(top, text="Firstname :", fg='black', bg='white', font=("Arial 25 bold"))
l2.place(x=350, y=300)

e2 = Entry(top, font=("Arial 25 bold"))
e2.place(x=550, y=300)

l3 = Label(top, text="Lastname: ", fg='black', bg='white', font=("Arial 25 bold"))
l3.place(x=350, y=400)

e3 = Entry(top, font=("Arial 25 bold"))
e3.place(x=550, y=400)

b1 = Button(top, text="SUBMIT", fg='white', bg='green', font=("Arial 25 bold"),command=insert)
b1.place(x=400, y=500)

b2 = Button(top, text="DELETE", fg='white', bg='red', font=("Arial 25 bold"),command=delete)
b2.place(x=600, y=500)

top.mainloop()