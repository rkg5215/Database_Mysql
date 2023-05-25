from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

top = Tk()
top.title('Calculator')
top.geometry('1200x600')

path = "D:/Python(Gaurav Sir)/GUI/image.png"
img = ImageTk.PhotoImage(Image.open(path))
l6 = Label(top, image=img)
l6.pack()


# def insert():
#     k=e1.get()
#     k1=e2.get()
#     k2=e3.get()
#     import pymysql as sql
#     db=sql.connect(host='localhost',user='root',passwd='mayank',db='meerut')
#     cur=db.cursor()
#     s="insert into emp values('%s','%s','%s')"%(k,k1,k2)
#     result=cur.execute(s)
#     if(result>0):
#         messagebox.showinfo("Welcome","Succeessfully, sumit")
#     else:
#         messagebox.showerror("Welcome","error")
#     db.commit()


# def delete():
#     k=int(e1.get())
#     # k1=e2.get()
#     # k2=e3.get()
#     import pymysql as sql
#     db=sql.connect(host='localhost',user='root',passwd='mayank',db='meerut')
#     cur=db.cursor()
#     s="delete from emp where id='%s'"
#     result=cur.execute(s,k)
#     if(result>0):
#         messagebox.showinfo("Welcome","Succeessfully, delete")
#     else:
#         messagebox.showerror("Welcome","error")
#     db.commit()

def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', passwd='mayank', db='meerut')
    cur = db.cursor()
    cur.execute("Select * from emp where name=%s and lastname=%s", (e2.get(), e3.get()))
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("Error", "Invalid user name and password")
    else:
        top.destroy()
        os.system("python Frame.py")


l = Label(top, text="Registration", fg='black', bg='powder blue', font=("Arial 25 bold"))
l.place(x=450, y=30)

# l1 = Label(top,text="ID:",fg='white',bg='blue',font=("Arial 20 bold"))
# l1.place(x=300,y=200)
# e1=Entry(top,bg='sky blue',font="Arial 20 bold")
# e1.place(x=550,y=200)

l2 = Label(top, text="Name:", fg='white', bg='blue', font=('Arial 20 bold'))
l2.place(x=300, y=250)
e2 = Entry(top, bg='sky blue', font=("Arial 20 bold"))
e2.place(x=550, y=250)

l3 = Label(top, text="Password:", fg='white', bg='blue', font=('Arial 20 bold'))
l3.place(x=300, y=300)
e3 = Entry(top, bg='sky blue', font=("Arial 20 bold"), show="*")
e3.place(x=550, y=300)

# b1=Button(top,text='insert',width=10,bg='red',fg='black',font=("Arial 20 bold"),command=insert)
# b1.place(x=450,y=400)

b2 = Button(top, text='Login', width=10, bg='red', fg='black', font=("Arial 20 bold"), command=Login)
b2.place(x=450, y=480)

top.config(bg="green")
top.mainloop()
