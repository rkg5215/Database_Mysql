from tkinter import *
import os
top=Tk()
top.geometry('1000x600')
top.title("Welcome To dashboard")

def login():
    top.destroy()
    os.system("SIGN_IN.py")

f1=Frame(top,height=600,width=1000,bg='orange')
f1.pack()


b1=Button(f1,text="Go to Login Page",command=login)
b1.place(x=400,y=300)


top.mainloop()