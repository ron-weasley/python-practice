import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("img1.PNG"))

label = tk.Label(root, image=img)
label.grid(column=0, row=0)

root.mainloop()