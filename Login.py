from tkinter import *
import tkinter.font as font




root = Tk()

root.geometry('900x600+200+100')
root.title("Login")

root.resizable(False,False)
#root.bell()
#root.iconify()

myFont = font.Font(family='Helvetica',size=40,slant='italic')

myFont2 = font.Font(family=' verdana ',size=20)

p1 = PhotoImage(file="Resources//Anthony_backround2.png")
root.iconphoto(False,p1)

ff = Frame(root,width=900,height=56,bg='black')
ff.place(x=0,y=30)

ff1 = Frame(root,width=10,height=600,bg='pink')
ff1.place(x=500,y=0)

xyz = PhotoImage(file="Resources//abstract-wallpaper-97-900x600.png")
l = Label(root,image=xyz)
l.place(x=0,y=0)

ppp = PhotoImage(file="Resources//Sample_User_Icon.png")
l_u = Label(root,image=ppp)
l_u.place(x=479,y=200)

aaa = PhotoImage(file="Resources//login-page-password.png")
l_p = Label(root,image=aaa)
l_p.place(x=479,y=250)

lbl1 = Label(root,text="LOGIN",fg='black')
lbl1['font'] = myFont

lbl1.place(x=180,y=30)

lbl2 = Label(root,text="Username")
lbl2['font'] = myFont2
lbl2.place(x=100,y=200)

lbl3 = Label(root,text="Password")
lbl3['font'] = myFont2
lbl3.place(x=100,y=250)

lbl4 = Label(root,text="Don't have an account ?")
lbl4['font'] = myFont2
lbl4.place(x=285,y=550)

ue=Entry(root,font=('bold',14))
ue.place(x=250,y=200)

pe=Entry(root,font=('bold',14),show="•")
pe.place(x=250,y=250)


def reg():
    import Register



b1=Button(root,text='Register',font=('bold',14),command=reg)
b1.place(x=600,y=550)

def cont():
    import sqlite3
    from tkinter import messagebox

    con = sqlite3.connect("info.db")
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM user where unm=? AND pas=?",
                   (str(ue.get()),
                    str(pe.get())))
    row = cursor.fetchone()
    
    if row:
       
        root.destroy()
        import Content
    else:
        messagebox.askretrycancel('error','Login Failed!')
    
def close():
    from tkinter import messagebox
    a = messagebox.askyesno('Confirm','Are your sure you want to Quit')
    if a == 1:
        root.destroy()
    
    
    
    
        
    

b2=Button(root,text='Continue',font=('bold',15),width=10,command=cont)
b2.place(x=300,y=300)

btn3 = Button(root,text='Quit',font=('bold',15),width=10,command=close)
btn3.place(x=770,y=550)

root.mainloop()



