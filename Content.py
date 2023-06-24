from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk
import tkinter as tk

#============================= FUCTIONS =================================================#
def save():
    import sqlite3
    from tkinter import messagebox
    
    conn=sqlite3.connect("info.db")
    cursor=conn.cursor()
    print("Cursor Made")
    
    cursor.execute('''create table if not exists student (
    st_nm TEXT,
    st_cls TEXT,
    st_ID INTEGER,
    st_dob TEXT,
    st_year TEXT,
    st_fthr TEXT,
    st_mthr TEXT,
    st_per INTEGER
    )''')
    print("Sudent table created")

    cursor.execute("INSERT INTO student (st_nm, st_cls, st_ID, st_dob, st_year, st_fthr, st_mthr, st_per) VALUES(?, ?, ?, ?, ?, ?,?,?)",
                   (str(ent1.get()),
                    str(c.get()),
                    str(ent3.get()),
                    str(ent4.get()),
                    str(c1.get()),
                    str(ent6.get()),
                    str(ent7.get()),
                    str(ent8.get())))
    conn.commit()
    '''
    ent1.set("")
    c.set("")
    ent3.set("")
    ent4.set("")
    c1.set("")
    ent6.set("")
    ent7.set("")
    ent8.set("")'''

    cursor.close()
    conn.close()
    messagebox.showinfo("SUCCESS !","Record saved Successfully!")


    







#============================ WINDOW SETTINGS ========================================================#
root = Tk()
root.geometry('1300x800+100+100')
root.title("SCHOOL MANAGEMENT SYSTEM")

root.resizable(False,False)

p1 = PhotoImage(file="Resources//NBFrYx.png")
root.iconphoto(False,p1)

xyz = PhotoImage(file='Resources//NBFrYx.png')
lbl1 = Label(root,image=xyz)
lbl1.place(x=0,y=0)

#=============================== WINDOW LABELS====================================================================#
lbl2 = Label(root,text="Welcome Admin",font=('times','40','bold'),bg='orange')
lbl2.place(x=450,y=0)

ff = Frame(root,height=6,width=10000,border=10)
ff.place(x=0,y=80)

lbl3 = Label(root,text="SCHOOL MANAGEMENT SYSTEM",font=('times','40','bold'),bg='orange')
lbl3.place(x=250,y=100)

lbl4 = Label(root,text="Student Name",font=('times','20','bold'))
lbl4.place(x=50,y=200)

lbl5 = Label(root,text="Class&Section",font=('times','20','bold'))
lbl5.place(x=50,y=270)

lbl6 = Label(root,text="ID or RollNo.",font=('times','20','bold'))
lbl6.place(x=50,y=340)

lbl7 = Label(root,text="Date Of Birth",font=('times','20','bold'))
lbl7.place(x=50,y=410)

lbl8 = Label(root,text="Batch Year",font=('times','20','bold'))
lbl8.place(x=50,y=480)

lbl9 = Label(root,text="Father's Name",font=('times','20','bold'))
lbl9.place(x=50,y=550)

lbl10 = Label(root,text="Mother's Name",font=('times','20','bold'))
lbl10.place(x=50,y=620)

lbl11 = Label(root,text="Percentage in previous grade",font=('times','20','bold'))
lbl11.place(x=50,y=690)

lbl12 = Label(root,text="Student info",font=('times','20','bold'))
lbl12.place(x=630,y=200)

#================================ Frames ==================================================================#

ff1 = Frame(root,height=10,width=10000,border=20)
ff1.place(x=0,y=170)

ff2 = Frame(root,height=10000,width=30,border=20)
ff2.place(x=0,y=180)

ff3 = Frame(root,height=10000,width=30,border=20)
ff3.place(x=1270,y=180)

ff4 = Frame(root,height=30,width=10000,border=20)
ff4.place(x=0,y=780)

ff5 = Frame(root,height=10000,width=30,border=20)
ff5.place(x=600,y=180)


#===================================== WIDGETS ======================================================#

stu_lst=['Anil kumar','12 SCIENCE(MATHS)',213516,'2005-04-27','2022-2023','Manoj Kumar','Devi kumar','88%','','','','','','','','Total Students Recorded: 2319','Total Students searched: 2320','Time Taken to Load Data: 3sec']
list1=tk.StringVar(value=stu_lst)
lst=Listbox(root,selectmode=SINGLE,listvariable=list1,bg="gray",fg="white",font=('arial',15),height=20,width=47,selectbackground="gray",selectforeground="white")
lst.grid(columnspan=12)
lst.place(x=630,y=230)

btn = Button(root,text="Load data",font=('Times',20,'bold'),border=5)
btn.place(x=630,y=720)

btn2 = Button(root,text="Save data",font=('Times',13,'bold'),border=5,width=15,command=save)
btn2.place(x=50,y=740)

btn3 = Button(root,text="Modify data",font=('Times',13,'bold'),border=5,width=15,state=DISABLED)
btn3.place(x=230,y=740)

btn4 = Button(root,text="Delete data",font=('Times',13,'bold'),border=5,width=15,state=DISABLED)
btn4.place(x=410,y=740) 



#===================================== Entries =====================================================#

ent1 = Entry(root,font=('Times',20,'bold'))
ent1.place(x=240,y=200)

# 2 drop down list
c=ttk.Combobox(root, width=20, values=['11 SCIENCE(MATHS)','11 SCIENCE(BIO)','12 SCIENCE(MATHS)','12 SCIENCE(BIO)','11 COMMERCE','12 COMMERCE','11 HUMANITIES','12 HUMANITIES'],font=('Times',20,'bold') )
c.place(x=250,y=270)

ent3 = Entry(root,font=('Times',20,'bold'))
ent3.place(x=240,y=340)

ent4 = Entry(root,font=('Times',20,'bold'))
ent4.place(x=240,y=410)

c1=ttk.Combobox(root, width=10, values=['2018-2019','2019-2020','2020-2021','2021-2022','2022-2023','2023-2024'],font=('Times',20,'bold') )
c1.place(x=250,y=480)
# 5 DROP DOWN LIST

ent6 = Entry(root,font=('Times',20,'bold'))
ent6.place(x=240,y=550)

ent7 = Entry(root,font=('Times',20,'bold'))
ent7.place(x=240,y=620)

ent8 = Entry(root,font=('Times',20,'bold'),width=10)
ent8.place(x=400,y=694)











root.mainloop()