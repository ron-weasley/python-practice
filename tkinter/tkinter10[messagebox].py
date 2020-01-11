from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
def clicked():
    messagebox.showinfo('Message title', 'Message content')
def warn():
    messagebox.showwarning('Message title', 'Message content')
def error():
    messagebox.showerror('Message title', 'Message content')
def ask():
    res = messagebox.askquestion('Message title','Message content')
    btn3.configure(text=res)

btn = Button(window,text='message', command=clicked)
btn.grid(column=0,row=0)
btn1 = Button(window,text='warn', command=warn)
btn1.grid(column=0,row=1)
btn2 = Button(window,text='error', command=error)
btn2.grid(column=0,row=2)
btn3 = Button(window,text='Click here', command=ask)
btn3.grid(column=0,row=3)
window.mainloop()
# res = messagebox.askyesno('Message title','Message content')
# res = messagebox.askyesnocancel('Message title','Message content')
# res = messagebox.askokcancel('Message title','Message content')
# res = messagebox.askretrycancel('Message title','Message content')