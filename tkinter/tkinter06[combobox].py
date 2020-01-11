import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("200x200")

combo = ttk.Combobox(root)
combo["values"] = (1, 3, "asdf")
combo.current(0)
combo.grid(column=0, row=0)

# combo.get()

root.mainloop()
