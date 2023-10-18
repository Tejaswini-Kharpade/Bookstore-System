from tkinter import *
from Database import *

class Addoffset():

    def __init__(self):
        win=Tk()

        bg=PhotoImage(file='G:\A-TEJASWINI\Education\python\Projects\TejaswiniK\Bookstore\Royalblue.png')

        label = Label(win, image=bg)
        label.place(x=0, y=0)

        #Title
        win.title("Bookstore")
        win.configure(bg='#EEC591')

        #Functions
        def adddb():
            insertTable(e1.get(),e2.get(),e3.get(),e4.get())
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            viewdb()

        def viewdb():
            lb1.delete(0,END)
            for i in readTable():
                lb1.insert(END,i)

        def searchdb():
            lb1.delete(0, END)
            for i in searchTable(e1.get(),e2.get(),e3.get(),e4.get()):
                lb1.insert(END, i)

        def list_select(e):
            global b
            try:
                #print(e)
                g=lb1.curselection()
                #print(g)
                b=lb1.get(g)
                #print(b)
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e1.insert(END,b[1])
                e2.insert(END,b[2])
                e3.insert(END,b[3])
                e4.insert(END,b[4])
            except:
                pass

        def deletedb():
            delTable(b[0])
            viewdb()

        def updatedb():
            updateTable(e1.get(),e2.get(),e3.get(),e4.get(),b[0])
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            viewdb()




        group_frame = Frame(win)
        group_frame.grid(row=0, column=0, sticky='WENS')
        group_frame.configure(bg='#EEC591')
        label = Label(group_frame, image=bg)
        label.place(x=0, y=0)

        #Labels
        l1=Label(group_frame,text="Title",font=("Verdana", 10,'bold')).grid(row=0,column=0,padx=(10), pady=10,)
        l2=Label(group_frame,text="Author  ",font=("Verdana", 10,'bold')).grid(row=0,column=3,padx=(10), pady=10)
        l3=Label(group_frame,text="Price",font=("Verdana", 10,'bold')).grid(row=2,column=0,padx=(10), pady=10)
        l4=Label(group_frame,text="Year  ",font=("Verdana", 10,'bold')).grid(row=2,column=3,padx=(10), pady=10)


        #Entries
        Title_value=StringVar()
        e1=Entry(group_frame,textvariable=Title_value)
        e1.grid(row=0,column=2,padx=(10), pady=10)
        Author_value=StringVar()
        e2=Entry(group_frame,textvariable=Author_value)
        e2.grid(row=0,column=4,padx=(10), pady=10)
        Price_value=DoubleVar()
        e3=Entry(group_frame,textvariable=Price_value)
        e3.grid(row=2,column=2,padx=(10), pady=10)
        Year_value=IntVar()
        e4=Entry(group_frame,textvariable=Year_value)
        e4.grid(row=2,column=4,padx=(10), pady=10)

        group1 = LabelFrame(win)
        group1.grid(row=1, column=0,sticky='WENS')



        group2= LabelFrame(win)
        group2.grid(row=1, column=1,rowspan=4, sticky=N)
        # group2.configure(bg='#EEC591')


        win.columnconfigure(0, weight=9)
        win.columnconfigure(1, weight=1)
        win.rowconfigure(0, weight=1)
        win.rowconfigure(1, weight=9)

        group1.rowconfigure(0, weight=1)
        group1.columnconfigure(0, weight=1)

        group2.rowconfigure(0, weight=1)
        group2.columnconfigure(0, weight=1)


        #listbox
        lb1=Listbox(group1,width=42,height=10)
        lb1.grid(row=0,column=0,sticky='WENS')



        lb1.bind("<<ListboxSelect>>", list_select)
        #Buttons
        b1=Button(group2,text="Add",width=20,command=adddb,font=("Verdana", 10,'bold'))
        b1.grid(row=1,column=0, sticky=W+E)
        b2=Button(group2,text="Read",width=20,command=viewdb,font=("Verdana", 10,'bold'))
        b2.grid(row=2,column=0, sticky=W+E)
        b3=Button(group2,text="Update",width=20,command=updatedb,font=("Verdana", 10,'bold'))
        b3.grid(row=3,column=0, sticky=W+E)
        b4=Button(group2,text="Delete",width=20,command=deletedb,font=("Verdana", 10,'bold'))
        b4.grid(row=4,column=0, sticky=W+E)
        b5=Button(group2,text="Search",width=20,command=searchdb,font=("Verdana", 10,'bold'))
        b5.grid(row=5,column=0, sticky=W+E)
        b6=Button(group2,text="Clear",width=20,command=win.destroy,font=("Verdana", 10,'bold'))
        b6.grid(row=6,column=0, sticky=W+E)



        win.mainloop()
