import tkinter as tk
from tkinter import ttk
def lol():
    btn1.configure(text=c.get())

root = tk.Tk()
root.geometry("200x200")
btn1 = tk.Button(root,command=lol, text="Do not click!")
btn1.grid(column =0, row=0)
c=tk.IntVar()
c.set(False)
# c=tk.BooleanVar()
# c.set(False)
check = ttk.Checkbutton(root, text="lol or !lol", var=c)
check.grid(column=0, row=1)

root.mainloop()
