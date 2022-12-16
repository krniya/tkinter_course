
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

# ! Scroll bar in text box

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
# check.pack()

# ! Radio button

storage = tk.StringVar()

option1 = ttk.Radiobutton(root, text="Option1", variable=storage, value="Option1")
option2 = ttk.Radiobutton(root, text="Option2", variable=storage, value="Option2")
option3 = ttk.Radiobutton(root, text="Option3", variable=storage, value="Option3")

# option1.pack()
# option2.pack()
# option3.pack()

# ! Combo Boxes

selected = tk.StringVar()

weekday = ttk.Combobox(root, textvariable=selected)
weekday["value"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# weekday.pack()

def handleWeek(event):
    print("Today is ", selected.get())
    print("But we're gonna change it to friday.")
    selected.set("Friday")
    print(weekday.current())

weekday.bind("<<ComboboxSelected>>", handleWeek)


# ! ListBoxes

prog_lang = ("C", "C++", "JavaScript", "Python", ".net")

langs = tk.StringVar(value=prog_lang)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
# langs_select.pack()

def handle_select(event):
    selected_indice = langs_select.curselection()
    for i in selected_indice:
        print(langs_select.get(i))

# langs_select.bind("<<ListboxSelect>>", handle_select)

# ! SpinBox

inital = tk.IntVar(value=20)
spinBox = ttk.Spinbox(root, from_=0, to=30, textvariable=inital, wrap=False)
# spinBox.pack()

# ! Scale
def handleScale(event):
    print(scale.get())


scale = ttk.Scale(root, orient="horizontal", from_=0, to=10, command=handleScale)
scale.pack(fill="x")


root.mainloop()