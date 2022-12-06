
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

# ! Basic TKinter template

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

# ! Label 
label = ttk.Label(root, text="Hello World!", padding=20)
label.config(font=("Segoe UI", 20))
label.pack()

# ? Image additon
image = Image.open("tkinter_widget.png").resize((100,100))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Python", image=photo, padding=5, compound="bottom")
label.pack()



root.mainloop()