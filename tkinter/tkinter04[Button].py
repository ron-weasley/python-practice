import tkinter as tk
def lol():
    btn2.configure(text="lol")

root = tk.Tk()
root.geometry("200x200")
btn1 = tk.Button(root,command=lol, text="Do not click!")
btn1.grid(column =0, row=1)
btn2 = tk.Button(root, text="Click here!", bg="#000", fg="green")
btn2.grid(column =0, row=0)
root.mainloop()
