from calendar import c
import tkinter as tk
from tkinter import ttk
from turtle import st
from windows import set_dpi_awareness

set_dpi_awareness() # dpi setting for windows

#Basic screen setups
root = tk.Tk()
root.title("Distance Coverter")
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
meter_input = ttk.Entry(main, width=10, textvariable=meters_values)
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet show here", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meter_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
meter_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
meter_input.focus()
feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()