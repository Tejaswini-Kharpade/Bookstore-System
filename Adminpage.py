from tkinter import *
import Mainpage as bk
from tkinter import messagebox


mGui=Tk()
mGui.title("Bookstore")
width,height=750,400
v_dim=str(width)+'x'+str(height)
mGui.geometry(v_dim)


bg=PhotoImage(file='G:\A-TEJASWINI\Education\python\Projects\TejaswiniK\Bookstore\Royalblue.png')

label = Label(mGui, image=bg)
label.place(x=0, y=0)


def askoffset():
    print("logged in")
    mGui.destroy()
    of=bk.Addoffset()

L1=Label(mGui,text="USER ID",width=9,height=1,font=("Verdana", 10,'bold')).place(relx = 0.4, rely = 0.4, anchor = CENTER)
L2=Label(mGui,text="PASSWORD",width=9,height=1,font=("Verdana", 10,'bold')).place(relx = 0.4, rely = 0.5, anchor = CENTER)

logid=StringVar()
E1=Entry(mGui,textvariable=logid)
E1.place(relx = 0.55, rely = 0.4, anchor = CENTER)
password=StringVar()
E2=Entry(mGui,textvariable=password)
E2.place(relx = 0.55, rely = 0.5, anchor = CENTER)

def validate_login():
    userid = logid.get()
    Pass = password.get()

    if userid == "Admin" and Pass == "admin123":
       #Label(mGui,text="Login successfull")
       return askoffset()
       #messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
       #Label(mGui,text="Login ID or Password is wrong")
       messagebox.showerror("Login Failed", "Invalid username or password")



Button(mGui,text="LOGIN",command=validate_login,width=10,height=1,font=("Verdana", 10,'bold')).place(relx = 0.5, rely = 0.6, anchor = CENTER)

mGui.mainloop()
