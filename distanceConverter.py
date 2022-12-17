
import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from turtle import st
from windows import set_dpi_awareness

set_dpi_awareness() # dpi setting for windows

#Basic screen setups
root = tk.Tk()
root.title("Distance Coverter")

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

# meter to feet conversion

meters_values = tk.StringVar()
feet_value = tk.StringVar()

def calculate_feet(*args):
    try:
        meter = float(meters_values.get())
        feet = meter * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

# Converter screeen

meter_label = ttk.Label(main, text="Meters:")
meter_input = ttk.Entry(main, width=10, textvariable=meters_values, font=("Arial", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet show here", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meter_label.grid(column=0, row=0, sticky="W")
meter_input.grid(column=1, row=0, sticky="EW")
meter_input.focus()
feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

# Updating padding
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

# Adding key binding

root.bind("<Return>", calculate_feet) 
root.bind("<KP_Enter>", calculate_feet) 

root.mainloop()