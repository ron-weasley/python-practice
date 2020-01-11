from tkinter import *
from tkinter import scrolledtext
def clear():
    txt.delete(1.0,END)
    # txt.insert(INSERT,'You text goes here') # to append to text

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
btn1 = Button(window,command=clear, text="clear")
btn1.grid(column =0, row=1)
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=0)

window.mainloop()