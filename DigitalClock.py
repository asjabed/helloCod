
from tkinter import *
from tkinter import font
import datetime

def clock():
    tm=datetime.datetime.now()
    time=tm.strftime('%H:%M:%S')
    mytext.set(time)
    win.after(1000,clock)

    
win=Tk()
win.title('Digital Clock')
win.geometry('800x400')
win.resizable(False,False)
win.configure(background='black')

myfont=font.Font(family='poppins', size=120, weight='bold')
mytext=StringVar()



lblTime=Label(win,textvariable=mytext,font=myfont,foreground='white',background='black')
lblTime.place(relx=0.5,rely=0.5,anchor=CENTER)

win.after(1000,clock)
win.mainloop()