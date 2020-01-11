import tkinter as tk
from tkinter.ttk import *
def click():
    if label.cget("text") == "none selected":
        label.configure(text="")
    label.configure(text=(label.cget("text") + str(c.get())))

window = tk.Tk()
label = tk.Label(window, text="none selected")
label.grid(column=0, row=1, columnspan=3)
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")
c=tk.IntVar()
rad1 = Radiobutton(window, text="First", value=1, command=click, var=c)
rad2 = Radiobutton(window, text="Second", value=2, command=click, var=c)
rad3 = Radiobutton(window, text="Third", value=3, command=click, var=c)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()
