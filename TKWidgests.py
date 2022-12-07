
from tabnanny import check
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
# label.pack()

# ? Image additon
image = Image.open("tkinter_widget.png").resize((100,100))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Python", image=photo, padding=5, compound="bottom")
# label.pack()

# ! Text widget

text = tk.Text(root, height=8)
# text.grid(row=0, column=1, sticky="ns")

# * Inserting a value in textbox

text.insert("1.0", "Please enter a comment...")
text["state"] = "normal" # "disabled"
text_content = text.get("1.0", "end" )

# ? Scroll bar in text box

text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# text_scroll.grid(row=0, column=1, sticky="ns")
text["yscrollcommand"] = text_scroll.set


# ! Seperator widget

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# ttk.Label(root, text="Hello", padding=20).pack()

# ttk.Separator(root, orient="horizontal").pack(fill="x")

# ttk.Label(root, text="Hello", padding=20).pack()

# ! Check button

check_button = ttk.Checkbutton(root, text="Click me!")
# check_button.pack()

selected_option = tk.StringVar()

def print_curr_option():
    print(selected_option.get())

check = ttk.Checkbutton(
    root,
    text="Check",
    variable=selected_option,
    command=print_curr_option,
    onvalue="On",
    offvalue="Off"
)
check.pack()

root.mainloop()