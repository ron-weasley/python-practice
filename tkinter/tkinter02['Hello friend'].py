import tkinter as tk

root = tk.Tk()
root.title("first")
root.geometry("500x500")
label = tk.Label(root, font=("monospace", 50), text="Hello, friend!")
# label.pack(padx=40, pady=40)
label.grid(column=1, row=0)
root.mainloop()