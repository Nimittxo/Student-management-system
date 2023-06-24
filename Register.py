from tkinter import *
import tkinter.font as font
import time


  
root = Tk()
root.geometry('900x600+200+100')
root.title("REGISTER")
root.overrideredirect(True)

myFont = font.Font(family='Helvetica',size=40,slant='italic')

myFont2 = font.Font(family=' verdana ',size=20)


ff = Frame(root,width=900,height=56,bg='light blue')
ff.place(x=0,y=30)

ff1 = Frame(root,width=100,height=600,bg='light blue')
ff1.place(x=500,y=0)







lbl1 = Label(root,text="REGISTER",fg='black',font=('Helventica',40,'italic'))


lbl1.place(x=180,y=30)

lbl2 = Label(root,text="Username")
lbl2['font'] = myFont2
lbl2.place(x=100,y=200)

lbl3 = Label(root,text="Password")
lbl3['font'] = myFont2
lbl3.place(x=100,y=250)

lbl2 = Label(root,text="First Name")
lbl2['font'] = myFont2
lbl2.place(x=100,y=300)

lbl2 = Label(root,text="Last Name")
lbl2['font'] = myFont2
lbl2.place(x=100,y=350)

lbl2 = Label(root,text="E-mail ID")
lbl2['font'] = myFont2
lbl2.place(x=100,y=400)

lbl2 = Label(root,text="Phone No.")
lbl2['font'] = myFont2
lbl2.place(x=100,y=450)

ue=Entry(root,font=('Times',14,'bold'))
ue.place(x=250,y=200)

pe=Entry(root,font=('Times',14,'bold'),show='•')
pe.place(x=250,y=250)

qe=Entry(root,font=('Times',14,'bold'))
qe.place(x=250,y=300)

ee=Entry(root,font=('Times',14,'bold'))
ee.place(x=250,y=350)

re=Entry(root,font=('Times',14,'bold'))
re.place(x=250,y=400)

se=Entry(root,font=('Times',14,'bold'))
se.place(x=250,y=450)


def reg_btn():
    import sqlite3
    print("Module Imported !")


    con = sqlite3.connect('info.db')
    print("data file made !")

    cursor = con.cursor()
    print("cursor connected")
    
    if  ue.get() == ""or pe.get() == ""or qe.get() == ""or ee.get() == ""or re.get() == ""or se.get() == "":
        from tkinter import messagebox
        messagebox.showerror('ERROR 100','Entries Cannot be Empty')
    else:    
        cursor.execute('''create table if not exists user (
        unm TEXT,
        pas TEXT,
        f_nm TEXT,
        l_nm TEXT,
        E_mail TEXT,
        mob INTEGER
        )''')
        print("table created")

        cursor.execute("INSERT INTO user (unm, pas, f_nm, l_nm, E_mail, mob) VALUES(?, ?, ?, ?, ?, ?)",
                       (str(ue.get()),
                        str(pe.get()),
                        str(qe.get()),
                        str(ee.get()),
                        str(re.get()),
                        str(se.get())))
        con.commit()
        cursor.close()
        con.close()

    
        lbl7 = Label(root,text="Credential Registered successfully !",font=('Times',20,'bold'),fg='Green')
        lbl7.place(x=50,y=500)
    
        def close():
            root.destroy()
    
        root.after(1300,close)

def close():
    from tkinter import messagebox
    messagebox.showerror("ERROR 001","Cannot Close without Giving Any Entry")


btn = Button(root,text='Register',font=('Times',10,'bold'),width=12,height=2,border=5,command=reg_btn)

btn.place(x=500,y=500)

btn2 = Button(root,text='Quit',font=('Times',10,'bold'),width=12,height=2,border=5,command=close)
btn2.place(x=780,y=550)
root.mainloop()




