import tkinter as tk
def getCommand():
    label1.configure(text=(inp.get()))
    inp.configure(state="disabled")

root = tk.Tk()
root.geometry("200x200")
btn1 = tk.Button(root,command=getCommand, text="get!")
btn1.grid(column =0, row=2)
# btn2= tk.Button(root,command=lol, text="set!")
# btn2.grid(column =0, row=2)
label1 = tk.Label(root, text="Type something!")
label1.grid(column=0, row =0)

inp = tk.Entry(root, width=20)
inp.grid(column=0, row=1)
inp.focus()

root.mainloop()