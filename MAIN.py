#splesh screen

from tkinter import *
from tkinter.ttk import Progressbar
import time



def splesh():
    w=Tk()

    w.geometry("800x533+200+100")
    w.config(bg="Purple")
    w.overrideredirect(True)



    xyz = PhotoImage(file="Resources//Anthony_backround.png")
    l1 = Label(w,image=xyz)
    l1.place(x=0,y=0)

    ppp = PhotoImage(file="Resources//images.png")
    l2 = Label(w,image=ppp)
    l2.place(x=320,y=250)

    lbl = Label(w,text="Welcome,user !",font=('Times',40,'bold','italic'), ).place(x=220,y=0)

    lbl_header = Label(w,text="St Anthony's Sr Sec. School",font=('Times',40,'bold'))
    lbl_header.place(x=100,y=150)

    lbl_version = Label(w,text="version 1.0.0",font=('Times',9,'bold'))
    lbl_version.place(x=530,y=0)

    progress = Progressbar(w, orient = HORIZONTAL,length = 350)
    progress.place(x=200,y=454)


    lb1=Label(w,text='0%',font=("Arial",16))
    lb1.place(x=550,y=450)

    lbl2 = Label(w,text="LOADING",font=("times",20,'bold'))
    lbl2.place(x=300,y=480)

    lbl3 = Label(w,text="",font=("times",20,'bold'))
    lbl3.place(x=300,y=480)

    lbl4 = Label(w,text="",font=("times",20,'bold'))
    lbl4.place(x=300,y=480)

    lbl5 = Label(w,text="",font=("times",20,'bold'))
    lbl5.place(x=300,y=480)

    lbl6 = Label(w,text="Made by ~~ Nimitt Sharma. 2022 under Guidance of SUNIL KUMAR SHARMA.",font=("verdana",10))
    lbl6.place(x=0,y=580)

    def bar(): 

            for i in range(1,101,):
                    progress['value'] = i
                    w.update_idletasks() 
                    time.sleep(1)
                    s=str(i)+" %"
                    p="INITIALIZING"
                    d="Checking OS        "
                    f="Unzipping          "
            
                    lb1.config(text= s)
                    if i == 20:
                        lbl2.destroy()
                        lbl3.config(text= p)
                    elif i == 50:
                        lbl3.destroy()
                        lbl4.config(text= d)
                
                    elif i == 70:
                        lbl4.destroy()
                        lbl5.config(text= f)
                    
                
                


    def close():
        bar()
        w.destroy()
        
    w.after(1000,close)






    w.mainloop()

    def show():
        import Login

    show()











if __name__ == '__main__':
    splesh()
else:
    print("Error : Code 101")
    







