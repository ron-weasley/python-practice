from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
var=IntVar()
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
var.set(36)
spin.grid(column=0,row=0)
window.mainloop()
